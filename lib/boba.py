from __init__ import CONN, CURSOR

import ipdb
# from tea import Tea

class Boba():

    def __init__(self, name, flavor, tea_id=None, id=None):
        self.name = name
        self.flavor = flavor
        self.tea_id = tea_id
        self.id = id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    def tea(self):
        from tea import Tea
        sql = '''
            SELECT * FROM teas
            WHERE id = ?
        '''
        row = CURSOR.execute(sql, (self.tea_id,)).fetchone()
        if row:
            return Tea.create_by_row(row)

    @property
    def flavor(self):
        return self._flavor

    @flavor.setter
    def flavor(self, flavor): 
        self._flavor = flavor 

    def bobas(self):
        sql = '''
            SELECT * FROM owners 
            WHERE id = {self.tea_id}
        '''
        rows = CURSOR.execute(sql, (self.id,))
        return [Boba.create_by_row(row) for row in rows]

    @classmethod
    def create_table(cls):
        sql = '''
            CREATE TABLE IF NOT EXISTS bobas (
                id INTEGER PRIMARY KEY,
                name TEXT, 
                flavor TEXT,
                tea_id INTEGER DEFAULT NULL
            );
        '''
        CONN.execute(sql)
        # CURSOR.commit()

    @classmethod
    def drop_table(cls):
        sql = '''
            DROP TABLE bobas;
        '''

        CURSOR.execute(sql)

    @classmethod
    def create(cls, name, flavor, tea_id=None):
        boba = Boba(name=name, flavor=flavor, tea_id=tea_id)
        boba.save()
        return boba
    
    @classmethod
    def find_by_id(cls, id=id):
        sql='''
            SELECT * FROM bobas
            WHERE id = ?;
        '''

        row = CURSOR.execute(sql, (id,)).fetchone()
        if row:
            return Boba.create_by_row(row)
        # print("no current boba")


    @classmethod
    def all(cls):
        sql = '''
            SELECT * FROM bobas; 
        '''
        bobas = CURSOR.execute(sql).fetchall()

        return [Boba.create_by_row(row) for row in bobas]
    
    @classmethod
    def unsold_bobas(cls):
        sql = '''
            SELECT * FROM bobas WHERE NOT tea_id NOT NULL;
        '''

        bobas = CURSOR.execute(sql).fetchall
        # ipdb.set_trace()
        return [Boba.create_by_row(row) for row in bobas]
            
    @classmethod
    def create_by_row(cls, row):
        return Boba(id=row[0], name=row[1], flavor=row[2], tea_id=row[3])

    @classmethod
    def delete_all(cls):
        for boba in cls.all():
            boba.delete()

    def save(self):
        if not self.id:
            sql = '''
                INSERT INTO bobas (name, flavor, tea_id) VALUES (?, ?, ?)
            '''

            CURSOR.execute(sql, (self.name, self.flavor, self.tea_id))
            CONN.commit()
            sql = '''
                SELECT id FROM bobas ORDER BY id DESC LIMIT 1
            '''
            self.id = CURSOR.execute(sql).fetchall()[0]

        else:
            sql = '''
                UPDATE bobas SET name = ?, flavor = ?
                WHERE id = ?
            '''
            CURSOR.execute(sql, (self.name, self.flavor, self.tea_id, self.id))
            CONN.commit()

    def delete(self):
        sql = "DELETE FROM bobas WHERE id = ?"
        CURSOR.execute(sql, (self.id, self.flavor, self.id))
        CONN.commit()


    def __repr__(self):
        return f'<Boba id={self.id} name="{self.name}" flavor="{self.flavor}" tea_id={self.tea_id}>'
    