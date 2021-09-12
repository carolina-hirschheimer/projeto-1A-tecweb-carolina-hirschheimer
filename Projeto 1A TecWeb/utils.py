import json
from database import Note, Database

def extract_route(requisicao):
    if requisicao.startswith('GET'):
        lista1 = requisicao.split("GET /")
    else:
        lista1 = requisicao.split("POST /")

    lista2 = lista1[1].split(" ")
    return lista2[0]

def read_file(path):
    lista = str(path).split(".")
    if lista[-1]=="txt" or lista[-1]=="html" or lista[-1]=="css" or lista[-1]=="js":
        with open(path, "rb") as file:
            text = file.read()
            return text
    else:
        with open(path, "rb") as file:
            binary = file.read()
        return binary
        
def load_template(file_path):
    file = open("templates/"+file_path)
    content = file.read()
    file.close()
    return content

def add_data(params, bancoDados):
    db = Database(bancoDados)
    addDados = list(params.values())
    db.add(Note(title=addDados[0], content=addDados[1]))  

def get_all_data(bancoDados):
    db = Database(bancoDados)
    dados = db.get_all()
    return dados

def update_data(params, bancoDados):
    db = Database(bancoDados)
    updateDados = list(params.values())
    db.update(Note(title=updateDados[0], content=updateDados[1],id=updateDados[2])) 

def delete_data(note_id, bancoDados):
    db = Database(bancoDados)
    db.delete(note_id) 

'''def add_note(note):
    with open('data/notes.json',encoding='UTF-8') as file:
        content = json.load(file)
    content.append(note)
    with open('data/notes.json','w',encoding='UTF-8') as file:
        json.dump(content, file, ensure_ascii=False)'''

def build_response(body='', code=200,reason='OK',headers=''):
    if body == '' and headers == '':
        return (f'HTTP/1.1 {code} {reason}\n\n').encode()
    elif body == '' and headers != '':
        return (f'HTTP/1.1 {code} {reason}\n{headers}\n\n').encode()
    elif body != '' and headers == '':
        return (f'HTTP/1.1 {code} {reason}\n\n{body}').encode()
    elif body != '' and headers != '':
        return (f'HTTP/1.1 {code} {reason}\n{headers}\n\n{body}').encode()