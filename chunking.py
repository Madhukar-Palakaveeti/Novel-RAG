import re
from tqdm import tqdm
import json

def word_count(text):
    return len(re.findall(r'\w+', text))

 
with open('paragraphs.txt', 'r', encoding='utf-8') as f:
    paragraphs = f.readlines()

def process_paragraphs(paragraphs, target_length=200, min_length=100, max_length=300):
    
    processed_paragraphs = []
    current_paragraph = ""
    
    for i, paragraph in enumerate(tqdm(paragraphs, desc=f"Processing paragraphs")):
        tqdm.write(f"Paragraph {i+1}")
        words = paragraph.split()
        
        if word_count(current_paragraph + paragraph) < min_length:
            # Combine short paragraphs
            current_paragraph += paragraph if current_paragraph else paragraph
        elif word_count(paragraph) > max_length:
            if current_paragraph:
                processed_paragraphs.append(current_paragraph)
                current_paragraph = ""
            
            # Split the long paragraph
            start = 0
            while start < len(words):
                end = start + target_length
                if end > len(words):
                    end = len(words)
                processed_paragraphs.append(" ".join(words[start:end]))
                start = end 
        else:
            # Handle normal-sized paragraphs
            if current_paragraph:
                processed_paragraphs.append(current_paragraph)
            current_paragraph = paragraph

        # Check if we've reached or exceeded the target length
        if word_count(current_paragraph) >= target_length:
            processed_paragraphs.append(current_paragraph)
            current_paragraph = ""

    # Add any remaining text
    if current_paragraph:
        processed_paragraphs.append(current_paragraph)

    return processed_paragraphs

chunks = []
for i in range(len(paragraphs)):
    chunks.extend(process_paragraphs(paragraphs[i]))

with open('chunks.json', 'w') as json_file:
    json.dump({"chunks" : chunks}, json_file)