# app/responder.py

from app.llm import generate


def respond(user_input, memories):

    # --------------------------
    # CASE 1 → STORED DB MEMORIES
    # --------------------------

    if memories:

        memory_text = "\n".join(memories)

        prompt = f"""
You are a helpful assistant.

Use Known Facts ONLY if relevant.

Known Facts:

{memory_text}

User Question:

{user_input}

Answer naturally.
"""

    # --------------------------
    # CASE 2 → GENERAL KNOWLEDGE
    # --------------------------

    else:

        prompt = f"""
You are a helpful assistant.

Answer normally using general knowledge.

User Question:

{user_input}

Answer:
"""

    return generate(prompt)
