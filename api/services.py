import uuid

from crew.run_full_pipeline import (
    run_pipeline
)


def analyze_log(log_text: str):

    return run_pipeline(
        log_text
    )