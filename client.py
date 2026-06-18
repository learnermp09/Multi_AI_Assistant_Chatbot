import requests
import streamlit as st

# --------------------------------------------------
# Streamlit Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="Multi AI Assistant",
    page_icon="🤖",
    layout="centered"
)

# --------------------------------------------------
# API Endpoints
# --------------------------------------------------
BASE_URL = "http://127.0.0.1:8000"

GROQ_ENDPOINT = f"{BASE_URL}/chatgroq/invoke"
OPENAI_ENDPOINT = f"{BASE_URL}/chatopenai/invoke"
GEMINI_ENDPOINT = f"{BASE_URL}/chatgeminiai/invoke"


# --------------------------------------------------
# API Helper Function
# --------------------------------------------------
def get_response(endpoint: str, question: str):
    response = requests.post(
        endpoint,
        json={"input": {"question": question}}
    )

    response.raise_for_status()

    data = response.json()

    return data.get("output", data)


# --------------------------------------------------
# Streamlit UI
# --------------------------------------------------
st.title("🤖 Multi AI Assistant")

st.markdown(
    "Compare responses from **Groq**, **Gemini**, and **OpenAI** using a single interface."
)

# --------------------------------------------------
# Groq Assistant
# --------------------------------------------------

st.image(
    "https://cdn.sanity.io/images/chol0sk5/production/ce0b2266373b3c9722b0bccb9a98441c26c89696-1200x630.png",
    width=120
)

st.subheader("Groq LLM")

groq_question = st.text_input(
    "Enter your question for Groq:",
    key="groq_input"
)

if groq_question:
    with st.spinner("Generating response..."):
        st.write(
            get_response(
                GROQ_ENDPOINT,
                groq_question
            )
        )

# --------------------------------------------------
# Gemini Assistant
# --------------------------------------------------

st.image(
    "https://cdn.beebom.com/content/2025/07/google-gemini-new-rainbow-colours-1120w630h.webp",
    width=120
)

st.subheader("Google Gemini")

gemini_question = st.text_input(
    "Enter your question for Gemini:",
    key="gemini_input"
)

if gemini_question:
    with st.spinner("Generating response..."):
        st.write(
            get_response(
                GEMINI_ENDPOINT,
                gemini_question
            )
        )

# --------------------------------------------------
# OpenAI Assistant
# --------------------------------------------------

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/4/4d/OpenAI_Logo.svg",
    width=120
)

st.subheader("OpenAI")

st.error(
    "⚠️ OpenAI endpoint is currently unavailable because API credits have been exhausted."
)

openai_question = st.text_input(
    "Enter your question for OpenAI:",
    key="openai_input"
)

if openai_question:
    with st.spinner("Generating response..."):
        st.write(
            get_response(
                OPENAI_ENDPOINT,
                openai_question
            )
        )