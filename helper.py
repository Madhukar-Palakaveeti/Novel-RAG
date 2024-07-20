import json

paragraphs = []
with open('pre_paras.json', 'r', encoding='utf-8') as json_file:
    with open('paragraphs.txt', 'w', encoding='utf-8') as file:
        data = json.load(json_file)
        pre_paras = data['paragraphs']
        for i in range(0, len(pre_paras) , 10):
            paragraphs.append("\n".join(pre_paras[i:i+10]))
        
        for para in paragraphs:
            file.write(para.replace('\n', '').strip() + '\n')




