import MySQLdb
from flask import current_app, g

def get_db():
    if 'db' not in g:
        g.db = MySQLdb.connect(
            host=current_app.config['DB_HOST'],
            user=current_app.config['DB_USER'],
            password=current_app.config['DB_PASSWORD'],
            database=current_app.config['DB_NAME'],
            cursorclass=MySQLdb.cursors.DictCursor
        )
    return g.db

