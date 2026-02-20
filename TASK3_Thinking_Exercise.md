Conversational AI assistants  make use of persistent memory to personalize the conversation. However, the memory capacity is never unlimited. AT the same time, the AI assistant needs to make intelligent decisions about what to remember, what to compress, and what to forget. This is a challenge that requires trade-offs between usefulness, efficiency, and trust.

# Approach 1 — Recency-Based Decay (Temporal Forgetting)
One strategy is recency-based decay, where memories lose importance over time. Recent interactions are assumed to be more relevant to the user’s current context.

Each stored memory is associated with a timestamp. Older memories gradually receive lower priority and may eventually be removed when storage limits are reached.

Advantages of this would be that it is Simple and Computationally inexpensive and it Works well for short-term preferences or temporary contexts.

Limitation would be that Recency alone cannot distinguish between temporary and permanent facts.

Important long-term information such as a user’s name,allergies,dietary restrictions,profession, will be forgotten over time if not referenced frequently.

# Approach 2 — Importance Scoring Using an LLM
A more intelligent method involves assigning an importance score to memories using a language model.

When new information appears, the AI evaluates questions such as:

Is this a stable personal fact?

Does it affect safety or personalization?

Will future conversations benefit from remembering it?

Advantages

Context-aware decision making.

Highly personalized memory storage.

Prevents storing irrelevant conversational noise.

Limitations

The primary drawback is cost and complexity.

LLM calls consume API quota or compute resources.

Models may hallucinate or misclassify importance.

Requires careful prompt engineering.

# My Approach 

I have a proposed a Retrieval-first Architecture where, first the Vector Database is checked for stored facts and then responses are generated. 

Advantages
This reduces LLM computational costs when simple facts need to be referenced.

Disadvantages 
It requires careful prompt desgin to extract facts from user queries.
