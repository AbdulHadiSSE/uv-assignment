# UV Assignment - AI Greeting Agents

**Author:** Abdul Hadi  
**PIAIC Registration:** PIAIC228505

Two AI greeting agent applications using OpenAI Agents library with Gemini 2.5 Flash model.

## Projects

### 1. Simple App
- AI greeting agent with direct execution
- Uses Gemini 2.5 Flash via OpenAI-compatible API
- Environment-based configuration

### 2. Packaged App
- Same AI agent functionality in packaged format
- Console script entry point
- Modular structure

## Setup

1. Create `.env` file in each project:
```
GEMINI_API_KEY=your_api_key_here
```

2. Install dependencies:
```bash
uv sync
```

## Running

### Simple App
```bash
cd simple-app
uv run python main.py
```

### Packaged App
```bash
cd packaged-app
uv run run_agent
```