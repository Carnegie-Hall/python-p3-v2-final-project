from __init__ import CONN, CURSOR

import ipdb

class Tea():

    def __init__(self, name, id=None):
        self.name = name
        self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS teas (
                id INTEGER PRIMARY KEY,
                name TEXT
            );
        '''
        CONN.execute(sql)
        # CURSOR.commit()

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE teas;
        '''

        CURSOR.execute(sql)

    @classmethod
    def create(cls, name):
        tea = Tea(name=name)
        tea.save()
        return tea
    
    @classmethod
    def find_by_id(cls, id=id):
        sql='''
            SELECT * FROM teas
            WHERE id = ?;
        '''

        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return Tea.create_by_row(row)
        # print("no current boba")


    @classmethod
    def all(cls):
        sql = '''
            SELECT * FROM teas; 
        '''
        teas = CURSOR.execute(sql).fetchall()

        return [Tea.create_by_row(row) for row in teas]
    
    @classmethod
    def create_by_row(cls, row):
        return Tea(id=row[0], name=row[1])

    @classmethod
    def delete_all(cls):
        for tea in cls.all():
            tea.delete()

    def save(self):
        if not self.id:
            sql = '''
                INSERT INTO teas (name) VALUES (?)
            '''

            CURSOR.execute(sql, (self.name,))
            CONN.commit()
            sql = '''
                SELECT id FROM teas ORDER BY id DESC LIMIT 1
            '''
            self.id = CURSOR.execute(sql).fetchall()[0]

        else:
            sql = '''
                UPDATE teas SET name = ?
                WHERE id = ?
            '''
            CURSOR.execute(sql, (self.name, self.id))
            CONN.commit()

    def delete(self):
        sql = "DELETE FROM teas WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()


    def __repr__(self):
        return f'<Tea id={self.id} name="{self.name}">'
    