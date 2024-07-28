from transformers import pipeline

def generate_answer(query, context):
    qa_model = pipeline("question-answering")
    response = qa_model(question=query, context=' '.join(context))
    return response['answer']
