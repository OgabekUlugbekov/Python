# 1)
# 1. Define Task Class
class Task:
    def __init__(self, title, description, due_date, status="incomplete"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status


# 2. Define ToDoList Class
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_task_complete(self, title):
        for task in self.tasks:
            if task.title == title:
                task.status = "complete"
                break

    def list_all_tasks(self):
        for task in self.tasks:
            print(
                f"Title: {task.title}, Description: {task.description}, Due Date: {task.due_date}, Status: {task.status}")

    def display_incomplete_tasks(self):
        for task in self.tasks:
            if task.status == "incomplete":
                print(
                    f"Title: {task.title}, Description: {task.description}, Due Date: {task.due_date}, Status: {task.status}")


# 3. Create Main Program
def main():
    todo_list = ToDoList()

    while True:
        print("\nToDo List Application")
        print("1. Add Task")
        print("2. Mark Task as Complete")
        print("3. List All Tasks")
        print("4. Display Incomplete Tasks")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            task = Task(title, description, due_date)
            todo_list.add_task(task)
            print("Task added successfully!")

        elif choice == "2":
            title = input("Enter task title to mark as complete: ")
            todo_list.mark_task_complete(title)
            print("Task marked as complete!")

        elif choice == "3":
            print("All Tasks:")
            todo_list.list_all_tasks()

        elif choice == "4":
            print("Incomplete Tasks:")
            todo_list.display_incomplete_tasks()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")


# 4. Test the Application
if __name__ == "__main__":
    main()


# 2)
# 1. Define Post Class
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author


# 2. Define Blog Class
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def list_all_posts(self):
        for post in self.posts:
            print(f"Title: {post.title}, Author: {post.author}, Content: {post.content}")

    def display_posts_by_author(self, author):
        for post in self.posts:
            if post.author == author:
                print(f"Title: {post.title}, Author: {post.author}, Content: {post.content}")

    # 4. Enhance Blog System
    def delete_post(self, title):
        self.posts = [post for post in self.posts if post.title != title]

    def edit_post(self, title, new_content):
        for post in self.posts:
            if post.title == title:
                post.content = new_content
                break

    def display_latest_posts(self, n):
        for post in self.posts[-n:]:
            print(f"Title: {post.title}, Author: {post.author}, Content: {post.content}")


# 3. Create Main Program
def main():
    blog = Blog()

    while True:
        print("\nBlog System")
        print("1. Add Post")
        print("2. List All Posts")
        print("3. Display Posts by Author")
        print("4. Delete Post")
        print("5. Edit Post")
        print("6. Display Latest Posts")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter post title: ")
            content = input("Enter post content: ")
            author = input("Enter author name: ")
            post = Post(title, content, author)
            blog.add_post(post)
            print("Post added successfully!")

        elif choice == "2":
            print("All Posts:")
            blog.list_all_posts()

        elif choice == "3":
            author = input("Enter author name: ")
            print(f"Posts by {author}:")
            blog.display_posts_by_author(author)

        elif choice == "4":
            title = input("Enter post title to delete: ")
            blog.delete_post(title)
            print("Post deleted successfully!")

        elif choice == "5":
            title = input("Enter post title to edit: ")
            new_content = input("Enter new content: ")
            blog.edit_post(title, new_content)
            print("Post edited successfully!")

        elif choice == "6":
            n = int(input("Enter number of latest posts to display: "))
            print(f"Latest {n} Posts:")
            blog.display_latest_posts(n)

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")


# 5. Test the Application
if __name__ == "__main__":
    main()


# 3)
# 1. Define Account Class
class Account:
    def __init__(self, account_number, account_holder_name, balance=0):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance


# 2. Define Bank Class
class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        self.accounts[account.account_number] = account

    def check_balance(self, account_number):
        if account_number in self.accounts:
            return self.accounts[account_number].balance
        return None

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number].balance += amount

    def withdraw(self, account_number, amount):
        if account_number in self.accounts and self.accounts[account_number].balance >= amount:
            self.accounts[account_number].balance -= amount

    # 4. Enhance Banking System
    def transfer(self, from_account, to_account, amount):
        if from_account in self.accounts and to_account in self.accounts:
            if self.accounts[from_account].balance >= amount:
                self.accounts[from_account].balance -= amount
                self.accounts[to_account].balance += amount

    def display_account_details(self, account_number):
        if account_number in self.accounts:
            account = self.accounts[account_number]
            print(
                f"Account Number: {account.account_number}, Holder: {account.account_holder_name}, Balance: {account.balance}")

    def handle_overdraft(self, account_number, amount):
        if account_number in self.accounts:
            if self.accounts[account_number].balance < amount:
                print("Warning: Overdraft! Insufficient funds.")
            else:
                self.accounts[account_number].balance -= amount


# 3. Create Main Program
def main():
    bank = Bank()

    while True:
        print("\nBanking System")
        print("1. Add Account")
        print("2. Check Balance")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Transfer Money")
        print("6. Display Account Details")
        print("7. Handle Overdraft")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder_name = input("Enter account holder name: ")
            balance = float(input("Enter initial balance: "))
            account = Account(account_number, account_holder_name, balance)
            bank.add_account(account)
            print("Account added successfully!")

        elif choice == "2":
            account_number = input("Enter account number: ")
            balance = bank.check_balance(account_number)
            if balance is not None:
                print(f"Balance: {balance}")
            else:
                print("Account not found!")

        elif choice == "3":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            bank.deposit(account_number, amount)
            print("Deposit successful!")

        elif choice == "4":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.withdraw(account_number, amount)
            print("Withdrawal successful!")

        elif choice == "5":
            from_account = input("Enter source account number: ")
            to_account = input("Enter destination account number: ")
            amount = float(input("Enter amount to transfer: "))
            bank.transfer(from_account, to_account, amount)
            print("Transfer successful!")

        elif choice == "6":
            account_number = input("Enter account number: ")
            bank.display_account_details(account_number)

        elif choice == "7":
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            bank.handle_overdraft(account_number, amount)

        elif choice == "8":
            print("Exiting...")
            break

        else:
            print("Invalid choice, please try again.")


# 5. Test the Application
if __name__ == "__main__":
    main()