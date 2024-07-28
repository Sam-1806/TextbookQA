import streamlit as st
from extract import extract_text_from_pdf
from index import create_hierarchical_index
from retrieve import bm25_retrieval
from rag import generate_answer_rag

# Load data
@st.cache_data
def load_textbook():
    return extract_text_from_pdf('path/to/textbook.pdf')

# Create index
@st.cache_data
def load_index(text):
    return create_hierarchical_index(text)

textbook_text = load_textbook()
index = load_index(textbook_text)

st.title("Textbook Question Answering System")

query = st.text_input("Enter your question:")

if query:
    # Retrieve relevant sections
    top_sections = bm25_retrieval(index, query)
    
    # Generate answer with RAG
    answer = generate_answer_rag(query, top_sections)
    
    # Display results
    st.subheader("Answer:")
    st.write(answer)
    
    st.subheader("Relevant Sections:")
    for section in top_sections:
        st.write(section)
