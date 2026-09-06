from huggingface_hub import InferenceClient

client = InferenceClient()

def generate_answer(prompt: str) -> str:
    """Generate an answer using a Hugging Face hosted LLM."""
    response = client.chat_completion(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="deepseek-ai/DeepSeek-V4-Flash-0731",
        max_tokens=200,
    )

    return response.choices[0].message.content