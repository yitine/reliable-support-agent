from app.services.task_mapping import detect_task


def test_image_classification():
    assert detect_task(
        "What models are suitable for image classification?"
    ) == "image-classification"


def test_text_classification():
    assert detect_task(
        "What models can classify text?"
    ) == "text-classification"


def test_object_detection():
    assert detect_task(
        "What models are good for object detection?"
    ) == "object-detection"


def test_unknown_task():
    assert detect_task("What is LoRA?") is None