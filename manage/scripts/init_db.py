#!/usr/bin/env python

from manage.db import init_db

if __name__ == "__main__":
    print("Initializing the database...")
    init_db()
    print("Database initialized successfully!")