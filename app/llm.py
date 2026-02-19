from huggingface_hub import InferenceClient


# Uses your hf login automatically
client = InferenceClient(
    model="mistralai/Mistral-7B-Instruct-v0.2"
)


def generate(prompt):

    try:

        response = client.chat_completion(

            messages=[

                {
                    "role": "user",
                    "content": prompt
                }

            ],

            max_tokens=200,
            temperature=0.3
        )

        return response.choices[0].message.content

    except Exception as e:

        print("HF LLM Error:", e)

        return ""
