from fastapi import FastAPI, HTTPException

from api.schemas import (
    LogRequest,
    IncidentResponse
)

from api.services import (
    analyze_log
)

app = FastAPI(
    title="Agentic Data Pipeline Reliability Platform",
    version="1.0.0"
)


@app.get("/")
def health():

    return {
        "status": "running"
    }


@app.post(
    "/analyze",
    response_model=IncidentResponse
)
def analyze(request: LogRequest):

    try:

        result = analyze_log(
            request.log_text
        )

        return result

    except Exception as e:

        print(f"ERROR: {str(e)}")

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )