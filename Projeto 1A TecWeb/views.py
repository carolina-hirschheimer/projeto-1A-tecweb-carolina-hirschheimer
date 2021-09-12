from os import error, replace
from utils import add_data, delete_data, update_data, get_all_data, load_template, build_response
import urllib
from database import Database, Note

banco = Database('dados')

def index(request):

    if request.startswith('POST'):
        request = request.replace('\r', '')  # Remove caracteres indesejados

        partes = request.split('\n\n')
        corpo = partes[1]
        #params = {}
        titulo = urllib.parse.unquote_plus(corpo.split('&')[0].split('=')[1])
        detalhe = urllib.parse.unquote_plus(corpo.split('&')[1].split('=')[1])

        banco.add(Note(title=titulo, content=detalhe))



    note_template = load_template('components/note.html')
    notes_li = [
        note_template.format(title=dados.title, details=dados.content)
        for dados in banco.get_all()
    ]
    notes = '\n'.join(notes_li)
    

    if request.startswith('POST'):
        return build_response(code=303, reason='See Other', headers='Location: /') + load_template('indexUpdate.html').format(notes=notes).encode()
    else:
        return build_response() + load_template('indexUpdate.html').format(notes=notes).encode()