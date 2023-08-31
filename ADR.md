# Architecture Decision Records

This document contains the Architecture Decision Records (ADRs) for the Anki flash card generation project, which are used to document the architectural decisions made during the development process and the reasons behind them.

## ADR 001: JSON as Input Data Format

**Title:** Using JSON as the Input Data Format for Student Information

**Status:** Accepted

**Context:** The project requires a structured and standardized format to input student data, including names, images, and other relevant details.

**Decision:** Adopt JSON as the primary input format due to its widespread use, ease of parsing, and compatibility with various tools.

**Consequences:**
- Simplified data parsing and processing.
- Direct compatibility with the Penn Class List Scraper output.
- Requirement for users to have data in JSON format.

---

## ADR 002: Base64 Encoding for Image Embedding

**Title:** Embedding Student Images as Base64 in Anki Cards

**Status:** Accepted

**Context:** Anki cards need to display student images, but managing external image files can be cumbersome and may lead to broken links.

**Decision:** Embed images directly into Anki cards using Base64 encoding to ensure portability and eliminate external dependencies.

**Consequences:**
- Increased size of the Anki deck due to embedded images.
- Elimination of potential broken image links.
- Simplified import process for users.

---

## ADR 003: CLI Tool for Deck Generation

**Title:** Development of a Command-Line Interface (CLI) Tool for Anki Deck Generation

**Status:** Accepted

**Context:** Users may prefer a scriptable and automated way to generate Anki decks without relying on a web interface.

**Decision:** Develop a Python-based CLI tool that allows users to generate Anki decks directly from the command line.

**Consequences:**
- Increased flexibility for users familiar with the command line.
- Requirement to maintain both web and CLI versions of the tool.
- Potential for integration into automated workflows.

---

## ADR 004: Separate Decks Based on JSON Files

**Title:** Option to Generate Separate Anki Decks Based on Input JSON Files

**Status:** Accepted

**Context:** Users might have student data segmented into different JSON files based on sections or other criteria.

**Decision:** Provide an option in the CLI tool to generate separate Anki decks for each input JSON file.

**Consequences:**
- Enhanced organization of Anki decks.
- Additional complexity in the CLI tool to handle multiple output files.

---

## ADR 005: GitHub Pages for Web Tool Hosting

**Title:** Using GitHub Pages for Hosting the Web-Based Anki Deck Generator

**Status:** Accepted

**Context:** The web-based tool needs a hosting solution that is easy to manage, cost-effective, and reliable.

**Decision:** Use GitHub Pages to host the web-based Anki Deck Generator, leveraging its free hosting for static sites.

**Consequences:**
- Zero hosting costs.
- Direct integration with the project's GitHub repository.
- Limitation to static content, but suitable for the project's requirements.

