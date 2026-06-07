from tools.log_reader import read_log
from services.gemini_service import GeminiService


service = GeminiService()

log_content = read_log(
    "logs/schema_failure.log"
)

prompt = f"""
You are a Senior Data Reliability Engineer.

Analyze the following ETL failure log.

LOG:
{log_content}

Return ONLY:

1. Failure Category
2. Severity
3. Root Cause
4. Business Impact
5. Recommended Fix
"""

response = service.generate_response(
    prompt
)

print(response)