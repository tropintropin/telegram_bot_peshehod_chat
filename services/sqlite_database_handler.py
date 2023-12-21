import sqlite3
from sqlite3 import Error
from typing import Dict, List, Optional


def create_connection(path: str) -> Optional[sqlite3.Connection]:
    """
    Connect to the SQLite database if it's exist or create a new one.
    :param path: Path to the SQLite database
    :return: Connection object or None if connection failed
    """
    connection: Optional[sqlite3.Connection] = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


def open_query_file(path: str) -> str:
    """
    Open a file with SQL query and return the query as a string.
    :param path: Path to the file with SQL query
    :return: SQL query as a string
    """
    with open(path, "r") as f:
        query = f.read().strip()
        return query


def execute_query(connection: sqlite3.Connection, query: str) -> None:
    """
    Execute a query on the SQLite database.
    :param connection: Connection to the SQLite database
    :param query: SQL query to execute
    """
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_read_query(connection: sqlite3.Connection, query: str) -> List[str]:
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")
        return []


def get_tours_list(user_answers: Dict[str, str]) -> List[str]:
    query = """
    SELECT DISTINCT tours_list
    FROM tours
    WHERE
        is_group = ?
        AND have_children = ?
        AND (kids IS NULL OR kids = ?)
        AND visit = ?
"""
    if connection is not None:
        cursor = connection.cursor()
        cursor.execute(
            query,
            (
                user_answers["is_group"],
                user_answers["have_children"],
                user_answers["kids"],
                user_answers["visit"],
            ),
        )
        tours_list = cursor.fetchone()[0]

        return tours_list
    return []  # If connection is None


delete_tours_table_values = open_query_file("services/delete_tours_table.sql")
create_tours_table = open_query_file("services/create_tours_table.sql")
create_tours = open_query_file("services/create_tours.sql")

connection = create_connection("tours.sqlite")
if connection is not None:
    execute_query(connection=connection, query=delete_tours_table_values)
    execute_query(connection=connection, query=create_tours_table)
    execute_query(connection=connection, query=create_tours)

    select_tours = "SELECT * FROM tours"
    tours = execute_read_query(connection=connection, query=select_tours)

    for tour in tours:
        print(tour)
