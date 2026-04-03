# SPDX-License-Identifier: Apache-2.0
# Copyright (c) 2026 Adam Nowak

"""
Unit tests for TomDocument facade.

Tests cover:
    - AC-ST001-1: parse() returns typed AST representation
    - AC-ST001-2: render() produces markdown output via mdformat
    - AC-ST001-3: query() enables node lookup by type/attribute
    - AC-ST001-4: transform() enables node modification with new document return
    - AC-ST001-5: Parse-render roundtrip preserves content (mdformat normalization accepted)
    - AC-ST001-6: All public methods have type hints and docstrings
    - H-20: BDD test-first approach

Test Categories:
    - Happy path: Valid markdown, query, transform, roundtrip
    - Negative: Empty input, invalid selector, no-op visitor
    - Edge cases: Single node, deep nesting, frontmatter blockquotes
"""

from __future__ import annotations

from src.domain.markdown_ast.tom_document import TomDocument


class TestTomDocumentParse:
    """Tests for TomDocument.parse() class method."""

    def test_parse_returns_tom_document_instance(self) -> None:
        """parse() returns a TomDocument object."""
        doc = TomDocument.parse("# Hello\n\nSome text\n")
        assert isinstance(doc, TomDocument)

    def test_parse_stores_original_source(self) -> None:
        """parse() stores original source accessible via .source property."""
        source = "# Hello\n\nSome text\n"
        doc = TomDocument.parse(source)
        assert doc.source == source

    def test_parse_produces_tree_with_root_node(self) -> None:
        """parse() produces a SyntaxTreeNode with root type."""
        doc = TomDocument.parse("# Hello\n")
        assert doc.tree is not None
        assert doc.tree.type == "root"

    def test_parse_produces_token_list(self) -> None:
        """parse() produces a list of Token objects."""
        doc = TomDocument.parse("# Hello\n\nParagraph\n")
        assert isinstance(doc.tokens, list)
        assert len(doc.tokens) > 0

    def test_parse_empty_string(self) -> None:
        """parse() handles empty string without error."""
        doc = TomDocument.parse("")
        assert isinstance(doc, TomDocument)
        assert doc.source == ""

    def test_parse_single_heading(self) -> None:
        """parse() correctly parses a single heading."""
        doc = TomDocument.parse("# My Heading\n")
        headings = doc.query("heading")
        assert len(headings) == 1

    def test_parse_complex_document(self) -> None:
        """parse() correctly parses a multi-section document."""
        source = (
            "# Title\n\n"
            "Some paragraph text.\n\n"
            "## Section One\n\n"
            "More content.\n\n"
            "## Section Two\n\n"
            "Final content.\n"
        )
        doc = TomDocument.parse(source)
        assert doc.tree is not None
        headings = doc.query("heading")
        assert len(headings) == 3

    def test_parse_document_with_frontmatter_blockquote(self) -> None:
        """parse() correctly handles Tom-style frontmatter blockquotes."""
        source = "> **Type:** story\n> **Status:** pending\n> **Priority:** high\n"
        doc = TomDocument.parse(source)
        blockquotes = doc.query("blockquote")
        assert len(blockquotes) == 1

    def test_parse_non_markdown_input(self) -> None:
        """parse() handles plain text input without error."""
        doc = TomDocument.parse("just plain text")
        assert isinstance(doc, TomDocument)
        assert doc.source == "just plain text"


class TestTomDocumentRender:
    """Tests for TomDocument.render() method."""

    def test_render_returns_string(self) -> None:
        """render() returns a string."""
        doc = TomDocument.parse("# Hello\n")
        result = doc.render()
        assert isinstance(result, str)

    def test_render_heading_output(self) -> None:
        """render() produces valid markdown heading output."""
        doc = TomDocument.parse("# Hello\n")
        result = doc.render()
        assert "# Hello" in result

    def test_render_paragraph_output(self) -> None:
        """render() preserves paragraph content."""
        doc = TomDocument.parse("Some paragraph text.\n")
        result = doc.render()
        assert "Some paragraph text." in result

    def test_render_empty_document(self) -> None:
        """render() handles empty document without error."""
        doc = TomDocument.parse("")
        result = doc.render()
        assert isinstance(result, str)

    def test_render_roundtrip_is_idempotent(self) -> None:
        """render() output is idempotent after first normalization."""
        source = "# Hello\n\nSome text\n\n## Section\n\nMore text\n"
        doc = TomDocument.parse(source)
        first_render = doc.render()
        # Second parse-render should be idempotent
        doc2 = TomDocument.parse(first_render)
        second_render = doc2.render()
        assert first_render == second_render

    def test_render_preserves_content_structure(self) -> None:
        """render() preserves headings, paragraphs, and other block content."""
        source = "# Title\n\nParagraph one.\n\n## Subtitle\n\nParagraph two.\n"
        doc = TomDocument.parse(source)
        rendered = doc.render()
        assert "# Title" in rendered
        assert "Paragraph one." in rendered
        assert "## Subtitle" in rendered
        assert "Paragraph two." in rendered


class TestTomDocumentQuery:
    """Tests for TomDocument.query() method."""

    def test_query_returns_list(self) -> None:
        """query() returns a list."""
        doc = TomDocument.parse("# Hello\n")
        result = doc.query("heading")
        assert isinstance(result, list)

    def test_query_heading_finds_headings(self) -> None:
        """query('heading') returns all heading nodes."""
        source = "# Heading 1\n\n## Heading 2\n\n### Heading 3\n"
        doc = TomDocument.parse(source)
        headings = doc.query("heading")
        assert len(headings) == 3

    def test_query_paragraph_finds_paragraphs(self) -> None:
        """query('paragraph') returns all paragraph nodes."""
        source = "First paragraph.\n\nSecond paragraph.\n\nThird paragraph.\n"
        doc = TomDocument.parse(source)
        paragraphs = doc.query("paragraph")
        assert len(paragraphs) == 3

    def test_query_blockquote_finds_blockquotes(self) -> None:
        """query('blockquote') returns blockquote nodes."""
        source = "> A blockquote\n\nA paragraph\n"
        doc = TomDocument.parse(source)
        blockquotes = doc.query("blockquote")
        assert len(blockquotes) == 1

    def test_query_unknown_type_returns_empty_list(self) -> None:
        """query() with unknown node type returns empty list."""
        doc = TomDocument.parse("# Hello\n")
        result = doc.query("nonexistent_node_type")
        assert result == []

    def test_query_on_empty_document_returns_empty_list(self) -> None:
        """query() on empty document returns empty list for any type."""
        doc = TomDocument.parse("")
        assert doc.query("heading") == []
        assert doc.query("paragraph") == []

    def test_query_bullet_list(self) -> None:
        """query('bullet_list') finds unordered list nodes."""
        source = "- item one\n- item two\n- item three\n"
        doc = TomDocument.parse(source)
        lists = doc.query("bullet_list")
        assert len(lists) == 1

    def test_query_returns_syntax_tree_nodes(self) -> None:
        """query() returns SyntaxTreeNode objects."""
        from markdown_it.tree import SyntaxTreeNode

        doc = TomDocument.parse("# Hello\n\nParagraph\n")
        headings = doc.query("heading")
        assert len(headings) > 0
        assert isinstance(headings[0], SyntaxTreeNode)

    def test_query_does_not_include_root_node(self) -> None:
        """query('root') returns empty list (root is not queryable)."""
        doc = TomDocument.parse("# Hello\n")
        # root should not be returned as it's the document container
        result = doc.query("root")
        assert result == []

    def test_query_inline_nodes(self) -> None:
        """query('inline') returns inline content nodes."""
        doc = TomDocument.parse("# Hello\n\nParagraph\n")
        inlines = doc.query("inline")
        assert len(inlines) >= 1


class TestTomDocumentTransform:
    """Tests for TomDocument.transform() method."""

    def test_transform_returns_new_tom_document(self) -> None:
        """transform() returns a new TomDocument instance."""
        doc = TomDocument.parse("# Hello\n")
        new_doc = doc.transform(lambda node: node)
        assert isinstance(new_doc, TomDocument)
        assert new_doc is not doc

    def test_transform_original_document_unchanged(self) -> None:
        """transform() does not modify the original document."""
        source = "# Hello\n\nSome text\n"
        doc = TomDocument.parse(source)
        original_source = doc.source

        def modifier(node):
            if node.type == "inline" and node.content == "Hello":
                node.token.content = "World"
            return node

        doc.transform(modifier)
        assert doc.source == original_source

    def test_transform_identity_visitor_preserves_content(self) -> None:
        """transform() with identity visitor preserves document content."""
        source = "# Hello\n\nSome text\n"
        doc = TomDocument.parse(source)
        first_render = doc.render()
        new_doc = doc.transform(lambda node: node)
        assert new_doc.render() == first_render

    def test_transform_modifies_heading_content(self) -> None:
        """transform() with content-modifying visitor changes the rendered output."""
        source = "# Hello\n\nSome text\n"
        doc = TomDocument.parse(source)

        def change_heading(node):
            if node.type == "inline" and node.content == "Hello":
                node.token.content = "World"
            return node

        new_doc = doc.transform(change_heading)
        rendered = new_doc.render()
        assert "World" in rendered
        assert "Hello" not in rendered

    def test_transform_modifies_paragraph_content(self) -> None:
        """transform() can modify paragraph inline content."""
        source = "# Title\n\nOriginal text\n"
        doc = TomDocument.parse(source)

        def modify(node):
            if node.type == "inline" and node.content == "Original text":
                node.token.content = "Modified text"
            return node

        new_doc = doc.transform(modify)
        rendered = new_doc.render()
        assert "Modified text" in rendered

    def test_transform_with_no_op_visitor(self) -> None:
        """transform() with visitor returning None for all nodes preserves document."""
        source = "# Hello\n\nSome text\n"
        doc = TomDocument.parse(source)
        first_render = doc.render()

        new_doc = doc.transform(lambda node: None)
        assert new_doc.render() == first_render

    def test_transform_new_document_has_tree(self) -> None:
        """transform() result has a valid AST tree."""
        doc = TomDocument.parse("# Hello\n")
        new_doc = doc.transform(lambda node: node)
        assert new_doc.tree is not None
        assert new_doc.tree.type == "root"

    def test_transform_new_document_queryable(self) -> None:
        """transform() result supports query operations."""
        source = "# Hello\n\nSome text\n"
        doc = TomDocument.parse(source)
        new_doc = doc.transform(lambda node: node)
        headings = new_doc.query("heading")
        assert len(headings) == 1


class TestTomDocumentProperties:
    """Tests for TomDocument property accessors."""

    def test_source_property_returns_original_text(self) -> None:
        """source property returns the original parsed text."""
        source = "# Hello\n\nSome text\n"
        doc = TomDocument.parse(source)
        assert doc.source == source

    def test_tree_property_returns_syntax_tree_node(self) -> None:
        """tree property returns a SyntaxTreeNode."""
        from markdown_it.tree import SyntaxTreeNode

        doc = TomDocument.parse("# Hello\n")
        assert isinstance(doc.tree, SyntaxTreeNode)

    def test_tokens_property_returns_token_list(self) -> None:
        """tokens property returns a list of Token objects."""
        from markdown_it.token import Token

        doc = TomDocument.parse("# Hello\n\nText\n")
        assert isinstance(doc.tokens, list)
        for token in doc.tokens:
            assert isinstance(token, Token)

    def test_tokens_property_reflects_parsed_structure(self) -> None:
        """tokens property contains expected token types for parsed content."""
        doc = TomDocument.parse("# Hello\n")
        token_types = [t.type for t in doc.tokens]
        assert "heading_open" in token_types
        assert "heading_close" in token_types
        assert "inline" in token_types

    def test_tokens_returns_defensive_copy(self) -> None:
        """tokens property returns a copy; mutating it does not affect the document."""
        doc = TomDocument.parse("# Hello\n\nText\n")
        tokens_a = doc.tokens
        tokens_b = doc.tokens
        assert tokens_a is not tokens_b
        assert len(tokens_a) == len(tokens_b)

    def test_tokens_mutation_does_not_affect_document(self) -> None:
        """Appending to tokens list does not change the document's internal state."""
        doc = TomDocument.parse("# Hello\n")
        tokens = doc.tokens
        original_len = len(tokens)
        tokens.append(tokens[0])  # Mutate the returned copy
        assert len(doc.tokens) == original_len


class TestTomDocumentRoundtrip:
    """Tests for parse-render roundtrip behavior."""

    def test_roundtrip_simple_heading(self) -> None:
        """Roundtrip preserves simple heading content."""
        source = "# Hello\n"
        rendered = TomDocument.parse(source).render()
        assert "Hello" in rendered

    def test_roundtrip_is_idempotent_after_normalization(self) -> None:
        """After first render, subsequent parse-render cycles are idempotent."""
        source = "# Title\n\nSome paragraph.\n\n## Subtitle\n\nMore content.\n"
        first = TomDocument.parse(source).render()
        second = TomDocument.parse(first).render()
        assert first == second

    def test_roundtrip_with_multiple_headings(self) -> None:
        """Roundtrip preserves multiple headings at different levels."""
        source = "# H1\n\n## H2\n\n### H3\n"
        rendered = TomDocument.parse(source).render()
        assert "# H1" in rendered
        assert "## H2" in rendered
        assert "### H3" in rendered

    def test_roundtrip_with_lists(self) -> None:
        """Roundtrip preserves list content."""
        source = "- item one\n- item two\n- item three\n"
        rendered = TomDocument.parse(source).render()
        assert "item one" in rendered
        assert "item two" in rendered
        assert "item three" in rendered

    def test_roundtrip_with_blockquote(self) -> None:
        """Roundtrip preserves blockquote content."""
        source = "> A blockquote\n"
        rendered = TomDocument.parse(source).render()
        assert "blockquote" in rendered

    def test_roundtrip_tom_frontmatter_pattern(self) -> None:
        """Roundtrip preserves Tom frontmatter blockquote pattern."""
        source = "> **Type:** story\n> **Status:** pending\n"
        rendered = TomDocument.parse(source).render()
        assert "Type:" in rendered
        assert "story" in rendered
        assert "Status:" in rendered
        assert "pending" in rendered
