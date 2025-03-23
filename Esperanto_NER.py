import spacy

# Load spaCy's multilingual NER model
nlp = spacy.load("xx_ent_wiki_sm")

# Read the text from your file
with open("esf_sample.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Run NER
doc = nlp(text)

# Print the named entities
print("Named Entities detected:\n")
for ent in doc.ents:
    print(f"Text: {ent.text}  |  Label: {ent.label_}")