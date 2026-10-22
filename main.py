from paddleocr import PaddleOCR

ocr = PaddleOCR(
    lang="en",
    enable_mkldnn=False,
    use_doc_orientation_classify=False,
    use_doc_unwarping=False,
    use_textline_orientation=False
)

#results = ocr.predict("test2.jpg")
results = ocr.predict("test2.jpg")

for result in results:
    texts = result["rec_texts"]
    scores = result["rec_scores"]

    for text, score in zip(texts, scores):
        print(text, score)