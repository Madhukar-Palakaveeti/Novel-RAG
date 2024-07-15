from langchain_community.llms import Ollama
import json
from vector_store import top_5_indices

llm = Ollama(model="tinyllama")
with open("paragraphs.json", "r") as f:
    data = json.load(f)
    paragraphs = data["paragraphs"]

context = "".join(paragraphs[i] for i in top_5_indices)
print(llm.invoke(f"""
        Please answer the query based on the given context.
        Query : Where is amon now?
        context : {context}
"""))