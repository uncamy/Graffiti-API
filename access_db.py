import sqlite3
import pandas as pd
from contextlib import closing


def create_database(db_file, schem, csv):
    def init_db():
        with closing(connect_db(db_file)) as db:
            with open(schema, mode='r') as f: #r is reading
                db.cursor().executescript(f.read())
                db.commit()

    def generate_db_from_csv():
        graff_data = pd.read_csv('./Graffiti_Locations.csv')
        for row in graff_data:
            add_row(row)

def connect_db(db_file=db_file):
    return sqlite3.connect(db_file)

def select(database, query, items=None):
    with closing(connect_db(database)) as db:
        if items:
            q = db.execute(query, items)
        else:
            q = db.execute(query)
            return q.fetchall()

def insert(database, query, items):
    with closing(connect_db(database)) as db:
        db.execute(query, items)
        db.commit()

def update(database, query, items):
    insert(database, query, items)

def delete(database, query, items):
    with closing(connect_db(database)) as db:
        db.execute(query, items)
        db.commit

def add_row(row):
    insert(db_file, 'INSERT INTO graff_nyc_data\
        (incident_address, borough, data_created, status, lat, lon)\
        VALUES (?, ?, ?, ?, ?, ?)', row)

def add_latlon():
    insert(db_file, 'INSERT INTO graff_nyc_data (lat, lon) VALUES (?,?)',\
           (lat, lon)
