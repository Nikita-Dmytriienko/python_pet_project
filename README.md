# Simple Gemini AI Chat

Hey, this is my little pet project: a minimal web chat with Google's Gemini AI. You type a prompt, it answers, and everything gets saved in a local SQLite database tied to your IP. Your chat history shows up only for you when you reload the page.

Super simple — one HTML file for the frontend, FastAPI backend, and Gemini handling the heavy lifting.

## Requirements

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) for dependency and environment management (highly recommended)
- A valid Gemini API key (free tier works fine)

## General Workflow

Dependencies are managed with `uv`. If you don't have it yet:

```bash
# Install uv (one-time thing)
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Install everything and set up the virtual environment:

```bash
$ uv sync
```

Activate the venv if needed:

```bash
$ source .venv/bin/activate   # Linux/macOS
$ .venv\Scripts\activate      # Windows
```

Create a `.env` file in the project root with your Gemini key:

```env
GEMINI_API_KEY=your_actual_key_here
```

## Running the backend

Start the FastAPI server:

```bash
$ uvicorn main:app --reload
```

It will run on `http://127.0.0.1:8000`.

## Opening the frontend

Just open `index.html` in your browser. I usually use Live Server in VS Code (ports 5500/5501 — CORS is configured for those).

The page will connect to the local backend automatically.

## How it works

- Type your prompt and hit Send (or Ctrl+Enter)
- POST → `/requests` → Gemini generates the answer
- Request + response saved to `requests.db` with your IP
- GET → `/requests` loads your personal history
- History appears below the input field

CORS is locked to localhost Live Server ports only.

## Database

SQLite file: `requests.db` in the project root.  
Table `chat_requests` is created automatically on first start.

Want to clear history? Just delete `requests.db`.

## VS Code

Project is ready for VS Code out of the box:
- Pick the interpreter from `.venv/bin/python`
- Debug `main.py` directly
- Live Server for the frontend works great

## Security note

- API key lives in `.env` (ignored by git)
- Never commit `.env` or `requests.db`
- This is purely local/dev — no auth, no rate limiting. For any real deployment you'd want proper user accounts and limits.

That's it! Quick way to play with Gemini and have persistent chat history. Feel free to fork and tweak.

Enjoy! 🚀
