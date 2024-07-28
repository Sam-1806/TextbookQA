from rank_bm25 import BM25Okapi
from nltk.tokenize import word_tokenize

def bm25_retrieval(index, query):
    corpus = [' '.join(section) for chapter in index.values() for section in chapter.values()]
    tokenized_corpus = [word_tokenize(doc.lower()) for doc in corpus]
    bm25 = BM25Okapi(tokenized_corpus)
    tokenized_query = word_tokenize(query.lower())
    return bm25.get_top_n(tokenized_query, corpus, n=3)
