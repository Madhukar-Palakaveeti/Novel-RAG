import fitz
import re


my_path = 'book.pdf'
doc = fitz.open(my_path)
data = "".join(page.get_text() for page in doc[52:6247])


def para_split(text): #Split the data into paragraphs
    paras = re.split(r'(\n[A-Z])', text)
    new_matches = []
    for i in range(len(paras)):
        if i+1 <= len(paras) and re.match(r'\n[A-Z]',paras[i]):
            new_matches.append(paras[i] + paras[i+1])
            paras[i+1] = ""

        else:
            new_matches.append(paras[i])
        
    new_paras = [i.replace('\n', '') for i in new_matches if i]

    return new_paras

paragraphs = para_split(data)



