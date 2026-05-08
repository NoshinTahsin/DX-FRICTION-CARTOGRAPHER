# FastAPI server entrypoint for DX Friction Cartographer
# Exposes endpoints for transcript ingestion, JSON output, and export generation
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env")

import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pipeline import run_pipeline
from api.models import AnalyzeRequest, AnalysisResult

app = FastAPI(title="DX Friction Cartographer API")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze", response_model=AnalysisResult)
async def analyze_transcript(request: AnalyzeRequest) -> AnalysisResult:
    """Analyze a developer interview transcript for DX friction."""
    try:
        # Validate API key
        if not os.getenv("ANTHROPIC_API_KEY"):
            raise HTTPException(status_code=500, detail="API key not configured")

        # Run the analysis pipeline
        result = run_pipeline(request.transcript)
        return result

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.on_event("startup")
async def startup_event():
    key = os.getenv("ANTHROPIC_API_KEY")
    print(f"API key loaded: {bool(key)}")
    print(f"Key starts with: {key[:10] if key else 'NOT FOUND'}")

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
