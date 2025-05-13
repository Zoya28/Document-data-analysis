import streamlit as st
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

def query_agent(query, document):
    df = pd.read_csv(document)

    # Load the HuggingFace model
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.9,
    )

    # Create the agent to query the DataFrame
    agent = create_pandas_dataframe_agent(llm, df, allow_dangerous_code=True, handle_parsing_errors=True)
    return agent.invoke(query)


# Streamlit UI
st.set_page_config(
    page_title="📊 Document Data Analysis",
    page_icon="📄",
)

st.title("📄 Document Data Analysis")
st.write(
    "Upload a CSV file and ask anything about your dataऍ"
)

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

# Query input
query = st.text_input(
    "Enter your query", placeholder="E.g., What's the average value in column X?"
)

# Submit button
if st.button("Submit") and uploaded_file is not None and query:
    with st.spinner("Thinking really hard... 🤯"):
        try:
            result = query_agent(query, uploaded_file)
            print(result)
            st.write("### 🔍 Result:")
            st.write(result.get("output", "No output found."))
        except Exception as e:
            st.error(f"Oopsie! Something went wrong: {e}")
else:
    st.info("Please upload a file and enter a query to get started!")
