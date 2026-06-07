from crewai import Task


def create_failure_task(
    log_content,
    agent
):

    return Task(

        description=f"""
        Analyze the log.

        LOG:
        {log_content}

        Return ONLY:

        1. Failure Category
        2. Severity

        Do not provide fixes.
        Do not provide root causes.
        """,

        expected_output="""
        Failure category and severity.
        """,

        agent=agent
    )