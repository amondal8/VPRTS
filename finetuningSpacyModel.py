import spacy
import random
from spacy.util import minibatch, compounding
from spacy.training import Example

# Load the "en_core_web_lg" model
nlp = spacy.load("en_core_web_lg")

# Load the SE-REDS dataset
with open("se-reds-dataset.json", "r") as f:
    data = json.load(f)

# Define the entity labels for the dataset
entity_labels = ["METHOD", "CLASS", "VARIABLE"]

# Define the number of training iterations and batch size
n_iter = 20
batch_size = 32

# Disable all other pipeline components except for the ner
nlp.disable_pipes([pipe for pipe in nlp.pipe_names if pipe != "ner"])

# Add the new entity labels to the ner component
for label in entity_labels:
    nlp.entity.add_label(label)

# Train the ner component on the SE-REDS dataset
optimizer = nlp.create_optimizer()
for i in range(n_iter):
    random.shuffle(data)
    batches = minibatch(data, size=compounding(batch_size, max_batch_size=512))
    for batch in batches:
        examples = []
        for text, entities in batch:
            example = Example.from_dict(nlp.make_doc(text), {"entities": entities})
            examples.append(example)
        nlp.update(examples, sgd=optimizer)

# Save the trained model to disk
nlp.to_disk("se-reds-ner-model")
