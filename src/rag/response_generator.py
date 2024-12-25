from transformers import pipeline

class ResponseGenerator:
    def __init__(self, model_name="gpt2"):
        self.generator = pipeline("text-generation", model = model_name)

    def generate_response(self, query, retrieved_context, max_length=500):
        context = "\n".join([f"Source: {res['source']}\n{res['text']}" for res in retrieved_context])
        
        prompt = f"Answer the question based on the following context:\n\n{context}\n\nQuestion: {query}\nAnswer:"
        
        response = self.generator(prompt, max_length=max_length, num_return_sequences=1)
        return response[0]['generated_text']