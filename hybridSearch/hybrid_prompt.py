from langchain_core.prompts import ChatPromptTemplate


SYSTEM_PROMPT = """You are a knowledgeable and precise assistant.

You must answer the question using ONLY the provided context.
Do not use outside knowledge.
Do not guess or hallucinate.

If the answer cannot be found in the context, say:
"The provided context does not contain enough information to answer this question."
"""


USER_PROMPT = """
You are given a set of retrieved context passages from a knowledge base.

Each passage may come from keyword search, semantic search, or both.
Some passages may be partially relevant.

Your job:
- Read the context carefully
- Answer the question using only the information present
- Be concise, factual, and clear

---------------------------
CONTEXT:
{context}
---------------------------

QUESTION:
{question}

ANSWER:
"""


def build_final_prompt(context: str, question: str):
    """
    Builds the final RAG prompt for the LLM
    """
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", SYSTEM_PROMPT),
            ("user", USER_PROMPT),
        ]
    )

    return prompt.format(
        context=context,
        question=question,
    )
