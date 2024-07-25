from sentence_transformers import SentenceTransformer, util
import torch
import numpy as np
import json

with open('processed_paragraphs.json', 'r') as f: #Get the paragraphs from the file
    paragraphs = json.load(f)


model_name = "nq-distilbert-base-v1"
bi_encoder = SentenceTransformer(model_name)
top_k=5

query = "Who/What is susie?" #This should be user input
query_embed = bi_encoder.encode(query, convert_to_tensor=True)

embeddings = np.load('paragraph-embeddings.pt', allow_pickle=True)
device = util.get_device_name()
embeddings = embeddings.to(device)

similarity_scores = bi_encoder.similarity(query_embed, embeddings)[0]
scores, indices = torch.topk(similarity_scores, k=top_k)

context = "\n".join(paragraphs[i] for i in indices)