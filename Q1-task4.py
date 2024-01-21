import spacy
from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch
from collections import Counter

# Suppress FutureWarning from spaCy
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# Load spaCy models
nlp_sci_sm = spacy.load('en_core_sci_sm')
nlp_bc5cdr_md = spacy.load('en_ner_bc5cdr_md')

# Load BioBERT model and tokenizer
biobert_tokenizer = AutoTokenizer.from_pretrained("monologg/biobert_v1.1_pubmed")
biobert_model = AutoModelForTokenClassification.from_pretrained("monologg/biobert_v1.1_pubmed")

# Read the content of the text file
file_path = 'output/Q1-task1_output.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()

# Process the text using spaCy models
doc_sci_sm = nlp_sci_sm(text[:1000000])  # Process only the first 1,000,000 characters
doc_bc5cdr_md = nlp_bc5cdr_md(text[:1000000])  # Process only the first 1,000,000 characters

# Process the text using BioBERT
tokens = biobert_tokenizer(text[:512], return_tensors='pt')  # Process only the first 512 tokens for BioBERT
with torch.no_grad():
    outputs = biobert_model(**tokens)

# Extract 'diseases' and 'drugs' entities separately
def extract_entities(doc, label):
    return [ent.text for ent in doc.ents if ent.label_ == label]

diseases_sci_sm = extract_entities(doc_sci_sm, 'DISEASE')
drugs_sci_sm = extract_entities(doc_sci_sm, 'CHEMICAL')

diseases_bc5cdr_md = extract_entities(doc_bc5cdr_md, 'DISEASE')
drugs_bc5cdr_md = extract_entities(doc_bc5cdr_md, 'CHEMICAL')

# Extract entities from BioBERT outputs
bio_entities = biobert_tokenizer.convert_ids_to_tokens(torch.argmax(outputs.logits, dim=2).squeeze().tolist())
bio_entities = [token for token, label in zip(bio_entities, outputs.logits.argmax(dim=2).squeeze().tolist()) if label != 0]

# Separate BioBERT entities into 'diseases' and 'drugs'
bio_diseases = [entity.replace("##", "") for entity in bio_entities if entity.startswith("B-Disease") or entity.startswith("I-Disease")]
bio_drugs = [entity.replace("##", "") for entity in bio_entities if entity.startswith("B-Chemical") or entity.startswith("I-Chemical")]

# Compare the differences
total_entities_sci_sm = len(diseases_sci_sm) + len(drugs_sci_sm)
total_entities_bc5cdr_md = len(diseases_bc5cdr_md) + len(drugs_bc5cdr_md)
total_entities_biobert = len(bio_diseases) + len(bio_drugs)

common_diseases = set(diseases_sci_sm) & set(diseases_bc5cdr_md) & set(bio_diseases)
common_drugs = set(drugs_sci_sm) & set(drugs_bc5cdr_md) & set(bio_drugs)

difference_diseases_sci_sm_bc5cdr_md = set(diseases_sci_sm) - set(diseases_bc5cdr_md)
difference_drugs_sci_sm_bc5cdr_md = set(drugs_sci_sm) - set(drugs_bc5cdr_md)

difference_diseases_biobert = set(bio_diseases) - set(diseases_sci_sm) - set(diseases_bc5cdr_md)
difference_drugs_biobert = set(bio_drugs) - set(drugs_sci_sm) - set(drugs_bc5cdr_md)

# Print the results
print(f"Total entities (en_core_sci_sm): {len(diseases_sci_sm)} diseases, {len(drugs_sci_sm)} drugs")
print(f"Total entities (en_ner_bc5cdr_md): {len(diseases_bc5cdr_md)} diseases, {len(drugs_bc5cdr_md)} drugs")
print(f"Total entities (BioBERT): {len(bio_diseases)} diseases, {len(bio_drugs)} drugs")

print(f"Common diseases: {common_diseases}")
print(f"Common drugs: {common_drugs}")

print(f"Difference in diseases (en_core_sci_sm vs. en_ner_bc5cdr_md): {difference_diseases_sci_sm_bc5cdr_md}")
print(f"Difference in drugs (en_core_sci_sm vs. en_ner_bc5cdr_md): {difference_drugs_sci_sm_bc5cdr_md}")

print(f"Difference in diseases (BioBERT): {difference_diseases_biobert}")
print(f"Difference in drugs (BioBERT): {difference_drugs_biobert}")

# Check for most common words
all_words = text.split()
most_common_words = Counter(all_words).most_common(10)
print(f"Most common words: {most_common_words}")
