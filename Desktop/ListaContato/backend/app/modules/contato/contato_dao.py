import sqlite3

class ContatoDAO:

    def connect(self):
        self.conn = sqlite3.connect('./app/database/agenda.db')
        self.cursor = self.conn.cursor()
    
    def disconnect(self):
        self.cursor.close()
        self.conn.close()
    
    def save(self, contato):
        params = [contato['nome'], contato['email'], contato['telefone']]
        self.connect()
        result = self.cursor.execute("""
        INSERT INTO contatos (nome, email, telefone) 
        VALUES (?,?,?)
        """, params)
        modified_registers = result.rowcount
        self.conn.commit()
        self.disconnect()
        return modified_registers
    
    def getAll(self):
        self.connect()
        self.cursor.execute("""
        SELECT * FROM contatos
        """)
        contacts = self.cursor.fetchall()
        self.disconnect()
        return contacts
    
    def update(self, contato):
        params = [contato['nome'], contato['email'], contato['telefone'], contato['id']]
        self.connect()
        result = self.cursor.execute("""
        UPDATE contatos SET nome = ?, 
        email = ?, 
        telefone = ?
        WHERE id = ?;
        """, params)
        modified_registers = result.rowcount
        self.conn.commit()
        self.disconnect()
        return modified_registers
    
    def delete(self, id):
        params = [id]
        self.connect()
        result = self.cursor.execute("""
        DELETE FROM contatos WHERE id = ?;
        """, params)
        modified_registers = result.rowcount
        self.conn.commit()
        self.disconnect()
        return modified_registers
