# 🤖 Multi-AI Assistant

Multi-AI Assistant is a production-ready AI application that enables users to interact with multiple state-of-the-art Large Language Models (LLMs) through a single unified interface.

The project integrates **Groq**, **Google Gemini**, and **OpenAI** models using **LangChain**, **LangServe**, **FastAPI**, and **Streamlit**, demonstrating modern AI application deployment with separate frontend and backend services.

---

## 🚀 Live Demo

**Frontend (Streamlit Cloud)**

https://your-streamlit-app.streamlit.app

**Backend API (Render)**

https://your-render-service.onrender.com

---

## 📌 Features

* Unified interface for multiple AI models
* Compare responses from Groq, Gemini, and OpenAI
* FastAPI + LangServe backend architecture
* Streamlit frontend interface
* REST API-based communication
* LangChain-powered prompt orchestration
* LangSmith tracing and observability
* Secure cloud deployment
* Environment variable-based configuration
* Responsive and intuitive user experience

---

## 🏗️ Architecture

```text
User
 │
 ▼
Streamlit Frontend
(Streamlit Community Cloud)
 │
 ▼
FastAPI + LangServe Backend
(Render)
 │
 ├── Groq (Qwen3-32B)
 ├── Google Gemini 2.5 Flash
 └── OpenAI GPT-4o
 │
 ▼
LangSmith Monitoring
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### Backend

* FastAPI
* LangServe

### LLM Framework

* LangChain

### AI Models

* Groq (Qwen/Qwen3-32B)
* Google Gemini 2.5 Flash
* OpenAI GPT-4o

### Monitoring

* LangSmith

### Deployment

* Render
* Streamlit Community Cloud

---

## 📂 Project Structure

```text
Multi_AI_Assistant/
│
├── app.py              # FastAPI + LangServe backend
├── client.py           # Streamlit frontend
├── requirements.txt    # Project dependencies
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/learnermp09/Multi_AI_Assistant.git

cd Multi_AI_Assistant
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Create a `.env` file locally:

```env
GROQ_API_KEY=your_groq_api_key

GOOGLE_API_KEY=your_google_gemini_api_key

OPENAI_API_KEY=your_openai_api_key

LANGCHAIN_API_KEY=your_langsmith_api_key

LANGCHAIN_TRACING_V2=true

LANGCHAIN_PROJECT=multi-ai-assistant
```

> Never commit your `.env` file or API keys to GitHub.

---

### 5. Run the Backend

```bash
uvicorn app:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

---

### 6. Run the Frontend

```bash
streamlit run client.py
```

Frontend URL:

```text
http://localhost:8501
```

---

## 🌐 API Endpoints

### Groq

```http
POST /chatgroq/invoke
```

### Google Gemini

```http
POST /chatgeminiai/invoke
```

### OpenAI

```http
POST /chatopenai/invoke
```

---

## 🔐 Deployment

### Backend Deployment (Render)

The FastAPI + LangServe backend is deployed on Render.

Environment variables are securely stored using Render Environment Variables.

Required Render Environment Variables:

```env
GROQ_API_KEY

GOOGLE_API_KEY

OPENAI_API_KEY

LANGCHAIN_API_KEY

LANGCHAIN_TRACING_V2=true

LANGCHAIN_PROJECT=multi-ai-assistant
```

### Frontend Deployment (Streamlit Community Cloud)

The Streamlit frontend is deployed independently on Streamlit Community Cloud.

The frontend communicates with the Render-hosted backend through REST API calls.

Required Streamlit Secrets:

```toml
BACKEND_URL="https://your-render-service.onrender.com"
```

### Security

* No API keys stored in source code
* Environment-variable-based configuration
* GitHub Push Protection enabled
* Secure cloud deployment practices
* LangSmith observability enabled

---

## 🧠 How It Works

1. User enters a question through the Streamlit interface.
2. Streamlit sends the request to the Render-hosted FastAPI backend.
3. LangServe routes the request to the selected model endpoint.
4. LangChain formats the prompt.
5. The selected LLM generates a response.
6. FastAPI returns the response to Streamlit.
7. Streamlit displays the answer to the user.
8. LangSmith captures traces for monitoring and debugging.

---

## 📸 Application Preview

<img width="3810" height="1872" alt="image" src="https://github.com/user-attachments/assets/9e9c3065-f9fd-43c2-8250-4f0ea4f9c9b6" />

---

## 🎯 Future Enhancements

* Conversation memory
* Chat history support
* Streaming responses
* Retrieval-Augmented Generation (RAG)
* PDF Question Answering
* Document Chat
* Multi-Agent Workflows
* Authentication and User Accounts
* Docker Deployment
* Kubernetes Deployment
* Usage Analytics Dashboard

---

## 👨‍💻 Author

**Mrityunjay Pathak**

GitHub:
https://github.com/learnermp09

LinkedIn:
https://www.linkedin.com/in/mrityunjay-pathak-74151aa/

---

## 📜 License

This project is licensed under the MIT License.

