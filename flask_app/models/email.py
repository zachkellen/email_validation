from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

class Email():
    def __init__(self,data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_email(cls, data):
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        results = connectToMySQL('email_schema').query_db(query, data)
        return results

    @classmethod
    def get_all_emails(cls):
        query = "SELECT * FROM emails;"
        results = connectToMySQL('email_schema').query_db(query)
        
        emails = []
        for item in results:
            new_email = Email(item)
            emails.append(new_email)
        return emails

    @staticmethod
    def validate_email(email):
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(email['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid