#!/usr/bin/env nu

# UTC timestamp utility. Prints ISO 8601 timestamp, optionally updates a file's
# *Updated:* line in-place.
#
# Usage:
#   nu scripts/ts.nu                          Print timestamp
#   nu scripts/ts.nu lode/framework/rules.md  Update *Updated:* line + print

def main [
    file?: path   # Optional file to update the *Updated:* timestamp line in-place
] {
    let ts = (date now | date to-timezone "UTC" | format date "%Y-%m-%dT%H:%M:%SZ")

    if ($file | is-empty) {
        print $ts
        return
    }

    if not ($file | path exists) {
        print $"Error: ($file) does not exist"
        exit 1
    }

    let content = (open $file --raw)
    let updated = ($content | str replace --regex '\*Updated: [^\*]+\*' $"*Updated: ($ts)*")

    if $content == $updated {
        print $"No *Updated:* line found in ($file). Timestamp: ($ts)"
    } else {
        $updated | save $file --force
        print $"Updated ($file) → ($ts)"
    }
}
