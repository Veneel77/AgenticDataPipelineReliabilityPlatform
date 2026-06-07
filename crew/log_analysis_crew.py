from crewai import Crew

from agents.log_analysis_agent import (
    log_analysis_agent
)

from crew.log_analysis_task import (
    log_analysis_task
)

log_analysis_crew = Crew(
    agents=[
        log_analysis_agent
    ],

    tasks=[
        log_analysis_task
    ],

    verbose=True
)