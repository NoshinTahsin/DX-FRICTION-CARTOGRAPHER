# FastAPI server entrypoint for DX Friction Cartographer
# Exposes endpoints for transcript ingestion, JSON output, and export generation
from pathlib import Path
from dotenv import load_dotenv
load_dotenv(dotenv_path=Path(__file__).resolve().parent.parent / ".env", override=True)

import os
from fastapi import FastAPI, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pipeline import run_pipeline
from api.models import AnalyzeRequest, AnalysisResult

app = FastAPI(title="DX Friction Cartographer API")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def validate_access_code(submitted_code: str | None) -> None:
    access_code = (os.getenv("APP_ACCESS_CODE") or "").strip()
    submitted_access_code = (submitted_code or "").strip()
    if access_code and submitted_access_code != access_code:
        raise HTTPException(status_code=401, detail="Invalid access code")


@app.post("/auth/validate")
async def validate_app_access(x_app_access_code: str | None = Header(default=None)):
    """Validate the shared app access code without running an analysis."""
    validate_access_code(x_app_access_code)
    return {"ok": True}

@app.post("/analyze", response_model=AnalysisResult)
async def analyze_transcript(
    request: Request,
    payload: AnalyzeRequest,
    x_app_access_code: str | None = Header(default=None),
) -> AnalysisResult:
    """Analyze a developer interview transcript for DX friction."""
    try:
        # Validate API key
        if not os.getenv("OPENAI_API_KEY"):
            raise HTTPException(status_code=500, detail="OpenAI API key not configured")

        validate_access_code(x_app_access_code)

        # Run the analysis pipeline
        result = run_pipeline(payload.transcript)
        return result

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

@app.on_event("startup")
async def startup_event():
    key = os.getenv("OPENAI_API_KEY")
    print(f"OpenAI API key loaded: {bool(key)}")
    print(f"OpenAI model: {os.getenv('OPENAI_MODEL', 'gpt-5.1')}")

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "access_code_required": bool((os.getenv("APP_ACCESS_CODE") or "").strip())}
