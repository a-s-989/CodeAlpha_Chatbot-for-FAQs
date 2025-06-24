
# Chatbot for FAQs 

## 👤 Developer
**Abhishek Singh**  
B.Tech CSE, OP Jindal University  
Intern at **Code Alpha**  

## 📌 Project Overview
This project is a chatbot system designed to answer Frequently Asked Questions (FAQs) related to a product or topic using two approaches:
1. Static Matching using NLP techniques and cosine similarity.
2. Dynamic Answering using Google's Gemini API for more natural responses when static match fails.

## 🔧 Features
- Collects and preprocesses FAQ data using NLTK
- Matches user queries using cosine similarity
- Switches to Gemini API if no close FAQ match is found
- Web-based chatbot interface using Flask and HTML

## 🛠 Tech Stack
- Python
- Flask
- NLTK
- scikit-learn
- Google Generative AI (Gemini)
- HTML/CSS (for UI)

## 🚀 How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/chatbot-faqs-websearch.git
cd chatbot-faqs-websearch
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set your Gemini API Key
Create a `.env` file in the root directory and add:
```
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

### 4. Run the App
```bash
python app.py
```
Then open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## 📄 Folder Structure
```
chatbot-faqs-websearch/
│
├── app.py                  # Main Flask app
├── gemini_api.py           # Gemini API logic
├── matcher.py              # Static FAQ matcher (cosine similarity)
├── templates/
│   └── index.html          # UI template
├── .env                    # API key (not included in repo)
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## 📌 Note
- Make sure you have valid access to the Gemini API (Google Vertex AI)
- If you hit the free-tier quota, you can switch to a lighter Gemini model or wait 24h
