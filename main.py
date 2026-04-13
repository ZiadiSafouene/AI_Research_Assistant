# from ai_research_assistant.src.pipeline import process_and_summarize
# import os

# INPUT_DIR = "ai_research_assistant/data/raw_papers"
# OUTPUT_DIR = "ai_research_assistant/data/summaries"

# os.makedirs(OUTPUT_DIR, exist_ok=True)

# for file in os.listdir(INPUT_DIR):
#     if file.endswith(".pdf"):
#         path = os.path.join(INPUT_DIR, file)

#         summary = process_and_summarize(path)

#         with open(os.path.join(OUTPUT_DIR, file.replace(".pdf", ".txt")), "w",encoding="utf-8") as f:
#             f.write(summary)

# print("Summarization complete.")

from ai_research_assistant.src.retrieval.qdrant.build_index_qdrant import build_qdrant_store
from ai_research_assistant.src.retrieval.query import query_vector_store
from ai_research_assistant.src.retrieval.rag import generate_answer

store = build_qdrant_store("ai_research_assistant/data/raw_papers")

query = "What are transformer architectures used for?"

results = query_vector_store(store, query)

answer = generate_answer(query, results)

print(answer)