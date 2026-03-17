# building-with-claude-api

Code samples and tutorials for building with Anthropic Claude APIs across multiple workflows.

## Repository structure

- `Accessing-Claude-with-API/`
  - `Chat Exercise.py`
  - `How to use System Prompt.py`
  - `Making Requests with Claude API Key.ipynb`
  - `Response Streaming.py`
  - `Structuring Data using Control Modelling and Stop Sequences.py`

- `Claude-Code/`
  - `app_starter/`
    - `main.py` (small app starter example)
    - `tools/document.py`, `tools/math.py` (utility tools)
    - `tests/` (unit tests for document tooling)

- `Claude-Features/`
  - Jupyter notebooks exploring Claude features such as thinking, citations, caching, and code execution.
  - `streaming.csv` sample or data artifact from streaming experiments.

- `Model-Context-Protocol/`
  - `cli_project/` and `cli_project_COMPLETE/` with example implementations of a CLI-based MCP server/client and chat core.
  - `core/` modules (`chat.py`, `claude.py`, `cli_chat.py`, `cli.py`, `tools.py`).

- `Prompt-Engineering/` and `Prompt-Evaluation/`
  - Notebooks and datasets for prompt crafting and evaluation.

- `RAG-and-Agentic-Search/`
  - Notebooks covering chunking, embeddings, vector DBs, BM25, reranking, contextual search, and reporting.

- `Tools-with-Claude/`
  - Notebooks demonstrating tools integration, structured data, tool streaming, text editor tools, and web search.

## Key features demonstrated

- System prompts and prompt engineering patterns
- Response streaming and interactive response handling
- Control modeling, stop sequences, and generation constraints
- Retrieval-augmented generation (RAG) and tool-augmented agents
- CLI and protocol-based multi-step agent flows

## How to use

1. Pick the folder matching your workflow (API sample, features deep dive, RAG, etc.).
2. Run notebooks (`.ipynb`) with your Claude API key configured.
3. Review `app_starter` source for Python code patterns and `Model-Context-Protocol` for architecture guidance.
4. Extend with your own tools, retrieval store, or task-specific prompt logic.

## Notes

- These are sample code artifacts for experimentation and learning; customize for production as needed.
- Check each folder-level README (where present) for more details.


