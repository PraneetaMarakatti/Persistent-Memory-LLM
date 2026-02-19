from app.llm import generate


from app.llm import generate


def extract_facts(user_input):

    prompt = f"""

Extract ONLY personal facts about the USER.

Allowed facts:

- name
- preferences
- allergies
- profession
- hobbies
- nationality
- projects
etc..

Return ONLY short factual sentences.



If NO facts exist return ONLY:

NONE

Message:

{user_input}

Facts:
"""

    output = generate(prompt)

    if not output:

        print("LLM extraction failed")

        return []

    facts = []

    for line in output.split("\n"):

        clean = line.replace("*", "").replace("-", "").strip()

        # Skip NONE or garbage
        if (
            clean
            and clean.lower() != "none"
            and "sorry" not in clean.lower()
            and "ai" not in clean.lower()
            and "cannot" not in clean.lower()
        ):

            facts.append(clean)

    print("Extracted facts:", facts)

    return facts

