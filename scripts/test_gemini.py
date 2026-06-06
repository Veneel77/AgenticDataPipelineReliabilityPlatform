from services.gemini_service import GeminiService

service = GeminiService()

response = service.generate_response(
    """
    Explain ETL pipeline failures
    in 3 bullet points.
    """
)

print(response)