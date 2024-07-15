import os
from sentence_transformers import SentenceTransformer
from pinecone.grpc import PineconeGRPC as Pinecone

#Fetching the embedding model
EMBED_MODEL = SentenceTransformer("all-MiniLM-L6-v2")
query_embed = EMBED_MODEL.encode("Where is Amon now?")

#Setting up the pinecone index
pinecone_api_key = os.environ.get('PINECONE_API_KEY')
pc = Pinecone(api_key=pinecone_api_key)
index = pc.Index("novel-index")

#Top-k vector search
top_5_result = index.query(vector=query_embed,
            top_k=5,
            include_values=False
            )

top_5_indices = sorted([int(result['id']) for result in top_5_result['matches']])
print(top_5_indices)