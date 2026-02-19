import chromadb

from sentence_transformers import SentenceTransformer
import uuid


class MemoryStore:

    def __init__(self):

        print("Loading embedding model...")

        self.embedder = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        # database folder
        self.client = chromadb.PersistentClient(

         path="chroma_db"
         )


        self.collection = self.client.get_or_create_collection(
            name="memories"
        )


    def add_memory(self, fact):
        print("ADDING MEMORY:", fact)

        memory_id = str(uuid.uuid4())

        embedding = self.embedder.encode(
            fact
        ).tolist()

        self.collection.add(

            documents=[fact],

            embeddings=[embedding],

            ids=[memory_id]
        )
        print("Stored ID:", memory_id)

        return memory_id




    def get_all_memories(self):

        results = self.collection.get()

        memories = []

        for i, doc in enumerate(
            results["documents"]
        ):

            memories.append({

                "id": results["ids"][i],

                "memory": doc
            })
        print(results)


        return memories


    def delete_memory(self, memory_id):

        results = self.collection.get()

        if memory_id not in results["ids"]:

            return False

        self.collection.delete(

            ids=[memory_id]
        )

        return True




    def search(self, query,k=3):

        embedding = self.embedder.encode(
            query
        ).tolist()

        results = self.collection.query(

            query_embeddings=[embedding],

            n_results=k
        )

        documents = results.get("documents", [])

        if documents and len(documents[0]) > 0:

            return documents[0]

        return []
