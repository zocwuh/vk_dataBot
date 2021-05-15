from typing import *

import sqlalchemy.engine.cursor
from sqlalchemy import *

engine = create_engine("sqlite:///database/users.db")
metadata = MetaData()

users = Table("user", metadata,
              Column("id", Integer, primary_key=True),
              Column("data", String),
              )
if "user" not in metadata.tables.keys():
    users.create(engine)

metadata.bind = engine
conn = engine.connect()


def add_user(user_id, data):
    query = users.insert({"id": user_id, "data": data})
    conn.execute(query)


def delete_user(user_id: Union[int, None] = None):
    if user_id is None:
        query = users.delete()
        conn.execute(query)
        return
    query = users.delete().where(users.columns.id == user_id)
    conn.execute(query)


def get_user(user_id: Union[int, None] = None) -> Union[list, sqlalchemy.engine.cursor.LegacyCursorResult]:
    if user_id is None:
        query = users.select()
        return list(conn.execute(query))
    query = users.select().where(users.columns.id == user_id)
    return conn.execute(query)


def update_user(user_id: int, data: Union[float, int, str]):
    query = users.update().values(data=data).where(users.columns.id == user_id)
    conn.execute(query)
