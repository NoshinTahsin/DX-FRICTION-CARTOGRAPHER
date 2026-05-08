# DX Friction Cartographer

A full-stack course project scaffold for mapping developer interview transcripts into the DX landscape.

## Architecture

- Python FastAPI backend with a 3-stage OpenAI pipeline
- React frontend with interactive dimension cards and tables
- Single source of truth for DX dimensions in `config/dimensions.py`
- Export support planned for JSON, Markdown, and PDF

## Project structure

- `config/`: central DX dimension dictionary and package config
- `pipeline/`: AI prompt builder and pipeline stage stubs
- `api/`: FastAPI server and data models
- `frontend/`: React UI scaffolding
- `tests/`: sample transcript and test entrypoint

## Notes

- OpenAI API key should be stored in `.env` as `OPENAI_API_KEY`
- Optional sharing control: set `APP_ACCESS_CODE` to require a private access code for analysis
- Do not hardcode dimension names outside `config/dimensions.py`
- `.gitignore` excludes `.env`, `.venv/`, and common generated files

## License

Copyright (c) 2026 Noshin Tahsin. All rights reserved.
No permission is granted to use, copy, modify, or distribute this software without prior written consent.

This repository is public for viewing only and is not licensed for reuse.
