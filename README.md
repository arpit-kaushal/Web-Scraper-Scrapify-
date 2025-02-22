# 🚀 Scrapify - The Ultimate Web Scraper & AI Chatbot

Scrapify is a powerful web application that allows users to **scrape text content** from any website, **summarize** the extracted text, and **chat with an AI** using advanced language models. Whether you're conducting research, analyzing content, or just curious, Scrapify has you covered!

---

## 🌟 Features
✅ **Web Scraping** - Extracts meaningful text from any webpage effortlessly.  
✅ **AI-Powered Summarization** - Generates concise and insightful summaries.  
✅ **Smart AI Chatbot** - Engage in intelligent conversations with contextual awareness.  
✅ **Model Selection** - Switch between **Gemma2 💎** and **Mixtral 🚀** for different AI experiences.  

---

## 🛠️ Technologies Used
- **Flask** - Backend framework
- **BeautifulSoup** - Web scraping
- **Groq API** - AI model integration
- **JavaScript, HTML, CSS** - Frontend development

---

## 📥 Installation

### Prerequisites
🔹 Python 3.x  
🔹 Pip  

### Setup Instructions
1️⃣ **Clone the repository:**  
   ```sh
   git clone https://github.com/your-repo/scrapify.git
   cd scrapify
   ```
2️⃣ **Install dependencies:**  
   ```sh
   pip install -r requirements.txt
   ```
3️⃣ **Run the application:**  
   ```sh
   python app.py
   ```
4️⃣ **Open in browser:**  
   ```
   http://127.0.0.1:5000/
   ```

---

## 🌍 API Endpoints

### 🏠 Home Page
**`GET /`**  
Serves the frontend UI.

### 📝 Scrape & Summarize
**`POST /scrape`**  
- **Request:**  
  ```json
  { "url": "<website_url>" }
  ```
- **Response:**  
  ```json
  {
    "scraped_text": "Extracted text from the website",
    "summary": "Summarized text output"
  }
  ```

### 💬 AI Chat
**`POST /chat`**  
- **Request:**  
  ```json
  { "message": "User's input", "context": "Scraped content summary" }
  ```
- **Response:**  
  ```json
  { "response": "AI-generated reply" }
  ```

### 🔄 Model Selection
**`POST /select_model`**  
- **Request:**  
  ```json
  { "model": "Gemma2 💎" | "Mixtral 🚀" }
  ```
- **Response:**  
  ```json
  { "message": "Model changed to <selected_model>" }
  ```

---

## 📌 How to Use
1️⃣ Enter a **URL** and click **Scrape and Summarize**.  
2️⃣ View the **extracted text** and its **summary**.  
3️⃣ Use the **chatbox** to interact with the **AI assistant**.  
4️⃣ Select a **different AI model** for a varied experience.  

---

