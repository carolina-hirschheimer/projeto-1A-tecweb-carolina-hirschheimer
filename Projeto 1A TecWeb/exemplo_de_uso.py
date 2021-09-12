from database import Database, Note

db = Database('banco')
#db.add(Note(title='Pão doce', content='Abra o pão e coloque o seu suco em pó favorito.'))
#db.add(Note(title='Hidratação', content='Lembrar de tomar água'))
db.update(Note(title='teste', content='teste', id=2))


#notes = db.get_all()
