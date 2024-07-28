from extract import extract_text_from_pdf
from index import create_hierarchical_index
from retrieve import bm25_retrieval
from rag import generate_answer_rag

# Extract content
textbook_text = extract_text_from_pdf('path/to/textbook.pdf')

# Create index
index = create_hierarchical_index(textbook_text)

# Query and retrieve
query = "Explain photosynthesis"
top_sections = bm25_retrieval(index, query)

# Generate answer with RAG
answer = generate_answer_rag(query, top_sections)
print("Answer:", answer)
