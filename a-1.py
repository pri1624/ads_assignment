import spacy

def recognize_entities(input_file, output_file):
    
    nlp = spacy.load("en_core_web_sm")
    
    
    with open(input_file, "r") as file:
        text = file.read()
    
    doc = nlp(text)
    
    with open(output_file, "w") as file:
        for ent in doc.ents:
            file.write(f"{ent.text} - {ent.label_}\n")

input_file = "C:\\cse\\uni\\ads\\Input.txt"
output_file = "C:\\cse\\uni\\ads\\Output.txt"


recognize_entities(input_file, output_file)

print("Named entities have been written to the output file.")