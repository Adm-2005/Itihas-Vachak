import os
import faiss
import sqlite3
import numpy as np
from sentence_transformers import SentenceTransformer

class EmbeddingsIndexer:
    def __init__(self, model_name = 'all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        self.index = None
        self.embeddings = []
        self.texts = []

    def create_index(self):
        self.index = faiss.IndexFlatL2(768)

    def add_embeddings(self, texts):
        embeddings = self.model.encode(texts)
        self.embeddings.extend(embeddings)
        self.texts.extend(texts)

        embeddings = np.array(embeddings).astype('float32')
        self.index.add(embeddings)

    def save_index(self, index_path = 'data/index.faiss', db = 'data/db.sqlite'):
        faiss.write_index(self.index, index_path)

        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS texts (id INTEGER PRIMARY KEY, text TEXT)''')
        
        for text in self.texts:
            cursor.execute('INSERT INTO texts (text) VALUES (?)', (text,))
        
        conn.commit()
        conn.close()

    def load_index(self, index_path='data/index.faiss', db='data/db.sqlite'):
        self.index = faiss.read_index(index_path)

        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        cursor.execute('SELECT text FROM texts')
        self.texts = [row[0] for row in cursor.fetchall()]
        conn.close()

    def search(self, query, top_k=5):
        query_embedding = self.model.encode([query])
        query_embedding = np.array(query_embedding).astype('float32')

        distances, indices = self.index.search(query_embedding, top_k)

        results = []
        for idx in indices[0]:
            if idx != -1:
                results.append(self.texts[idx])
        
        return results