def valid_fact(fact: str):

    fact_lower = fact.lower().strip()

    bad_phrases = [

        "no personal",
        "does not contain",
        "no information",
        "not provided",
        "cannot",
        "i cannot",
        "i can't",
        "unable",
        "based on the provided message"
        "sorry",
        "unavailable",
        "cannot",
        "no personal",
        "i do not know"

    ]

    # block garbage LLM responses
    for bad in bad_phrases:

        if bad in fact_lower:
            return False

    # too short
    if len(fact_lower) < 6:
        return False

    return True


  
