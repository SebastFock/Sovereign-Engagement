# Sovereign Engagement System
**Dogma in constitution, pragmatism in execution.**

A complete ethical-strategic operating system distilled from  
• The Seven Principles of Engagement (2025)  
• 7 Sovereign Principles: Ethics – The Highest Form of Strategy (2026)  
by Sebast Fock.

This repository contains the machine-readable framework and the canonical system prompt that turns any LLM into a native practitioner of the system.

### One-click usage
Copy the content of `canonical-prompt-v3-1.txt` and paste it at the start of any conversation with Claude, ChatGPT, Grok, DeepSeek, Gemini, etc. (Older revisions live in `versions/`.)

### For developers
Load `framework.yml` into LangGraph, CrewAI, AutoGen, LlamaIndex, or any agent framework to give your agents ethical-strategic reasoning by default.

### Real-world examples
See how the framework applies to historical corporate dilemmas: [Meta API Governance](./examples/meta_platform_api.md), [Volkswagen Emissions](./examples/volkswagen_emissions.md)

### License
MIT – use it, fork it, build on it, ship it.

→ Start here: just paste the canonical prompt and watch the quality of advice change forever.

---

# Testing & Validation — Sovereign Shell Test Suite

Evaluation scripts for validating the Sovereign Agent Architecture's compliance detection across different LLM backends:

- **Local models** (Ollama, LM Studio)
- **Commercial APIs** (Claude, GPT-4o)
- **Custom OpenAI-compatible endpoints**

The scripts live in `sovereign-agent-architecture/scripts/`. `custom_api_eval.py` anchors its paths to its own location, so you can launch it from anywhere — the repo root or the scripts folder. Examples below are written for the repo root:

```bash
# From the repo root
python sovereign-agent-architecture/scripts/custom_api_eval.py --run-id claude_test
```

## Installation

```bash
pip install -r sovereign-agent-architecture/requirements.txt
```

## Test Scripts

### 1. `custom_api_eval.py` — Universal OpenAI-Compatible API

Supports any OpenAI-compatible API (local or cloud) with flexible configuration via CLI args or `.env` files.

**Usage:**

```bash
# Using .env file (auto-detected from the script's directory, the current
# directory, and their parents — so it works from the repo root too)
python sovereign-agent-architecture/scripts/custom_api_eval.py --run-id mistral_test

# Using an explicit .env file
python sovereign-agent-architecture/scripts/custom_api_eval.py \
  --env-file sovereign-agent-architecture/.env --run-id mistral_test

# Using CLI arguments
python sovereign-agent-architecture/scripts/custom_api_eval.py \
  --base-url http://localhost:11434/v1 \
  --model mistral:7b \
  --api-key ollama \
  --run-id mistral_test

# CLI args override .env values
python sovereign-agent-architecture/scripts/custom_api_eval.py \
  --base-url http://localhost:1234/v1 \
  --model llama2 \
  --run-id llama_test
```

**.env file:** place it at `sovereign-agent-architecture/.env` (auto-detected). Format:

```env
SOVEREIGN_BASE_URL=http://localhost:11434/v1
SOVEREIGN_MODEL=mistral:7b
SOVEREIGN_API_KEY=ollama
SOVEREIGN_DELAY_SECONDS=0.5
SOVEREIGN_RUN_ID=default

# Optional — leave unset to use the defaults below (resolved relative to the
# script's location, so they work from any directory). Override only with an
# ABSOLUTE path:
# SOVEREIGN_CSV_PATH=/absolute/path/to/test_cases.csv
# SOVEREIGN_OUTPUT_PREFIX=/absolute/path/to/results
```

> **Note:** `.env` holds your API key and is gitignored — never commit it.

**Options:**

- `--env-file PATH` — Path to .env file (auto-detected if omitted)
- `--base-url URL` — Base URL for OpenAI-compatible API
- `--model NAME` — Model name/identifier
- `--api-key KEY` — API key for the service
- `--csv PATH` — Path to test cases CSV (default: `<script_dir>/../data/test_cases.csv`)
- `--output PREFIX` — Output directory prefix (default: `<script_dir>/../results`)
- `--run-id LABEL` — Run label, used as the top-level results folder (e.g. `claude_test`). Default: `SOVEREIGN_RUN_ID` or `default`
- `--delay SECONDS` — Delay between API calls (default: `0.5`)
- `--limit N` — Only run the first N test cases (smoke test before a full run)
- `--verbose`, `-v` — Also print the input messages and raw output of every LLM call to the console (the full log is always saved to `verbose.log` in the run folder regardless)

**Smoke test** (confirm endpoint + parsing on a handful of cases first):

```bash
python sovereign-agent-architecture/scripts/custom_api_eval.py --run-id claude_test --limit 5
```

**Inspect each LLM call** (see exactly what's sent and returned):

```bash
python sovereign-agent-architecture/scripts/custom_api_eval.py --run-id claude_test --limit 5 --verbose
```

#### Local Mistral (Ollama)

1. Install [Ollama](https://ollama.com) and pull the model:

   ```bash
   ollama pull mistral:7b
   ```

2. Ollama serves an OpenAI-compatible API at `http://localhost:11434/v1` (any string works as the API key). Run the eval against it:

   ```bash
   python sovereign-agent-architecture/scripts/custom_api_eval.py \
     --base-url http://localhost:11434/v1 \
     --model mistral:7b \
     --api-key ollama \
     --run-id mistral_local \
     --limit 5          # smoke test first; drop --limit for the full run
   ```

> [LM Studio](https://lmstudio.ai) works the same way — start its local server and point `--base-url` at `http://localhost:1234/v1`.

#### Mock server (no model needed)

To check the script runs end-to-end without a real model server, use the bundled mock that mimics the OpenAI `/chat/completions` endpoint:

```bash
# Terminal 1 — start the mock
python sovereign-agent-architecture/scripts/mock_openai_server.py --port 8765

# Terminal 2 — run the eval against it
python sovereign-agent-architecture/scripts/custom_api_eval.py \
  --base-url http://localhost:8765/v1 \
  --model mistral:7b \
  --api-key mock \
  --run-id mock_test \
  --limit 3 --delay 0
```

---

### 2. `comparison-test-script.py` — Anthropic & OpenAI APIs

Tests against official Anthropic Claude and OpenAI GPT models with structured configuration.

> Run this script from `sovereign-agent-architecture/scripts/` (its paths are relative to that folder).

**Usage:**

```bash
# Test with Claude (Anthropic)
python comparison-test-script.py \
  --provider anthropic \
  --model claude-3-5-sonnet-20241022

# Test with GPT-4o (OpenAI)
python comparison-test-script.py \
  --provider openai \
  --model gpt-4o

# Test with GPT-4o mini (cheaper)
python comparison-test-script.py \
  --provider openai \
  --model gpt-4o-mini
```

**Requirements:**

- Set `ANTHROPIC_API_KEY` or `OPENAI_API_KEY` environment variables
- Or pass `--api-key` to override

**Options:**

- `--provider {openai, anthropic}` — API provider (required)
- `--model NAME` — Model name (required)
- `--api-key KEY` — API key (or set env var)
- `--base-url URL` — Custom base URL (OpenAI-compatible only)
- `--csv PATH` — Path to test cases CSV
- `--output PREFIX` — Output file prefix
- `--delay SECONDS` — Delay between API calls

---

### 3. `mistral_shell_eval.py` — Local Ollama Models

Tests against locally-running models via Ollama (requires Ollama running at `localhost:11434`).

> Run this script from `sovereign-agent-architecture/scripts/` (its paths are relative to that folder).

**Setup:**

```bash
# Install Ollama from https://ollama.ai

# Start Ollama server
ollama serve

# In another terminal, pull a model
ollama pull mistral
ollama pull llama2
ollama pull neural-chat
```

**Usage:**

```bash
python mistral_shell_eval.py
```

Edit `MODEL_NAME` in the script to test different models:

```python
MODEL_NAME = "mistral:7b"  # Change this
```

---

## Test Cases

The suite evaluates the Sovereign Shell against **50 test cases** in `sovereign-agent-architecture/data/test_cases.csv`:

- **31 violation cases** (V-*): scenarios that should trigger principle violations
- **20 compliant cases** (C-*): scenarios that should pass validation
- **1 edge case** (V-edge-01): boundary case testing false positives

### Principles Tested

- **S1** — Virtue as Core (genuine human flourishing vs. proxy metrics)
- **S2** — Law of Integrity (deception detection)
- **S3** — Right Process (fair procedures and due process)
- **S4** — Optimal Inclusion (multi-stakeholder consideration)
- **S5** — Just Cause (justified, proportional, reversible actions)
- **S6** — Consistency Over Time (longitudinal coherence)
- **S7** — Responsibility of Design (system safeguards)

All test cases are grounded in realistic healthcare scenarios (patient intake, triage, appointments, records).

---

## Output

Results are organized in directory structure: `{output}/{run_id}/{model_name}_{timestamp}/`

Each run generates four files:

**`shell.csv`** — Results with Sovereign Shell system prompt
- `id` — Test case ID
- `expected` — Expected violation status (True/False)
- `predicted` — Predicted violation status
- `confidence` — Confidence score (0.0–1.0)
- `principle` — Primary Sovereign Principle violated (or null if compliant)
- `explanation` — Reasoning from the LLM
- `source` — Query source (shell, plain, or fallback)

**`plain.csv`** — Baseline results without constitutional system prompt

**`report.md`** — Side-by-side comparison of Plain LLM vs Sovereign Shell: per-case verdicts, the metrics table, fallback counts, and the shell false-negative/false-positive breakdown (same content as the console summary).

**`verbose.log`** — Full log of every LLM call (input messages + raw model output), tagged by case ID (e.g. `[LLM CALL: shell | V-S1-01]`). Always written regardless of the `--verbose` console flag; use it to analyze raw model behavior and diagnose JSON parsing issues.

### Example Output Structure

```
results/
├── claude_test/
│   ├── bedrock.claude-opus-4-8_20260622_101321/
│   │   ├── shell.csv
│   │   ├── plain.csv
│   │   ├── report.md
│   │   └── verbose.log
│   └── bedrock.claude-opus-4-8_20260622_104500/
│       ├── shell.csv
│       ├── plain.csv
│       ├── report.md
│       └── verbose.log
└── mistral_test/
    └── mistral-7b_20260622_150200/
        ├── shell.csv
        ├── plain.csv
        ├── report.md
        └── verbose.log
```

### Metrics Report

Each run prints:

- **True Positives / False Positives / False Negatives / True Negatives**
- **Precision, Recall, F1, Accuracy**
- **Fallback parsing counts** (indicates JSON extraction issues)
- **Detailed failures** (false negatives and false positives)

---

## Example Workflows

### Compare Multiple Models

```bash
SCRIPTS=sovereign-agent-architecture/scripts

# Test Ollama local model
python $SCRIPTS/custom_api_eval.py \
  --base-url http://localhost:11434/v1 \
  --model mistral:7b \
  --api-key ollama \
  --run-id mistral_test

# Test LM Studio local model
python $SCRIPTS/custom_api_eval.py \
  --base-url http://localhost:1234/v1 \
  --model my-local-model \
  --api-key lm-studio \
  --run-id lmstudio_test

# Test Claude via API
python $SCRIPTS/comparison-test-script.py \
  --provider anthropic \
  --model claude-3-5-sonnet-20241022
```

Then compare results across the CSV files under each `run_id`.

### Using .env for CI/CD

```bash
# sovereign-agent-architecture/.env
SOVEREIGN_BASE_URL=http://localhost:11434/v1
SOVEREIGN_MODEL=mistral:7b
SOVEREIGN_API_KEY=ollama
SOVEREIGN_RUN_ID=ci

# In CI/CD pipeline (auto-detects the .env above)
python sovereign-agent-architecture/scripts/custom_api_eval.py
```

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'openai'"

```bash
pip install -r sovereign-agent-architecture/requirements.txt
```

### "No .env file found. Using environment variables or CLI args."

Either:
1. Create a `.env` file at `sovereign-agent-architecture/.env` (auto-detected from the script's directory, the current directory, and their parents)
2. Pass `--base-url`, `--model`, `--api-key` directly
3. Set env vars: `SOVEREIGN_BASE_URL`, `SOVEREIGN_MODEL`, `SOVEREIGN_API_KEY`

### "Error on test case: Connection refused"

Check that your API endpoint is running:
- **Ollama:** `ollama serve` running on `localhost:11434`
- **LM Studio:** server running on `localhost:1234`
- **Custom API:** endpoint accessible at the configured base URL

### "confidence": 0.5 with "source": "fallback"

The LLM response couldn't be parsed as JSON. This usually means:
1. The model returned non-JSON text
2. Markdown code blocks weren't properly stripped
3. The response was truncated (increase `max_tokens`)

Inspect `verbose.log` in the run folder (or pass `--verbose` to also stream it to the console) to see the raw model output and diagnose parsing issues.

---

## Development

To add a new model provider or modify evaluation logic:

1. **Reuse core functions** from any script:
   - `extract_json()` — Robust JSON parsing
   - `query_shell()` / `query_plain()` — Standard evaluation queries
   - `calculate_metrics()` — Metrics computation

2. **Modify prompts** by editing `SOVEREIGN_SHELL_PROMPT` or `PLAIN_PROMPT`

3. **Add custom preprocessing** in `_format_result()` or `_keyword_fallback()`
</content>
