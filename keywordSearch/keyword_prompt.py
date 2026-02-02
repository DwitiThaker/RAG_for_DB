# from langchain_core.prompts import ChatPromptTemplate
# from utils.timing import log_time
# import logging

# logger = logging.getLogger("keyword_prompt")
# logger.setLevel(logging.INFO)


# CHAT_TEMPLATE = """
# You are an intelligent assistant. Answer the question using the provided context only.

# User Context:
# {user_context}

# Conversation History:
# {chat_history}

# Relevant Keywords:
# {keywords}

# Context:
# {context}

# Question:
# {question}

# Answer:
# """
# @log_time("prompt...")
# def build_prompt(
#     context_chunks: list[str],
#     question: str,
#     keywords: list[str],
#     user_context: str = "",
#     chat_history: str = "",
# ):
#     context = "\n\n".join(context_chunks)

#     prompt = ChatPromptTemplate.from_template(CHAT_TEMPLATE)

#     logger.info("Extracted keywords: %s", keywords)

#     return prompt.format(
#         context=context,
#         question=question,
#         user_context=user_context,
#         chat_history=chat_history,
#         keywords=", ".join(keywords),
#     )
