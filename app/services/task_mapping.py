TASK_KEYWORDS = {
    # Computer Vision
    "image-classification": [
        "image classification",
        "classify images",
        "image classifier",
        "classify an image",
    ],
    "object-detection": [
        "object detection",
        "detect objects",
        "object detector",
        "detect objects in images",
    ],
    "image-segmentation": [
        "image segmentation",
        "semantic segmentation",
        "instance segmentation",
        "segment images",
    ],
    "image-to-image": [
        "image to image",
        "image transformation",
        "image translation",
    ],

    # NLP
    "text-classification": [
        "text classification",
        "classify text",
        "text classifier",
        "sentiment classification",
        "sentiment analysis",
    ],
    "token-classification": [
        "token classification",
        "named entity recognition",
        "ner",
        "entity recognition",
    ],
    "question-answering": [
        "question answering",
        "question answering model",
        "qa model",
        "answer questions from text",
    ],
    "text-generation": [
        "text generation",
        "generate text",
        "text generation model",
        "language model",
    ],
    "summarization": [
        "summarization",
        "summarize text",
        "text summarization",
        "summarization model",
    ],
    "translation": [
        "translation",
        "translate text",
        "machine translation",
        "translation model",
    ],
    "fill-mask": [
        "fill mask",
        "masked language model",
        "masked language modeling",
    ],

    # Audio
    "automatic-speech-recognition": [
        "speech recognition",
        "automatic speech recognition",
        "speech to text",
        "transcribe audio",
        "transcription",
    ],
    "audio-classification": [
        "audio classification",
        "classify audio",
        "audio classifier",
    ],
    "text-to-speech": [
        "text to speech",
        "text-to-speech",
        "speech synthesis",
        "generate speech",
    ],

    # Multimodal
    "image-text-to-text": [
        "image captioning",
        "vision language model",
        "visual question answering",
        "image and text",
        "multimodal model",
    ],
}

# Phase 2:
# Replace rule-based keyword matching with an LLM-based intent classifier
# to handle more diverse natural-language queries and infer tasks from context.

def detect_task(query: str) -> str | None:
    query_lower = query.lower()

    for task, keywords in TASK_KEYWORDS.items():
        if any(keyword in query_lower for keyword in keywords):
            return task

    return None

