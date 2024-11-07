import random
def randomId():
    return random.randint(1000, 9999)

class User(object):
    def __init__(self, userName, passWord):
        self.userName = userName
        self.passWord = passWord
        self.accounts = []
        self.is_authenticated = False

    def add_account(self, account):
        self.accounts.append(account)
        
    def authenticate(self, username, password):
        if self.userName == username and self.passWord == password:
            self.is_authenticated = True
            return True
        return False
            
        

class Library(object):
    def __init__(self, user, id=None):
        if not user.is_authenticated:
            raise ValueError("User must be authenticated to create an account.")
        self.user = user
        self.id = id if id is not None else randomId()
        self.books = [
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "ISBN": "9780060935467", "status": "available"},
    {"title": "1984", "author": "George Orwell", "ISBN": "9780451524935", "status": "borrowed"},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "ISBN": "9780141439518", "status": "available"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "ISBN": "9780743273565", "status": "available"},
    {"title": "Moby-Dick", "author": "Herman Melville", "ISBN": "9780142437247", "status": "borrowed"},
    {"title": "War and Peace", "author": "Leo Tolstoy", "ISBN": "9780199232765", "status": "available"},
    {"title": "The Odyssey", "author": "Homer", "ISBN": "9780140268867", "status": "available"},
    {"title": "Crime and Punishment", "author": "Fyodor Dostoevsky", "ISBN": "9780140449136", "status": "borrowed"},
    {"title": "Brave New World", "author": "Aldous Huxley", "ISBN": "9780060850524", "status": "available"},
    {"title": "Jane Eyre", "author": "Charlotte Brontë", "ISBN": "9780142437209", "status": "available"},
    {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "ISBN": "9780316769488", "status": "borrowed"},
    {"title": "Wuthering Heights", "author": "Emily Brontë", "ISBN": "9780141439556", "status": "available"},
    {"title": "The Brothers Karamazov", "author": "Fyodor Dostoevsky", "ISBN": "9780374528379", "status": "available"},
    {"title": "The Divine Comedy", "author": "Dante Alighieri", "ISBN": "9780142437223", "status": "borrowed"},
    {"title": "Anna Karenina", "author": "Leo Tolstoy", "ISBN": "9780143035008", "status": "available"},
    {"title": "Les Misérables", "author": "Victor Hugo", "ISBN": "9780451419439", "status": "borrowed"},
    {"title": "The Hobbit", "author": "J.R.R. Tolkien", "ISBN": "9780547928227", "status": "available"},
    {"title": "The Iliad", "author": "Homer", "ISBN": "9780140275360", "status": "available"},
    {"title": "Frankenstein", "author": "Mary Shelley", "ISBN": "9780143131847", "status": "borrowed"},
    {"title": "Don Quixote", "author": "Miguel de Cervantes", "ISBN": "9780060934348", "status": "available"},
    {"title": "Fahrenheit 451", "author": "Ray Bradbury", "ISBN": "9781451673319", "status": "borrowed"},
    {"title": "Dracula", "author": "Bram Stoker", "ISBN": "9780141439846", "status": "available"},
    {"title": "The Lord of the Rings", "author": "J.R.R. Tolkien", "ISBN": "9780618640157", "status": "available"},
    {"title": "Catch-22", "author": "Joseph Heller", "ISBN": "9781451626656", "status": "borrowed"},
    {"title": "The Scarlet Letter", "author": "Nathaniel Hawthorne", "ISBN": "9780142437261", "status": "available"},
    {"title": "A Tale of Two Cities", "author": "Charles Dickens", "ISBN": "9780141439600", "status": "available"},
    {"title": "The Grapes of Wrath", "author": "John Steinbeck", "ISBN": "9780143039433", "status": "borrowed"},
    {"title": "Heart of Darkness", "author": "Joseph Conrad", "ISBN": "9780141441672", "status": "available"},
    {"title": "Sense and Sensibility", "author": "Jane Austen", "ISBN": "9780141439662", "status": "borrowed"},
    {"title": "Lolita", "author": "Vladimir Nabokov", "ISBN": "9780679723165", "status": "available"},
    {"title": "The Count of Monte Cristo", "author": "Alexandre Dumas", "ISBN": "9780140449266", "status": "available"},
    {"title": "The Picture of Dorian Gray", "author": "Oscar Wilde", "ISBN": "9780141439570", "status": "borrowed"},
    {"title": "Madame Bovary", "author": "Gustave Flaubert", "ISBN": "9780140449129", "status": "available"},
    {"title": "One Hundred Years of Solitude", "author": "Gabriel García Márquez", "ISBN": "9780060883288", "status": "borrowed"},
    {"title": "Ulysses", "author": "James Joyce", "ISBN": "9780679722762", "status": "available"},
    {"title": "The Stranger", "author": "Albert Camus", "ISBN": "9780679720201", "status": "borrowed"},
    {"title": "The Metamorphosis", "author": "Franz Kafka", "ISBN": "9780143105244", "status": "available"},
    {"title": "David Copperfield", "author": "Charles Dickens", "ISBN": "9780140439441", "status": "available"},
    {"title": "The Sun Also Rises", "author": "Ernest Hemingway", "ISBN": "9780743297334", "status": "borrowed"},
    {"title": "Mansfield Park", "author": "Jane Austen", "ISBN": "9780141439808", "status": "available"},
    {"title": "Great Expectations", "author": "Charles Dickens", "ISBN": "9780141439563", "status": "available"},
    {"title": "Beloved", "author": "Toni Morrison", "ISBN": "9781400033416", "status": "borrowed"},
    {"title": "Slaughterhouse-Five", "author": "Kurt Vonnegut", "ISBN": "9780385333849", "status": "available"},
    {"title": "Alice's Adventures in Wonderland", "author": "Lewis Carroll", "ISBN": "9780141439761", "status": "available"},
    {"title": "Gone with the Wind", "author": "Margaret Mitchell", "ISBN": "9781451635627", "status": "borrowed"},
    {"title": "The Old Man and the Sea", "author": "Ernest Hemingway", "ISBN": "9780684801223", "status": "available"},
    {"title": "On the Road", "author": "Jack Kerouac", "ISBN": "9780140283297", "status": "borrowed"},
    {"title": "Invisible Man", "author": "Ralph Ellison", "ISBN": "9780679732761", "status": "available"},
    {"title": "The Bell Jar", "author": "Sylvia Plath", "ISBN": "9780060837021", "status": "available"},
    {"title": "Things Fall Apart", "author": "Chinua Achebe", "ISBN": "9780385474542", "status": "borrowed"},
    {"title": "Middlemarch", "author": "George Eliot", "ISBN": "9780141439549", "status": "available"}
]

class Book(Library):
    def __init__(self, user, id=None):
        super().__init__(user, id)
    def borrow_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                if book["status"] == "available":
                    book["status"] = "borrowed" # Updating status
                    print(f'You have successfully borrowed "{title}".')
                print(f'Sorry, "{title}" is currently borrowed.')
        print(f'Book "{title}" not found in the library.')
    

    def return_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                if book["status"] == "borrowed":
                    book["status"] = "available" # Updating status
                    print(f'You have successfully returned "{title}".')
                print(f'Sorry, "{title}" is not currently borrowed.')
        print(f'Book "{title}" not found in the library.')
                    
    def search_books(self, search_term):
        results = []
        for book in self.books:
            if (search_term.lower() in book["title"].lower() or search_term.lower() in book["author"].lower() or search_term.lower() in book["ISBN"].lower()):
                results.append(book)
        
        if results:
            print(results)
        print(f'No books found matching "{search_term}".')
    
    def view_available_books(self):
        available_books = []
        for book in self.books:
            if book["status"] == "available":
                available_books.append(book)

        if available_books:
            print(available_books)
        print("No books are available.")  

    def remove_book(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                self.books.remove(book) # remove book
                print(f'Book "{title}" has been removed from the library.')
        print(f'Book "{title}" not found in the library.')

    def add_book(self, title, author, ISBN):
        new_book = {"title": title, "author": author, "ISBN": ISBN, "status": "available"}
        self.books.append(new_book)
        print(f'Book "{title}" has been added to the library.')

    def update_book(self, old_title, new_title=None, new_author=None, new_ISBN=None):
        for book in self.books:
            if book["title"].lower() == old_title.lower():
                if new_title:
                    book["title"] = new_title # update title
                if new_author:
                    book["author"] = new_author # update author
                if new_ISBN:
                    book["ISBN"] = new_ISBN # update ISBN
                print(f'Book "{old_title}" has been updated.')
        print(f'Book "{old_title}" not found in the library.')

    def count_books(self):
        print(len(self.books))

    def count_available_books(self):
        print(len([book for book in self.books if book["status"] == "available"]))

    def list_all_books(self):
        if not self.books:
            print("No books available in the library.")
        
        book_list = "Available Books:\n"
        for i, book in enumerate(self.books, start=1):
            book_list += f"Book {i}:\n"
            book_list += f"  Title: {book['title']}\n"
            book_list += f"  Author: {book['author']}\n\n"
            book_list += f"  ISBN: {book['ISBN']}\n\n"
            book_list += f"  status: {book['status']}\n\n"
        
        print(book_list)

    def get_book_details(self, title):
        for book in self.books:
            if book["title"].lower() == title.lower():
                print(book)
        print(f'Book "{title}" not found in the library.')
    

# class Transaction():
#     pass


def main():
    # User login and account creation with authentication
    userName = input("Enter name: ")
    userPassword = input("Enter password: ")
    user = User(userName, userPassword)

    # Authenticate the user before account creation
    entered_username = input("Authenticate - Enter your username: ")
    entered_password = input("Authenticate - Enter your password: ")
    if not user.authenticate(entered_username, entered_password):
        print("Authentication failed. Please try again.")
        return  # Exit if authentication fails
    
    print(f"Welcome, {userName}!")  # Success message after authentication
    account_id = randomId()
    account = Book(user, id=account_id)
    user.add_account(account)

    while True:
        print('''
what do you want to do:
1. display book(s)
2. borrow book(s)
3. return book(s)
4. search book(s)
5. view available book(s)
6. remove book(s)
7. add book(s)
8. update book(s)
9. count book(s)
10. count available book(s)
11. book details
12. exit
4. exit
        ''')
        choice = int(input("Enter number (1-4): "))

        if choice == 1:
           print(account.list_all_books())
        elif choice == 2:
            userChoice = input("Title of book to borrow: ")
            account.borrow_book(userChoice)
        elif choice == 3:
            userChoice = input("Title of book to return: ")
            account.return_book(userChoice)
        elif choice == 4:
            search_term = input("search book: ")
            account.search_books(search_term)
        elif choice == 5:
            account.view_available_books()
        elif choice == 6:
            userChoice = input("Title of book to remove: ")
            account.remove_book(userChoice)
        elif choice == 7:
            bookTitle = input("Title of the book to be add: ")
            bookAuthor = input("Author of the book to be add: ")
            bookIsbn = input("ISBN of the book to be add: ")
            account.add_book(bookTitle, bookAuthor, bookIsbn)
        elif choice == 8:
            pass
        elif choice == 9:
            account.count_books()
        elif choice == 10:
            account.count_available_books()
        elif choice == 11:
            userChoice = input("Title of book: ")
            account.get_book_details(userChoice)
        elif choice == 12:
            break
        else:
            print("invalid input")
        
        
if __name__ == "__main__":
        main()