from config import CONN, CURSOR

class Teacher:

    def _init_(self, name , title, id=None):
        self.id = id
        self.name = name
        self.title = title

    def __repr__(self):
        return f"Teacher (id={self.id}, name={self.name}, title={self.title})"
    
    @classmethod
    def create_table(cls):
        "create Teacher Table"
        sql ="""
           CREATE TABLE IF NOT EXISTS teachers()
              id INTEGER PRIMARY KEY,
                name TEXT,
                title TEXT
              )
           """"
        
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        "drop  Table"
        sql = """
        DROP TABLE IF EXISTS teachers
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod 
    def create(cls, name , title):
     teacher = (cls,name, title)
     teacher.save()
     return teacher
    

    def save(self):
        "save object to db"

        sql = """
        INSERT INTO teachers (name, title) VALUES(?, ?)
        """
        CURSOR.execute(sql, (self.name, self.title))
        CONN.commit()

        self.id = CURSOR.lastrowid

        type(self).all

    def delete(self):
        "delete object from db"
        sql = """
        DELETE FROM teachers WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()