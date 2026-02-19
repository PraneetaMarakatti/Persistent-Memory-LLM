from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.memory_store import MemoryStore
from app.fact_extractor import extract_facts
from app.filters import valid_fact
from app.responder import respond

app = FastAPI(
    title="AI Memory System API"
)

memory_store = MemoryStore()


# -------------------------
# Request Model
# -------------------------

class MemoryRequest(BaseModel):
    text: str


# -------------------------
# POST /memories
# Store Memory
# -------------------------

@app.post("/memories")

def add_memory(req: MemoryRequest):

    if not req.text.strip():

        raise HTTPException(
            status_code=400,
            detail="Text required"
        )

    try:

        facts = extract_facts(req.text)

        print("Extracted facts:", facts)


        stored = []

        for fact in facts:

            if valid_fact(fact):

                memory_id = memory_store.add_memory(fact)

                stored.append({

                    "id": memory_id,
                    "fact": fact
                })

        return {

            "stored_memories": stored
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# -------------------------
# SEARCH + RESPOND
# -------------------------

@app.get("/memories/search")

def search(q: str):

    if not q.strip():

        raise HTTPException(
            status_code=400,
            detail="Query required"
        )

    try:

        # -------- DB SEARCH FIRST --------

        memories = memory_store.search(q)

        print("Retrieved Memories:", memories)


        # -------- Gemini Response --------

        answer = respond(q, memories)


        return {

            "answer": answer,

            "memories_used": memories

        }


    except Exception as e:

        raise HTTPException(

            status_code=500,

            detail=str(e)

        )

# -------------------------
# GET ALL MEMORIES
# -------------------------

@app.get("/memories")

def get_all():

    return memory_store.get_all_memories()


# -------------------------
# DELETE MEMORY
# -------------------------

@app.delete("/memories/{memory_id}")

def delete(memory_id: str):

    deleted = memory_store.delete_memory(
        memory_id
    )

    if not deleted:

        raise HTTPException(

            status_code=404,

            detail="Memory not found"
        )

    return {

        "message": "Deleted"
    }
