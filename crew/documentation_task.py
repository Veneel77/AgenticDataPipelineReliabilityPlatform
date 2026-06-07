from crewai import Task


def create_documentation_task(
    root_cause_output,
    retrieved_docs,
    agent
):

    return Task(

        description=f"""
        Root Cause Investigation:

        {root_cause_output}

        Retrieved Documentation:

        {retrieved_docs}

        Summarize:

        1. Relevant Documentation
        2. Supporting Evidence
        3. Operational Guidance

        Do not recommend fixes.
        """,

        expected_output="""
        Documentation summary.
        """,

        agent=agent
    )