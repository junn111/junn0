class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print("title = ", self.title)
        print("author = ", self.author)
        print("price = ", self.price)

    def __eq__(self, other):
        return self.price == other.price


book1 = Book('책 제목1', '저자1', '가격1')
book2 = Book('책 제목1', '저자1', '가격1')

book1.display()
book2.display()

print(book1 == book2)

실습2


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("잔액이 부족하면 출금 불가능")

    def display_balance(self):
        print(f"현재 잔액: {self.balance}")


text0 = BankAccount("나", 1000)
text0.deposit(500)
text0.display_balance()
text0.withdraw(300)
text0.display_balance()
text0.withdraw(1500)
text0.display_balance()

실습3


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        print(f"이름: {self.name}, 급여: {self.salary}")


class Manager:
    def __init__(self):
        self.team_members = []

    def add_team_member(self, employee):
        self.team_members.append(employee)

    def display_team(self):
        for member in self.team_members:
            member.display_info()


text1 = Employee("직원1", 500)
text2 = Employee("직원2", 1000)
text3 = Manager()
text3.add_team_member(text1)  # 직원1
text3.add_team_member(text2)  # 직원2
text3.display_team()
