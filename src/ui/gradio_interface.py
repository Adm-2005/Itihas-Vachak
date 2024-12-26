import gradio as gr
from src.rag.response_generator import ResponseGenerator
from src.rag.multi_doc_retriever import MultiDocRetriever

db_path = "data/db.sqlite"
retriever = MultiDocRetriever(db_path=db_path, top_k=5)
generator = ResponseGenerator(model_name="gpt2")

def handle_query(query: str, history: list):
    retrieved_context = retriever.search(query)
    response = generator.generate_response(query, retrieved_context)
    
    return response

interface = gr.ChatInterface(
    fn=handle_query,
    type="messages",
    title="Itihas Vachak",
    theme=gr.themes.Soft()
)