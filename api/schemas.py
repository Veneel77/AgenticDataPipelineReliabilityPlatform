from pydantic import BaseModel


class LogRequest(BaseModel):
    log_text: str


class IncidentResponse(BaseModel):
    incident_id: str
    report: str