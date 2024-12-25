import gradio as gr
from src.rag.response_generator import ResponseGenerator
from src.rag.multi_doc_retriever import MultiDocRetriever

db_path = "data/db.sqlite"
retriever = MultiDocRetriever(db_path = db_path, top_k = 5)
generator = ResponseGenerator(model_name="gpt2")

def handle_query(query: str):
    retrieved_context = retriever.search(query)

    response = generator.generate_response(query, retrieved_context)
    return response

with gr.Blocks() as interface:
    gr.Markdown("### Itihas Vachak")

    query_input = gr.Textbox(label = "You", placeholder = "Most powerful empires in Indian history...")
    output_response = gr.Textbox(label = "IV", interactive = False)

    submit_button = gr.Button("Send")
    submit_button.click(fn = handle_query, inputs = query_input, outputs = output_response)