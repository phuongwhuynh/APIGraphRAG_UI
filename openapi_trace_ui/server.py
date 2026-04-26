from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
import json
from pathlib import Path
from openapi_trace_ui.renderer import render_app
import os

app = FastAPI()


@app.get("/", response_class=HTMLResponse)
def home():
    # spec = generate_openapi("./example_project")   # in-memory
    json_path = Path("./example/openapi.json")
    with open(json_path, "r", encoding="utf-8") as f:
        spec = json.load(f)

    return render_app(spec)


@app.get("/_trace")
def read_trace_file(path: str):
    """Return file content for a traced file path.

    Security: only allow relative paths within the project (no .. segments).
    """
    if not path:
        raise HTTPException(status_code=400, detail="missing path")

    # disallow path traversal
    if ".." in Path(path).parts:
        raise HTTPException(status_code=400, detail="invalid path")

    # resolve relative to workspace root (project root)
    # prefer an explicit relative path like 'app/..'
    candidate = Path(path)
    if not candidate.exists():
        candidate = Path(os.getcwd()) / path

    if not candidate.exists() or not candidate.is_file():
        raise HTTPException(status_code=404, detail="file not found")

    try:
        text = candidate.read_text(encoding="utf-8")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"unable to read file: {e}")

    return JSONResponse({"file": str(candidate), "content": text})
