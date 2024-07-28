# TextbookQA

# Textbook Question Answering System

Welcome to the Textbook Question Answering System! This project extracts content from textbooks, creates a hierarchical index, and uses a Retrieval-Augmented Generation (RAG) system to answer user queries.

## Features

- **Content Extraction:** Extracts text from PDF textbooks.
- **Hierarchical Indexing:** Organizes content into chapters and sections for efficient retrieval.
- **Advanced Retrieval:** Uses BM25 for finding relevant sections.
- **RAG System:** Combines retrieval with a generative model to provide accurate answers.
- **User Interface:** Streamlit-based UI for interactive querying.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/TextbookQA.git
   cd TextbookQA

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Download models:**

Ensure you have the required models for the RAG pipeline.

3. **Usage:**

Run the Streamlit app:
   ```bash
streamlit run ui.py
```
Interact with the system:

Enter your query in the input box.
View the generated answer and relevant sections.

## Sample output: 
Question: What is overfitting in machine learning?

Answer: Overfitting occurs when a model learns the training data too well, capturing noise and irrelevant patterns. This results in poor performance on unseen data.

Source: Machine Learning by Tom M. Mitchell, Chapter 3, Section 3.2

Additional Information: Techniques like cross-validation and regularization can help mitigate overfitting.\


## How It Works

### Content Extraction
- Utilizes PyMuPDF to extract text from PDF files.

### Hierarchical Indexing
- Structures content into a tree format, capturing chapters and sections.

### Retrieval Techniques
- Uses BM25 to retrieve the most relevant sections for a given query.

### RAG System
- Employs a RAG model to generate answers based on retrieved text.
- Enhances the answer quality by combining retrieval with language generation.

## Future Enhancements
- **Query Expansion:** Implement techniques like synonym expansion.
- **Hybrid Retrieval:** Combine BM25 with dense retrieval for improved accuracy.
- **Evaluation Metrics:** Assess system performance with precision and recall.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request.

## License
This project is licensed under the MIT License.

## Acknowledgments
- [Hugging Face Transformers](https://huggingface.co/transformers/)
- [Streamlit](https://streamlit.io/)
- [PyMuPDF](https://pymupdf.readthedocs.io/)
