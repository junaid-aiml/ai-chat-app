# 🤖 AI Chat Application (Full Stack)

A full-stack AI-powered chat application that allows users to interact with an AI model in real-time. Built using FastAPI for the backend and HTML, CSS, JavaScript for the frontend. The app supports multiple chat sessions, voice input, and is fully deployed on the cloud.

---

## 🌐 Live Demo

👉 https://timely-hotteok-55a6f9.netlify.app

---

## 🧠 Features

- 💬 Real-time AI chat interaction  
- 🧾 Multiple chat sessions (create, rename, delete)  
- 🎤 Voice input using browser speech recognition  
- 🌙 Dark mode UI  
- 💾 Chat history stored using local storage  
- ⚡ Fast API-based backend integration  
- 🌐 Fully deployed (Frontend + Backend)

---

## 🏗️ Tech Stack

**Frontend:**
- HTML
- CSS
- JavaScript

**Backend:**
- Python
- FastAPI

**Deployment:**
- Netlify (Frontend)
- Render (Backend)

---

## 🔗 API Endpoint

**POST /chat**

Request:
{ "message": "Hello" }

Response:
{ "reply": "Hello! How can I assist you?" }

---

## ⚙️ Installation (Run Locally)

### 1. Clone the repository
git clone https://github.com/junaid-aiml/ai-chat-app.git⁠ cd ai-chat-app

### 2. Setup Backend
cd backend pip install -r requirements.txt

### 3. Add Environment Variable

Create a `.env` file inside backend folder:
GROQ_API_KEY=your_api_key_here

### 4. Run Backend
uvicorn main:app --reload

### 5. Open Frontend

Open this file in browser:
frontend/index.html

---

## 🚀 Deployment

- Backend deployed on Render  
- Frontend deployed on Netlify  
- Accessible globally via browser  

---

## 🧪 Key Learnings

- Full-stack development (frontend + backend)
- API integration and handling asynchronous requests
- Debugging real-world deployment issues
- Environment variable management and security
- Cloud deployment using Render and Netlify

---

## 🔮 Future Improvements

- User authentication system  
- Database integration for chat persistence  
- Chat history sync across devices  
- Streaming responses (typing effect like ChatGPT)

---

## 👨‍💻 Author

Mohammed Junaid  
GitHub: https://github.com/junaid-aiml
