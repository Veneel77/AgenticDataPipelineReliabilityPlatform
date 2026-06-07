from crewai import Task


def create_fix_recommendation_task(
    root_cause_output,
    documentation_output,
    agent
):

    return Task(

        description=f"""
        Root Cause Investigation:

        {root_cause_output}

        Documentation Summary:

        {documentation_output}

        Generate:

        1. Immediate Actions
        2. Long-Term Preventive Measures
        3. Priority Level
        4. Estimated Resolution Effort

        Use the documentation as
        supporting evidence.
        """,

        expected_output="""
        Structured remediation plan.
        """,

        agent=agent
    )