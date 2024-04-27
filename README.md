# CIS4930-Data-Processing-and-Storage

This Python script implements a in-memory key-value database with transaction support. Users can perform basic operations like getting and putting key-value pairs through the program's simple CLI, as well as managing transactions.

## Setup

To run this application follow these steps:

1. Clone Repository and go to Repository Directory
2. Install Dependencies

```
pip install colorama
```

3. Execute Program

```
python InMemoryDB.py
```

## Usage

1. Get: Enter the key to retrieve its associated value from the database.
2. Put: Enter a key-value pair to store it in the database.
3. Begin transaction: Start a new transaction to group multiple database operations together.
4. Commit transaction: Apply the changes made within the current transaction to the main database state.
5. Rollback transaction: Abort the current transaction and revert any changes made within it.
6. Exit: Terminate the program.
