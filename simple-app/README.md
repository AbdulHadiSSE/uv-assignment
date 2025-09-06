# AI Greeting Agent - Simple App

**Author:** Abdul Hadi  
**PIAIC Registration:** PIAIC228505

AI greeting agent using OpenAI Agents library with Gemini 2.5 Flash model.

## App Output

![App Output](screenshot.jpg)

## Features

- Interactive AI greeting agent
- Gemini 2.5 Flash model integration
- Environment-based API key configuration
- UV package management

## Setup

1. Create `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

2. Install dependencies:

```bash
uv sync
```

3. Run:

```bash
uv run python main.py
```

## Dependencies

- openai-agents>=0.2.11
- python-dotenv
