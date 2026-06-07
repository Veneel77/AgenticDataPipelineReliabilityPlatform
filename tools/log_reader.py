from pathlib import Path


def read_log(log_path: str):

    file_path = Path(log_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"{log_path} not found"
        )

    return file_path.read_text(
        encoding="utf-8"
    )