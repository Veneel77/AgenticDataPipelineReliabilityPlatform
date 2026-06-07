from crewai import Crew

from tools.log_reader import read_log

from agents.failure_classifier_agent import (
    failure_classifier_agent
)

from agents.root_cause_agent import (
    root_cause_agent
)

from crew.failure_classification_task import (
    create_failure_task
)

from crew.root_cause_task import (
    create_root_cause_task
)


log_content = read_log(
    "logs/schema_failure.log"
)

# AGENT 1

classification_task = create_failure_task(
    log_content,
    failure_classifier_agent
)

classification_crew = Crew(
    agents=[failure_classifier_agent],
    tasks=[classification_task],
    verbose=True
)

classification_result = (
    classification_crew.kickoff()
)

print("\n")
print("=" * 60)
print("CLASSIFICATION RESULT")
print("=" * 60)
print(classification_result)

# AGENT 2

root_cause_task = create_root_cause_task(
    log_content,
    classification_result,
    root_cause_agent
)

root_cause_crew = Crew(
    agents=[root_cause_agent],
    tasks=[root_cause_task],
    verbose=True
)

root_cause_result = (
    root_cause_crew.kickoff()
)

print("\n")
print("=" * 60)
print("ROOT CAUSE RESULT")
print("=" * 60)
print(root_cause_result)