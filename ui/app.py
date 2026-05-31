import streamlit as st
import requests

st.set_page_config(
    page_title="Yuno AI Agent Platform",
    layout="wide"
)



st.sidebar.title(" Yuno AI")
st.sidebar.success("System Online")
st.sidebar.caption("Version 1.0")

menu = st.sidebar.selectbox(
    "Menu",
    [
        "Ask AI",
        "Logs",
        "Demo"
    ]
)


st.title(" Yuno AI Agent Platform")
st.caption(
    "Multi-Agent AI Platform powered by FastAPI + CrewAI + Groq"
)


if menu == "Ask AI":

    st.subheader(" Ask Multi-Agent")

    question = st.text_input(
        "Enter question",
        placeholder="Ask something..."
    )

    if st.button("Ask"):

        if question.strip() == "":
            st.warning("Please enter a question")

        else:
            try:

                with st.spinner("Generating response..."):

                    response = requests.post(
                        "http://127.0.0.1:8000/multi-agent",
                        params={
                            "query": question
                        }
                    )

                if response.status_code == 200:

                    data = response.json()

                    st.success("Answer Generated")

                    st.subheader(" Research")
                    st.write(
                        data.get(
                            "research",
                            "No research"
                        )
                    )

                    st.subheader(" Summary")
                    st.success(
                        data.get(
                            "summary",
                            "No summary"
                        )
                    )

                else:
                    st.error("Backend Error")
                    st.code(response.text)

            except Exception as e:
                st.error(
                    f"Connection Error: {e}"
                )



elif menu == "Logs":

    st.subheader(" System Logs")

    try:

        response = requests.get(
            "http://127.0.0.1:8000/logs"
        )

        if response.status_code == 200:

            data = response.json()

            st.json(
                data.get(
                    "logs",
                    []
                )
            )

        else:
            st.error("Could not load logs")

    except Exception as e:
        st.error(e)



elif menu == "Demo":

    st.subheader(" System Demo")

    try:

        response = requests.get(
            "http://127.0.0.1:8000/demo"
        )

        if response.status_code == 200:

            data = response.json()

            st.success(
                f"Status: {data['status']}"
            )

            st.write(
                f"Project: {data['project']}"
            )

            st.subheader("Features")

            for feature in data["features"]:
                st.write(
                    f" {feature}"
                )

        else:
            st.error("Demo route error")

    except Exception as e:
        st.error(e)



st.markdown("---")
st.caption(
    "Built with FastAPI • CrewAI • Groq • Streamlit"
)