from huggingface_hub import InferenceClient
import os


HF_TOKEN = os.getenv("HF_TOKEN")

client = InferenceClient(

    model="mistralai/Mistral-7B-Instruct-v0.2",

    token=HF_TOKEN
)


def generate(prompt):

    try:

        response = client.text_generation(

            prompt,

            max_new_tokens=200,

            temperature=0.7
        )

        return response

    except Exception as e:

        print("HF Error:", e)

        return "Sorry, AI response unavailable right now."
