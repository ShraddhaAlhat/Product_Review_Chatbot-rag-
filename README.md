''' ''uvicorn main:app --reload --port 8001''
'''python -m streamlit run scrapper_ingestion_ui.py'''
``` all the best```

# Flipkart Product Review Chatbot (RAG)

**A Retrieval-Augmented Generation (RAG) based chatbot that answers product-related customer queries using real Flipkart product reviews to help users make confident purchase decisions.**

## 🚀 Features
✅ Uses **RAG architecture** for accurate, context-backed answers

✅ Scrapes product reviews using **BeautifulSoup + undetected-chromedriver**

✅ Stores and retrieves data using **AstraDB**

✅ Uses **LangChain (Groq / Google GenAI)** for high-quality generation

✅ **FastAPI backend** for scalable APIs

✅ **Streamlit interface** for ingestion and testing

✅ **Dockerized & deployable on AWS ECS and App Runner**

✅ Clean environment management using **.env**

## ⚡ Installation
#### 1️⃣ Clone the repository:

```bash
git clone https://github.com/ShraddhaAlhat/Product_Review_Chatbot-rag-.git
cd Product_Review_Chatbot-rag
```

#### 2️⃣ Create & activate a virtual environment:
```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate   # Mac/Linux
```


#### 3️⃣ Install dependencies:
```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure environment variables:
```bash
ASTRA_DB_API_ENDPOINT="your_astra_db_api_endpoint"
ASTRA_DB_APPLICATION_TOKEN="your_astra_db_token"
ASTRA_DB_KEYSPACE="your_astra_db_keyspace"
GOOGLE_API_KEY="your_google_genai_key"
GROQ_API_KEY="your_groq_api_key"
```
## 🏃‍♀️ Running Locally

#### Run FastAPI backend:
```bash
uvicorn main:app --reload --port 8001
```
####  Run Streamlit ingestion UI:
```bash
python -m streamlit run scrapper_ingestion_ui.py
```

## 🗨️ Example Queries

“Is the camera of this phone good in low light?”

“How is the battery life of this laptop?”

“Are there heating issues during gaming?”

“How is the outdoor display quality?”

![Alt Text](image_path_or_url)


## 🤝 Contributing

Pull requests are welcome! Please open an issue for feature suggestions.
