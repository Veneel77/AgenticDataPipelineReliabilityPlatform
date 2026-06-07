import requests
import streamlit as st

st.set_page_config(
    page_title="Agentic Data Pipeline Reliability Platform",
    layout="wide"
)

st.title(
    "Agentic Data Pipeline Reliability Platform"
)

st.write(
    "Upload logs and analyze failures."
)

log_text = st.text_area(
    "Paste Pipeline Log",
    height=300
)

if st.button("Analyze Incident"):

    if not log_text:

        st.warning(
            "Please enter a log."
        )

    else:

        try:

            with st.spinner(
                "Running Multi-Agent Analysis..."
            ):

                response = requests.post(
                    "http://127.0.0.1:8000/analyze",
                    json={
                        "log_text": log_text
                    }
                )

            st.subheader(
                "Debug Information"
            )

            st.write(
                "Status Code:",
                response.status_code
            )

            if response.status_code == 200:

                result = response.json()

                st.success(
                    "Analysis Completed"
                )

                st.subheader(
                    "Incident ID"
                )

                st.write(
                    result["incident_id"]
                )

                st.subheader(
                    "Incident Report"
                )

                st.write(
                    result["report"]
                )

            else:

                try:
                    error_data = response.json()

                    st.error(
                        error_data.get(
                            "detail",
                            "Unknown Error"
                        )
                    )

                except Exception:

                    st.error(
                        response.text
                    )

        except Exception as e:

            st.error(
                f"Exception: {str(e)}"
            )