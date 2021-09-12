import sqlite3
from dataclasses import dataclass

@dataclass
class Note:
    id: int = None
    title: str = None
    content: str = ''

class Database:
    def __init__(self, nome):
        self.nome = nome
        self.conn = sqlite3.connect(self.nome+'.db')
        self.conn.execute('CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title STRING, content TEXT NOT NULL);')
        return None

    def add(self, note):
        self.conn.execute("INSERT INTO note (title, content) VALUES ('{title}', '{content}');".format(title = note.title, content = note.content))
        self.conn.commit()
        return None
    
    def get_all(self):
        cursor = self.conn.execute("SELECT id, title, content FROM note")
        self.conn.commit()
        result = []
        for linha in cursor:
            id = linha[0]
            title = linha[1]
            content = linha[2]
            lista = Note(id,title,content)
            result.append(lista)
        return result

    def update(self, entry):
        self.conn.execute("UPDATE note SET title = '{title}', content = '{content}' WHERE id = '{id}'".format(title = entry.title, content = entry.content, id = entry.id))
        self.conn.commit()
        return None

    def delete(self, note_id):
        self.conn.execute("DELETE FROM note WHERE id = {id}".format(id = note_id))
        self.conn.commit()
        return None