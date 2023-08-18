from fastapi import FastAPI
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForTokenClassification


tokenizer = AutoTokenizer.from_pretrained("d4data/biomedical-ner-all")
model = AutoModelForTokenClassification.from_pretrained("d4data/biomedical-ner-all")

pipe = pipeline("ner", model=model, tokenizer=tokenizer, aggregation_strategy="simple")

app = FastAPI()

@app.get("/")
async def welcome():
    return "Welcome to MedTextAPI, follow the instructions on https://github.com/bsenst/MedTextAPI/blob/main/README.md"

@app.get("/extract_entities/")
async def extract_entities(t: str):

    entities = pipe(t)
    entities = [(i, entity["entity_group"], entity["word"]) for i, entity in enumerate(entities)]
    print(entities)

    return {"entities": entities}
