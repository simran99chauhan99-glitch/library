from datetime import date

class Book:
    def __init__(self, title):
        self.title = title
        self.on_loan = False
        self.due_date = None

    def loan_to_patron(self, due_date):
        self.on_loan = True
        self.due_date = due_date

    def return_book(self):
        self.on_loan = False
        self.due_date = None

    def availability_status(self):
        if not self.on_loan:
            return f"The book '{self.title}' is available for loan."
        else:
            return f"The book '{self.title}' is currently on loan. Return due date: {self.due_date}"

# Example usage:
mybook = Book("1984")
print(mybook.availability_status()) # Should print 'available for loan'

mybook.loan_to_patron(date(2025, 12, 1))
print(mybook.availability_status()) # Should print 'on loan, return due date: 2025-12-01'
