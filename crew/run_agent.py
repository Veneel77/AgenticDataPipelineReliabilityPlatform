from crewai import Crew

from agents.log_analysis_agent import (
    log_analysis_agent
)

from crew.log_analysis_task import (
    create_log_analysis_task
)

from tools.log_reader import (
    read_log
)

log_content = read_log(
    "logs/schema_failure.log"
)

task = create_log_analysis_task(
    log_content,
    log_analysis_agent
)

crew = Crew(
    agents=[
        log_analysis_agent
    ],

    tasks=[
        task
    ],

    verbose=True
)

result = crew.kickoff()

print(result)