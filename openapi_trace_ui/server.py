from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
import json
from pathlib import Path
from openapi_trace_ui.renderer import render_app
import os
from dotenv import load_dotenv

app = FastAPI()


# Load .env and get repo_dir
load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")
import os

REPO_DIR = os.getenv("repo_dir")
OPENAPI_SPEC_PATH = os.getenv("openapi_spec_path")
if not REPO_DIR:
    raise RuntimeError("repo_dir not set in .env")
REPO_DIR = Path(REPO_DIR).resolve()

if not OPENAPI_SPEC_PATH:
    raise RuntimeError("openapi_spec_path not set in .env")
OPENAPI_SPEC_PATH = Path(OPENAPI_SPEC_PATH).resolve()


@app.get("/", response_class=HTMLResponse)
def home():
    with open(OPENAPI_SPEC_PATH, "r", encoding="utf-8") as f:
        spec = json.load(f)

    return render_app(spec)


@app.get("/_trace")
def read_trace_file(path: str):
    """Return file content for a traced file path.

    Security: only allow access to files within the repo_dir (from .env).
    """
    if not path:
        raise HTTPException(status_code=400, detail="missing path")

    # Disallow path traversal and absolute paths
    candidate = Path(path)
    if candidate.is_absolute() or ".." in candidate.parts:
        raise HTTPException(status_code=400, detail="invalid path")

    # Only allow files inside the repo_dir
    abs_path = (REPO_DIR / candidate).resolve()
    try:
        abs_path.relative_to(REPO_DIR)
    except ValueError:
        raise HTTPException(status_code=400, detail="path outside project directory")

    if not abs_path.exists() or not abs_path.is_file():
        raise HTTPException(status_code=404, detail="file not found")

    try:
        text = abs_path.read_text(encoding="utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"unable to read file: {e}")

    return JSONResponse({"file": str(abs_path), "content": text})
