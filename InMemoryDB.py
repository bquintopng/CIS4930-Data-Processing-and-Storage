from colorama import Fore, Back, Style

class InMemoryDB:
    def __init__(self):
        self.data = {}  # In-memory store for key-value pairs
        self.transaction_in_progress = False
        self.transaction_data = {}

    def get(self, key):
        return self.data.get(key, None)

    def put(self, key, value):
        if not self.transaction_in_progress:
            raise Exception("No transaction in progress")
        self.transaction_data[key] = value

    def begin_transaction(self):
        if self.transaction_in_progress:
            raise Exception("Transaction already in progress")
        self.transaction_in_progress = True
        self.transaction_data = self.data.copy()

    def commit(self):
        if not self.transaction_in_progress:
            raise Exception("No transaction in progress")
        self.data.update(self.transaction_data)
        self.transaction_in_progress = False
        self.transaction_data.clear()

    def rollback(self):
        if not self.transaction_in_progress:
            raise Exception("No transaction in progress")
        self.transaction_in_progress = False
        self.transaction_data = {}

    def display(self):
        print(f"\nData: {self.data}")
        print(f"Transaction Data: {self.transaction_data}")

        if self.transaction_in_progress:
            print(Fore.GREEN + "Transaction Active")
        else:
            print(Fore.RED + "Transaction Inactive")



def main():
    database = InMemoryDB()
    
    print("Welcome to Key-Value Transaction Database")
    while True:   

        database.display()

        print(Fore.WHITE + "\n1. Get value by key")
        print("2. Put value by key")
        print("3. Begin transaction")
        print("4. Commit transaction")
        print("5. Rollback transaction")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            key = input("Enter key: ")
            value = database.get(key)
            print(f"Value: {value}")

        elif choice == "2":
            key = input("Enter key: ")
            value = int(input("Enter value: "))
            try:
                database.put(key, value)
                print("Value stored successfully.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "3":
            database.begin_transaction()
            print("Transaction started.")

        elif choice == "4":
            try:
                database.commit()
                print("Transaction committed.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "5":
            try:
                database.rollback()
                print("Transaction rolled back.")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == "6":
            break

        else:
            print("Invalid entry. Usage: [#1-7]")

if __name__ == "__main__":
    main()