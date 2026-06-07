from crewai import Task


def create_log_analysis_task(
    log_content: str,
    agent
):

    return Task(

        description=f"""
        Analyze the following log.

        LOG:

        {log_content}

        Determine:

        1. Failure Category
        2. Severity
        3. Root Cause
        4. Business Impact
        5. Recommended Fix
        """,

        expected_output="""
        Structured reliability report.
        """,

        agent=agent
    )