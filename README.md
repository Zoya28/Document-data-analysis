
# 📊 Document Data Analysis with LLMs

This project is a **Streamlit-based web application** that enables users to upload a CSV file and query the data using **natural language**. It leverages **LangChain agents** powered by **Groq’s LLaMA 3.1 8B** model to perform smart, context-aware analysis on your datasets.

---

## 🚀 Features

- Upload any CSV file and get instant insights
- Ask questions in plain English (e.g., _"What is the average age?"_)
- LLM-powered agent parses, analyzes, and answers your queries
- Supports advanced data exploration and summarization
- Clean and intuitive web interface built with Streamlit

---

## 🧠 Tech Stack

| Technology       | Description                                |
|------------------|--------------------------------------------|
| Python 🐍        | Core programming language                  |
| Streamlit 🧼     | Frontend UI for data upload & interaction |
| LangChain ⚙️     | Agent framework for LLM + tool orchestration |
| ChatGroq (LLaMA 3.1 8B) 🧠 | LLM backend used via Groq API      |
| Pandas 🐼         | For reading and handling CSV data         |
| dotenv 📁        | For securely loading API keys from `.env` |

---

## 📂 Project Structure

```

project/
│
├── app.py               # Main Streamlit application
├── .env                 # Stores your Groq API key (not pushed to GitHub)
├── requirements.txt     # Python dependencies
└── README.md            # You're here, cutie 😉

````

---

## 🛠️ Setup Instructions

1. **Clone this repository**
   ```bash
   git clone https://github.com/Zoya28/Document-data-analysis.git
   cd Document-data-analysis

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add your Groq API key to `.env`**

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

## 💬 Example Queries

* *"What are the different industries listed in the dataset?"*
* *"How many unique industries are present?"*
* *"Which industry has the highest revenue?"*
* *"Which industries have more than 10,000 employees?"*

---

## ❗ Notes

* This app uses `allow_dangerous_code=True` to let the agent execute Pandas code dynamically. Use with caution on sensitive data.
* Parsing errors are handled using `handle_parsing_errors=True`, but malformed queries may still fail.


