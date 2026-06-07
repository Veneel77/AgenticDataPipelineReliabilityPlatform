from crewai import Crew

from tools.log_reader import read_log
from rag.retriever import retrieve_documents

from agents.failure_classifier_agent import (
    failure_classifier_agent
)

from agents.root_cause_agent import (
    root_cause_agent
)

from agents.documentation_agent import (
    documentation_agent
)

from agents.fix_recommendation_agent import (
    fix_recommendation_agent
)

from agents.incident_report_agent import (
    incident_report_agent
)

from crew.failure_classification_task import (
    create_failure_task
)

from crew.root_cause_task import (
    create_root_cause_task
)

from crew.documentation_task import (
    create_documentation_task
)

from crew.fix_recommendation_task import (
    create_fix_recommendation_task
)

from crew.incident_report_task import (
    create_incident_report_task
)

from storage.incident_repository import (
    save_incident
)


def run_pipeline(log_content):

    # Agent 1

    classification_task = create_failure_task(
        log_content,
        failure_classifier_agent
    )

    classification_result = Crew(
        agents=[failure_classifier_agent],
        tasks=[classification_task]
    ).kickoff()

    # Agent 2

    root_cause_task = create_root_cause_task(
        log_content,
        classification_result,
        root_cause_agent
    )

    root_cause_result = Crew(
        agents=[root_cause_agent],
        tasks=[root_cause_task]
    ).kickoff()

    # Retrieval

    retrieved_docs = retrieve_documents(
        str(root_cause_result)
    )

    # Agent 3

    documentation_task = create_documentation_task(
        root_cause_result,
        retrieved_docs,
        documentation_agent
    )

    documentation_result = Crew(
        agents=[documentation_agent],
        tasks=[documentation_task]
    ).kickoff()

    # Agent 4

    fix_task = create_fix_recommendation_task(
        root_cause_result,
        documentation_result,
        fix_recommendation_agent
    )

    fix_result = Crew(
        agents=[fix_recommendation_agent],
        tasks=[fix_task]
    ).kickoff()

    # Agent 5

    incident_task = create_incident_report_task(
        classification_result,
        root_cause_result,
        documentation_result,
        fix_result,
        incident_report_agent
    )

    incident_result = Crew(
        agents=[incident_report_agent],
        tasks=[incident_task]
    ).kickoff()

    incident_id = save_incident(
        str(incident_result)
    )

    return {
        "incident_id": incident_id,
        "report": str(incident_result)
    }


if __name__ == "__main__":

    log_content = read_log(
        "logs/schema_failure.log"
    )

    result = run_pipeline(
        log_content
    )

    print(result)