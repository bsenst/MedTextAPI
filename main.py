from fastapi import FastAPI
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification


tokenizer = AutoTokenizer.from_pretrained("d4data/biomedical-ner-all")
model = AutoModelForTokenClassification.from_pretrained("d4data/biomedical-ner-all")

pipe = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

app = FastAPI()

@app.get("/")
async def extract_entities(t: str):
    print(t)

    entities = pipe(t)
    entities = [(i, entity["entity_group"], entity["word"]) for i, entity in enumerate(entities)]
    print(entities)

    return {"entities": entities}
