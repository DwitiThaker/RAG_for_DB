from rag.qa_service import answer_question

if __name__ == "__main__":
    question = input("Ask a question: ")

    result = answer_question(question)

    print("\n Answer:\n")
    print(result["answer"])

    print(f"\n⏱ Time taken: {result['time_taken']} seconds")
    print("\n----------------------------------------------\n")

    print("Retrieved chunks:\n")
    # for i, c in enumerate(result["chunks"]):
    #     print(f"--- Chunk {i+1} (score={c['score']:.4f}) ---")
    #     print(c["text"][:500])
