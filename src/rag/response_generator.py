from transformers import pipeline

class ResponseGenerator:
    def __init__(self, model_name="gpt2"):
        self.generator = pipeline("text-generation", model=model_name)

    def generate_response(self, query, retrieved_context, max_length=200):
        print(retrieved_context)
        context = "\n".join([f"Source: {res['source']}\n{res['text']}" for res in retrieved_context])

        prompt = f"Answer the question based on the following context:\n\n{context}\n\nQuestion: {query}\nAnswer:"
    
        response = self.generator(prompt, max_length=max_length, num_return_sequences=1)
        generated_text = response[0]['generated_text']
 
        if "Answer:" in generated_text:
            generated_text = generated_text.split("Answer:")[1].strip()
        else:
            generated_text = generated_text.strip()  
        
        # print("Generated Response:", generated_text)

        return generated_text