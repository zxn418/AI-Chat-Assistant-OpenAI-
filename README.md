# BFIM Care Developer Assistant AI

A Streamlit chat app that uses the OpenAI API to help developers ask coding questions, get code fixed, and generate images from text prompts — all from one page.

## Features

- **Chat assistant** — ask questions about your code or how to fix it, powered by an OpenAI chat model.
- **Image generation** — describe an image in text and generate it via the OpenAI Images API.
- **Vision input** — send an image along with a prompt and get a text response describing/analyzing it.
- Simple, single-page Streamlit UI.

> **Note:** `main.py` currently ships with the chat/image UI logic commented out as a starting scaffold. Uncomment the relevant sections in `main.py` (or wire them into `ui.py`) to enable the interactive chat and image-generation UI end to end.

## Project Structure

| File | Purpose |
|---|---|
| `main.py` | Streamlit entry point — page config, title, and (currently commented-out) chat/image UI wiring |
| `ai.py` | `OpenAIClient` wrapper — chat completions (`query`), image generation (`generate_image`), and vision (`generate_response_from_image`) |
| `setting.py` | Loads configuration/environment variables (e.g. `OPENAI_API_KEY`) via `python-dotenv` |
| `ui.py` | UI helper components |
| `image.py` | Image handling helpers |
| `pyproject.toml` / `uv.lock` | Project metadata and locked dependencies (managed with [uv](https://docs.astral.sh/uv/)) |

## Requirements

- Python **3.14+**
- An [OpenAI API key](https://platform.openai.com/api-keys)
- [uv](https://docs.astral.sh/uv/) (recommended) or `pip`

### Dependencies

- `streamlit`
- `openai`
- `litellm`
- `python-dotenv`
- `requests`

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/zxn418/AI-Chat-Assistant-OpenAI-.git
   cd AI-Chat-Assistant-OpenAI-
   ```

2. **Install dependencies**

   Using `uv` (uses the included `uv.lock`):

   ```bash
   uv sync
   ```

   Or with `pip`:

   ```bash
   pip install -r <(uv export --no-hashes 2>/dev/null) 2>/dev/null || pip install streamlit openai litellm python-dotenv requests
   ```

3. **Configure your API key**

   Create a `.env` file in the project root:

   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## Usage

Run the Streamlit app:

```bash
uv run streamlit run main.py
```

or, without `uv`:

```bash
streamlit run main.py
```

Then open the local URL Streamlit prints (typically `http://localhost:8501`) in your browser.

## How It Works

- `setting.py` reads `OPENAI_API_KEY` from your environment (loaded from `.env`).
- `ai.py` instantiates a single `OpenAIClient` (exported as `client`) used across the app to:
  - `query(prompt)` — send chat history to an OpenAI chat model and return the response text.
  - `generate_image(prompt)` — generate an image from a text prompt and return base64-encoded image data.
  - `generate_response_from_image(image_data_url, prompt)` — send an image + prompt to a vision-capable model and return a text response.
- `main.py` sets up the Streamlit page and (once uncommented) renders the chat history, takes user input, calls `client.query`, and displays results — plus a text box for image generation via `client.generate_image`.

## Configuration Notes

- Models are currently hardcoded in `ai.py` — update the `model=` values there if you want to switch to different OpenAI models.
- Never commit your `.env` file or API key to version control.

## License

No license has been specified for this repository. Add a `LICENSE` file if you intend to open-source this project.
