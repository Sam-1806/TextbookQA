from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration

def generate_answer_rag(query, retrieved_texts):
    tokenizer = RagTokenizer.from_pretrained("facebook/rag-sequence-base")
    retriever = RagRetriever.from_pretrained("facebook/rag-sequence-base", index_name="exact", passages=retrieved_texts)
    model = RagSequenceForGeneration.from_pretrained("facebook/rag-sequence-base", retriever=retriever)

    input_ids = tokenizer(query, return_tensors="pt").input_ids
    generated = model.generate(input_ids=input_ids, num_return_sequences=1, num_beams=5)

    return tokenizer.batch_decode(generated, skip_special_tokens=True)[0]
