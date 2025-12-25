# 🤖 Shopify AI Analytics Assistant

A powerful, intelligent analytics dashboard that translates natural language questions into actionable business insights. This tool acts as a virtual data analyst for Shopify store owners, capable of understanding complex queries about sales, inventory, marketing, and customer behavior.

## 🚀 Key Features

This AI Agent has been trained to understand a wide variety of business intents, ranging from basic reporting to advanced predictive analytics.

### 📊 Core Analytics
*   **Sales Tracking**: "Show me total sales for the last 30 days"
*   **Top Products**: "What are my best selling items?"
*   **Inventory Levels**: "Check current stock counts"
*   **Geography**: "Where are my customers located?"

### 🔮 Predictive & Strategic
*   **Demand Forecasting**: "How many units of Product X will I need next month?" (Predicts future demand based on trends)
*   **Stock Risk Analysis**: "Which products are likely to go out of stock?" (Calculates 'Days Until Empty')
*   **Reorder Recommendations**: "How much inventory should I reorder?"
*   **Return Rate Analysis**: "Which products have high return rates?"

### 🧠 Advanced "Unusual" Queries
The agent goes beyond standard reports to answer niche questions:
*   **Social Media Impact**: "How is Instagram performing?"
*   **Email Marketing**: "What is my newsletter open rate?"
*   **Customer Sentiment**: "Show me recent customer reviews" or "What is my CSAT score?"
*   **Competitor Intel**: "How do I compare to competitors?"
*   **Cart Abandonment**: "What is my cart abandonment rate?"

### 🛡️ Smart Fallback
If you ask a question the agent doesn't understand (e.g., "What is the meaning of life?"), it won't hallucinate. Instead, it gracefully admits low confidence and provides a **Store Health Dashboard** summary to ensure you always get value.

---

## Output 
<img width="633" height="852" alt="image" src="https://github.com/user-attachments/assets/4bf459bb-2337-4286-884f-0cf49a9e8a64" />

---


## 🛠️ Architecture

*   **Frontend**: A modern, responsive HTML/JS interface (`demo_ui.html`) with professional styling, suggestion chips, and dynamic data tables.
*   **Backend**: A Python Microservice (`python_service/`) built with **FastAPI**.
*   **AI Logic**: A custom Rule-based Natural Language Processing (NLP) engine (`agent.py`) that:
    1.  Identifies user intent from keywords.
    2.  Generates corresponding **ShopifyQL** queries.
    3.  Fetches (mock) data simulating a Shopify API response.
    4.  Generates a human-readable explanation of the data.

---

## 💻 How to Run

### Prerequisities
*   Python 3.9+
*   Git

### 1. Setup the Python Service
Navigate to the python service directory and install dependencies:
```bash
cd python_service
pip install -r requirements.txt
```

### 2. Start the API Server
Run the FastAPI backend:
```bash
uvicorn main:app --reload --port 8000
```
You should see output indicating the server is running on `http://127.0.0.1:8000`.

### 3. Launch the Dashboard
Simply open the `demo_ui.html` file in your preferred web browser (Chrome, Edge, etc.).
No local server is needed for the HTML file itself; it communicates directly with the running Python API.

---

## 🧪 Testing the Agent

Once the UI is open, try the "Suggestion Chips" or type your own questions:

1.  **Forecasting**: "How many units of Product X will I need?"
2.  **Marketing**: "Where is my traffic coming from?"
3.  **Risk**: "What items are running out soon?"
4.  **Unknown**: "Tell me a joke" (Triggers the Fallback Dashboard)

---

## 🔮 Future Roadmap

*   **Live Shopify Integration**: Connect to real Shopify Stores via OAuth.
*   **LLM Integration**: Replace rule-based logic with OpenAI/LangChain for true "Zero-Shot" query understanding.
*   **Data Visualization**: Add charts (Bar/Line graphs) to the frontend.
