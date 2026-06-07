import json
import uuid
from pathlib import Path
from datetime import datetime


INCIDENT_DIR = Path("incidents")

INCIDENT_DIR.mkdir(
    exist_ok=True
)


def save_incident(
    report_text: str
):

    incident_id = (
        f"INC-{uuid.uuid4().hex[:8]}"
    )

    incident_data = {
        "incident_id": incident_id,
        "created_at": datetime.utcnow().isoformat(),
        "report": report_text
    }

    file_path = (
        INCIDENT_DIR /
        f"{incident_id}.json"
    )

    with open(
        file_path,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            incident_data,
            f,
            indent=4
        )

    return incident_id