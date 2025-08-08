# 🤖  AI Prompt Crafter – Prompt Engineering Project

## 📌 Overview
AI Prompt Crafter is an **interactive web application** for experimenting with **Prompt Engineering** using **OpenAI's GPT-4o** model.  
It allows users to fine-tune prompt parameters in real time and view dynamically generated AI responses with a sleek UI.  
The backend is powered by **Flask** and supports a **Retrieval-Augmented Generation (RAG)**-ready architecture.

---

## 🚀 Features
- 🎯 **Full Control over Prompt Parameters**
  - `temperature`
  - `top_p`
  - `frequency_penalty`
  - `presence_penalty`
  - `max_tokens`
- 📚 **RAG Ready** – Prebuilt `retriever_info()` function for integrating external knowledge sources.
- 🔐 **Secure API Handling** with `.env` and `python-dotenv`.
- 🎨 **Modern UI** with:
  - Gradient animations
  - Glass-morphism style
  - Typewriter effect for AI responses
- ⚡ **Fast Backend API** powered by **Flask**.
- 🛡 **Robust Error Handling** for:
  - `APIConnectionError`
  - `RateLimitError`
  - `OpenAIError`

---

## 🏗 Tech Stack
### **Frontend**
- HTML5
- CSS3 (Glass-morphism, gradient animations)
- JavaScript (typewriter effect, slider controls)

### **Backend**
- Python 3.x
- Flask
- OpenAI API (`chat.completions.create()` with GPT-4o)
- python-dotenv

---

## ⚙️ Installation & Setup

1️⃣ **Clone the repository**
```bash
git clone https://github.com/yourusername/ai-prompt-crafter.git
cd ai-prompt-crafter
```

2️⃣ **Install dependencies**

```
pip install -r requirements.txt
```

3️⃣ **Set up environment variables**
Create a `.env` file in the root directory and add:
```
OPENAI_API_KEY=your_api_key_here
```

4️⃣ **Run the Flask app**
```
python app.py
```

## How It Works
* User enters a prompt in the AI Prompt Crafter UI.

* Adjusts temperature, top_p, max_tokens, etc.

* Frontend sends a POST request to /rag.

* Backend augments the prompt (RAG-ready) and calls OpenAI GPT-4o.

* AI response is displayed in a typewriter animation.

---
## Thank You
---
