#!/usr/bin/env nu

# Lode timestamp updater. Bumps *Updated:* lines to current UTC in lode files.
# Replaces the 2-call pattern: Read file → Edit timestamp line.
#
# Usage:
#   nu scripts/pug-lode-ts.nu lode/framework/rules.md     Update one file
#   nu scripts/pug-lode-ts.nu lode/summary.md lode/practices.md   Multiple files
#   nu scripts/pug-lode-ts.nu --changed                     Auto-detect from git diff
#   nu scripts/pug-lode-ts.nu --changed --json             JSON output
#   nu scripts/pug-lode-ts.nu --dry-run --changed           Preview without writing
#   nu scripts/pug-lode-ts.nu --stale                       Report stale lode files
#   nu scripts/pug-lode-ts.nu --stale --json                JSON staleness report
#   nu scripts/pug-lode-ts.nu --now                         Print current UTC timestamp

const LODE_DIR = "lode"

def main [
    ...files: string     # Lode files to update (relative paths)
    --changed            # Auto-detect changed lode files from git
    --dry-run            # Preview without writing
    --stale              # Report lode files by staleness (days since update + commits since)
    --json               # Output as JSON (with --stale or --changed)
    --now                # Print current UTC timestamp and exit
] {
    if $now {
        print (date now | date to-timezone "UTC" | format date "%Y-%m-%dT%H:%M:%SZ")
        return
    }
    if $stale {
        cmd-stale $json
        return
    }
    let ts = (date now | date to-timezone "UTC" | format date "%Y-%m-%dT%H:%M:%SZ")

    let targets = if $changed {
        detect-changed-lode-files
    } else if ($files | is-not-empty) {
        $files
    } else {
        print "Usage: pug-lode-ts <file...> or pug-lode-ts --changed"
        exit 1
    }

    if ($targets | is-empty) {
        if $json {
            print '{"files": [], "message": "No lode files to update"}'
        } else {
            print "No lode files to update."
        }
        return
    }

    # JSON output for integration
    if $json and $changed {
        let result = {
            files: ($targets | each {|f|
                let content = (open $f --raw)
                let has_ts = ($content | str contains "*Updated:") or ($content | str contains "*Created:")
                let needs_update = if $has_ts {
                    let current = if ($content | str contains "*Updated:") {
                        $content | parse --regex '\*Updated:\s*(?P<ts>[^\*]+)\*' | get -o ts | default [null] | first | str trim
                    } else {
                        $content | parse --regex '\*Created:\s*(?P<ts>[^\*]+)\*' | get -o ts | default [null] | first | str trim
                    }
                    $current != $ts
                } else {
                    false
                }
                {
                    path: $f
                    has_timestamp: $has_ts
                    needs_update: $needs_update
                }
            })
            timestamp: $ts
        }
        $result | to json
        return
    }

    mut updated_count = 0

    for file in $targets {
        if not ($file | path exists) {
            print $"  SKIP: ($file) — not found"
            continue
        }

        let content = (open $file --raw)

        # Match *Updated: ...* or *Created: ...* timestamp pattern
        let has_updated = ($content | str contains "*Updated:")
        let has_created = ($content | str contains "*Created:")

        if (not $has_updated) and (not $has_created) {
            print $"  SKIP: ($file) — no timestamp line"
            continue
        }

        let new_content = if $has_updated {
            $content | str replace --regex '\*Updated: [^\*]+\*' $"*Updated: ($ts)*"
        } else {
            $content | str replace --regex '\*Created: [^\*]+\*' $"*Updated: ($ts)*"
        }

        if $content == $new_content {
            print $"  SKIP: ($file) — already current"
            continue
        }

        if $dry_run {
            print $"  WOULD: ($file) → ($ts)"
        } else {
            $new_content | save $file --force
            print $"  ($file) → ($ts)"
        }
        $updated_count = $updated_count + 1
    }

    if $updated_count > 0 {
        let verb = if $dry_run { "Would update" } else { "Updated" }
        print $"\n($verb) ($updated_count) file\(s) → ($ts)"
    }
}

# Report staleness of all lode files with timestamps.
def cmd-stale [json_mode: bool] {
    let now = (date now)
    let lode_files = (glob $"($LODE_DIR)/**/*.md" | where {|f|
        not ($f | str contains "/tmp/") and not ($f | str contains "/completed/")
    } | sort)

    mut rows = []

    for file in $lode_files {
        let rel = ($file | path relative-to (pwd))
        let content = (open $file --raw)

        # Extract timestamp from *Updated: ...* or *Created: ...*
        let ts_match = if ($content | str contains "*Updated:") {
            $content | parse --regex '\*Updated:\s*(?P<ts>[^\*]+)\*' | get -o ts | default [null] | first
        } else if ($content | str contains "*Created:") {
            $content | parse --regex '\*Created:\s*(?P<ts>[^\*]+)\*' | get -o ts | default [null] | first
        } else {
            null
        }

        if ($ts_match == null) or ($ts_match | is-empty) {
            continue
        }

        let ts_str = ($ts_match | str trim)
        let ts_date = (try { $ts_str | into datetime } catch { null })
        if ($ts_date == null) { continue }

        let days_ago = (($now - $ts_date) / 1day | math round)

        # Count commits since the timestamp touching non-lode code
        let commits_since = (
            do -i { git log $"--since=($ts_str)" --oneline -- "src/" "tests/" "scripts/" ".claude/" "skills/" }
            | complete
            | get stdout
            | lines
            | where {|l| $l | is-not-empty }
            | length
        )

        $rows = ($rows | append {
            file: $rel,
            updated: $ts_str,
            days_ago: $days_ago,
            commits_since: $commits_since,
        })
    }

    # Sort by staleness (most stale first)
    let sorted = ($rows | sort-by days_ago --reverse)

    if $json_mode {
        $sorted | to json | print
        return
    }

    if ($sorted | is-empty) {
        print "No lode files with timestamps found."
        return
    }

    # Table header
    print $"('' | fill -c ' ' -w 6)days  commits  file"
    print $"('' | fill -c '─' -w 50)"
    for row in $sorted {
        let days_str = ($row.days_ago | into string | fill --alignment right --width 4)
        let commits_str = ($row.commits_since | into string | fill --alignment right --width 5)
        let stale_marker = if $row.days_ago > 14 and $row.commits_since > 5 { " !" } else { "  " }
        print $"($stale_marker)  ($days_str)  ($commits_str)  ($row.file)"
    }

    let stale_count = ($sorted | where {|r| $r.days_ago > 14 and $r.commits_since > 5 } | length)
    if $stale_count > 0 {
        print ""
        print $"($stale_count) file\(s) likely stale \(>14 days old, >5 commits since)"
    }
}

# Find lode files that have been modified in the working tree (git status based).
def detect-changed-lode-files [] {
    do -i { git status --short } | complete | get stdout
    | lines
    | where { |l| ($l | is-not-empty) }
    | each { |l| $l | str trim | str replace --regex '^[A-Z?]{1,2}\s+' '' | str trim }
    | where {|f| ($f | str starts-with $"($LODE_DIR)/") and ($f | str ends-with ".md") and (not ($f | str contains "/tmp/")) }
}
