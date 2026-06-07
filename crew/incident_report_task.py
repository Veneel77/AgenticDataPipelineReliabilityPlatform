from crewai import Task


def create_incident_report_task(
    classification_output,
    root_cause_output,
    documentation_output,
    fix_output,
    agent
):

    return Task(

        description=f"""
        Classification:

        {classification_output}

        Root Cause:

        {root_cause_output}

        Documentation:

        {documentation_output}

        Fix Plan:

        {fix_output}

        Generate a structured incident report.

        Include:

        1. Incident Summary
        2. Severity
        3. Business Impact
        4. Root Cause
        5. Supporting Evidence
        6. Recommended Actions
        7. Incident Status
        """,

        expected_output="""
        Enterprise incident report.
        """,

        agent=agent
    )