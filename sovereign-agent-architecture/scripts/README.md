# Sovereign Shell Test Suite

Evaluation scripts for validating the Sovereign Agent Architecture's compliance detection across different LLM backends.

## Installation

```bash
pip install -r requirements.txt
```

## Test Scripts

### 1. `custom_api_eval.py` — Universal OpenAI-Compatible API

Supports any OpenAI-compatible API (local or cloud) with flexible configuration via CLI args or `.env` files.

**Usage:**

```bash
# Using .env file (auto-detected from current or parent directories)
python custom_api_eval.py --model mistral:7b

# Using explicit .env file
python custom_api_eval.py --env-file /path/to/.env --model mistral:7b

# Using CLI arguments
python custom_api_eval.py \
  --base-url http://localhost:11434/v1 \
  --model mistral:7b \
  --api-key ollama \
  --output eval_mistral

# CLI args override .env values
python custom_api_eval.py \
  --base-url http://localhost:1234/v1 \
  --model llama2 \
  --output eval_llama
```

**.env file format:**

```env
SOVEREIGN_BASE_URL=http://localhost:11434/v1
SOVEREIGN_MODEL=mistral:7b
SOVEREIGN_API_KEY=ollama
SOVEREIGN_CSV_PATH=../data/test_cases.csv
SOVEREIGN_OUTPUT_PREFIX=../results
SOVEREIGN_DELAY_SECONDS=0.5
```

**Options:**

- `--env-file PATH` — Path to .env file (auto-detected if omitted)
- `--base-url URL` — Base URL for OpenAI-compatible API
- `--model NAME` — Model name/identifier
- `--api-key KEY` — API key for the service
- `--csv PATH` — Path to test cases CSV (default: `../data/test_cases.csv`)
- `--output PREFIX` — Output directory prefix (default: `../results`)
- `--delay SECONDS` — Delay between API calls (default: `0.5`)

---

### 2. `comparison-test-script.py` — Anthropic & OpenAI APIs

Tests against official Anthropic Claude and OpenAI GPT models with structured configuration.

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

The suite evaluates the Sovereign Shell against **50 test cases** in `../data/test_cases.csv`:

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

Results are organized in directory structure: `{output}/{model_name}/{timestamp}/`

Each run generates two CSV files:

**`shell.csv`** — Results with Sovereign Shell system prompt
- `id` — Test case ID
- `expected` — Expected violation status (True/False)
- `predicted` — Predicted violation status
- `confidence` — Confidence score (0.0–1.0)
- `principle` — Primary Sovereign Principle violated (or null if compliant)
- `explanation` — Reasoning from the LLM
- `source` — Query source (shell, plain, or fallback)

**`plain.csv`** — Baseline results without constitutional system prompt

### Example Output Structure

```
output/
├── mistral-7b/
│   ├── 20240615_143022/
│   │   ├── shell.csv
│   │   └── plain.csv
│   └── 20240615_145530/
│       ├── shell.csv
│       └── plain.csv
├── claude-3-5-sonnet-20241022/
│   └── 20240615_144100/
│       ├── shell.csv
│       └── plain.csv
└── gpt-4o/
    └── 20240615_150200/
        ├── shell.csv
        └── plain.csv
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
# Test Ollama local model
python custom_api_eval.py \
  --base-url http://localhost:11434/v1 \
  --model mistral:7b \
  --api-key ollama

# Test LM Studio local model
python custom_api_eval.py \
  --base-url http://localhost:1234/v1 \
  --model my-local-model \
  --api-key lm-studio

# Test Claude via API
python comparison-test-script.py \
  --provider anthropic \
  --model claude-3-5-sonnet-20241022
```

Then compare results across the three CSV files.

### Using .env for CI/CD

```bash
# .env
SOVEREIGN_BASE_URL=http://localhost:11434/v1
SOVEREIGN_MODEL=mistral:7b
SOVEREIGN_API_KEY=ollama
SOVEREIGN_CSV_PATH=../data/test_cases.csv
SOVEREIGN_OUTPUT_PREFIX=../results

# In CI/CD pipeline
python custom_api_eval.py
```

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'openai'"

```bash
pip install -r requirements.txt
```

### "No .env file found. Using environment variables or CLI args."

Either:
1. Create a `.env` file in the current or parent directory
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

---

## Development

To add a new model provider or modify evaluation logic:

1. **Reuse core functions** from any script:
   - `extract_json()` — Robust JSON parsing
   - `query_shell()` / `query_plain()` — Standard evaluation queries
   - `calculate_metrics()` — Metrics computation

2. **Modify prompts** by editing `SOVEREIGN_SHELL_PROMPT` or `PLAIN_PROMPT`

3. **Add custom preprocessing** in `_format_result()` or `_keyword_fallback()`

---

## License

MIT — See [parent repository](../../) for details.
