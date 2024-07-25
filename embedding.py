import json
from sentence_transformers import SentenceTransformer
import numpy as np

with open('pre_paras.json', 'r') as f:
    data = json.load(f)
    pre_paras = data["paragraphs"]

paragraphs = []
for i in range(0,len(pre_paras), 4): #Combining 4 pre-processed paragraphs into a single paragraph
    paragraphs.append("\n".join(pre_paras[i:i+4]))

model_name = "nq-distilbert-base-v1"
bi_encoder = SentenceTransformer(model_name)


corpus_embeddings = bi_encoder.encode(paragraphs, convert_to_tensor=True, show_progress_bar=True)

np.save(open("paragraph-embeddings.pt",'wb'), corpus_embeddings) #save the embeddings to a file
with open('processed_paras.json', 'w') as f:
    json.dump(f, paragraphs)
    