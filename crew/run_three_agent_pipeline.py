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

from crew.failure_classification_task import (
    create_failure_task
)

from crew.root_cause_task import (
    create_root_cause_task
)

from crew.documentation_task import (
    create_documentation_task
)


log_content = read_log(
    "logs/schema_failure.log"
)

# ------------------
# Agent 1
# ------------------

classification_task = create_failure_task(
    log_content,
    failure_classifier_agent
)

classification_result = Crew(
    agents=[failure_classifier_agent],
    tasks=[classification_task],
    verbose=True
).kickoff()

# ------------------
# Agent 2
# ------------------

root_cause_task = create_root_cause_task(
    log_content,
    classification_result,
    root_cause_agent
)

root_cause_result = Crew(
    agents=[root_cause_agent],
    tasks=[root_cause_task],
    verbose=True
).kickoff()

# ------------------
# Retrieval
# ------------------

retrieved_docs = retrieve_documents(
    str(root_cause_result)
)

# ------------------
# Agent 3
# ------------------

documentation_task = (
    create_documentation_task(
        root_cause_result,
        retrieved_docs,
        documentation_agent
    )
)

documentation_result = Crew(
    agents=[documentation_agent],
    tasks=[documentation_task],
    verbose=True
).kickoff()

print("\n")
print("=" * 70)
print("DOCUMENTATION RESULT")
print("=" * 70)
print(documentation_result)