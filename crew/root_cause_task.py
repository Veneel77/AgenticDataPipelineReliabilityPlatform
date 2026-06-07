from crewai import Task


def create_root_cause_task(
    log_content,
    classification_output,
    agent
):

    return Task(

        description=f"""
        Analyze the incident.

        LOG:
        {log_content}

        Classification:
        {classification_output}

        Determine:

        1. Most likely root cause
        2. Evidence
        3. Confidence Score (0-100)

        Do not recommend fixes.
        """,

        expected_output="""
        Root cause investigation report.
        """,

        agent=agent
    )