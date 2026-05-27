import streamlit as st
import requests

st.set_page_config(
    page_title="Yuno AI Agent Platform",
    layout="wide"
)

st.title(" Yuno AI Agent Platform")
st.subheader("Ask Multi-Agent")

menu = st.sidebar.selectbox(
    "Menu",
    ["Ask AI"]
)

if menu == "Ask AI":

    question = st.text_input(
        "Enter question",
        placeholder="Ask something..."
    )

    if st.button("Ask"):

        if question.strip() == "":
            st.warning("Please enter a question")

        else:
            try:
                response = requests.post(
                    "http://127.0.0.1:8000/multi-agent",
                    params={"query": question}
                )

                if response.status_code == 200:
                    data = response.json()

                    st.success("Answer Generated")
                    st.write(data)

                else:
                    st.error("Backend Error")
                    st.code(response.text)

            except Exception as e:
                st.error(f"Connection Error: {e}")