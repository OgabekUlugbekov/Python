# 1. Circle Class
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


circle = Circle(5)
print(circle.area())
print(circle.perimeter())

# 2. Person Class
from datetime import datetime


class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")

    def age(self):
        today = datetime.now()
        return today.year - self.date_of_birth.year - (
                    (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day))


person = Person("John", "USA", "1990-05-15")
print(person.age())


# 3. Calculator Class
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b


calc = Calculator()
print(calc.add(5, 3))
print(calc.subtract(5, 3))
print(calc.multiply(5, 3))
print(calc.divide(5, 3))


# 4. Shape and Subclasses
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        return self.a + self.b + self.c


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side


circle = Circle(5)
triangle = Triangle(3, 4, 5)
square = Square(4)
print(circle.area(), circle.perimeter())
print(triangle.area(), triangle.perimeter())
print(square.area(), square.perimeter())


# 5. Binary Search Tree Class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search(node.left, value)
        return self._search(node.right, value)


bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
print(bst.search(3) is not None)


# 6. Stack Data Structure
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())
print(stack.pop())


# 7. Linked List Data Structure
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()


linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.display()
linked_list.delete(2)
linked_list.display()


# 8. Shopping Cart Class
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, quantity):
        self.items[item] = {"price": price, "quantity": quantity}

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(item["price"] * item["quantity"] for item in self.items.values())


cart = ShoppingCart()
cart.add_item("apple", 1, 5)
cart.add_item("banana", 2, 3)
print(cart.total_price())
cart.remove_item("apple")
print(cart.total_price())


# 9. Stack with Display
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0

    def display(self):
        print(self.items)


stack = Stack()
stack.push(1)
stack.push(2)
stack.display()
stack.pop()
stack.display()


# 10. Queue Data Structure
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())
print(queue.dequeue())


# 11. Bank Class
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, balance=0):
        self.accounts[account_number] = balance

    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            self.accounts[account_number] += amount

    def withdraw(self, account_number, amount):
        if account_number in self.accounts and self.accounts[account_number] >= amount:
            self.accounts[account_number] -= amount

    def get_balance(self, account_number):
        return self.accounts.get(account_number, 0)


bank = Bank()
bank.create_account("123", 1000)
bank.deposit("123", 500)
bank.withdraw("123", 200)
print(bank.get_balance("123"))