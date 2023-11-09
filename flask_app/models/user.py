from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import user

class User:
    DB = "users_schema"
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.createdAt = data['createdAt']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def save(cls, data):
        query = """INSERT INTO users (first_name,last_name,email)
    		VALUES (%(first_name)s,%(last_name)s,%(email)s);"""
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result

    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM users WHERE id = %(id)s";
        result = connectToMySQL(cls.DB).query_db(query, data)
        return cls(result[0])

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def update(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updatedAt=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.DB).query_db(query,data)

    @classmethod
    def destroy(cls, data):
        query  = """
        DELETE FROM users WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.DB).query_db(query, data)
        return results