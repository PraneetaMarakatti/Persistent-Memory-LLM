from app.memory_store import MemoryStore
from app.fact_extractor import extract_facts
from app.responder import respond
from app.filters import valid_fact
import warnings
warnings.filterwarnings("ignore")

import os

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"
os.environ["TOKENIZERS_PARALLELISM"] = "false"
os.environ["TORCH_CPP_LOG_LEVEL"] = "ERROR"



def chat():

    memory_store = MemoryStore()

    print("\nHello!, I'm your AI Assistant")

    while True:

        user_input = input("You : ")

        if user_input.lower() == "exit":

            break

        # -------- Extract facts --------

        facts = extract_facts(user_input)

        for fact in facts:

            memory_store.add_memory(fact)

            print("Stored:", fact)

        # -------- Search DB --------

        memories = memory_store.search(
            user_input
        )

        # -------- Response --------

        answer = respond(
            user_input,
            memories
        )

        print("AI:", answer)


if __name__ == "__main__":

    chat()

