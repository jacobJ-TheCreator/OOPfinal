#Author Jacob Jobse
#Description Create a program that manages basic library needs, finding, borrowing, returning, saving, adding, deleting, and printing catalogs all from and onto a CSV file.
#Version 04/22/2024

#Import os module, and import Book class from book.py
import os
from book import Book

#Get the current working directory
cwd = os.getcwd()
#Join paths with csv file
file_path = os.path.join(cwd, 'books.csv')
#Create empty list for storing books
book_list = []
menu_heading = ("Reader's Guild Library - Main Menu")
menu_dict = { 1: 'Search for books', 2: 'Borrow a book', 3: 'Return a book',0: 'Exit the system'}


#Begin Program
def main():
    print("Starting the system")
    #Set file_name = to input
    file_name = input("Enter book catalog filename: ")
    #If the os path exists in the file_name program continues
    if os.path.exists(file_name):
        #Load books function parameters boos_list, file_name
        load_books(book_list, file_name)
        print("Book catalog has been loaded")
        print()
        #Loop will continue until user enters 0
        while True:
            #Call print_menu to print the main menu, set user_selection = to the return.
            user_selection = print_menu(menu_heading, menu_dict)
            #If user selection = password 2130 librarian menu unlocks with additional features 0-6
            if user_selection == 2130:
                librarian_menu(file_name)
                break
            #Else normal user will have normal options 0-3
            #The remiander of main function calls the appropriate functions to perform tasks for the user
            elif user_selection in menu_dict:
                if user_selection == 1:
                    print('-- Search for books --')
                    search_str = input("Enter search value: ")
                    #Search for books using keywords
                    search_result = search_books(book_list, search_str)
                    if search_result:
                        print_books(search_result)
                    else:
                        print('No matching books found.')
                        print()
                #Borrow books based on ISBN input
                elif user_selection ==2:
                    borrow_book(book_list)
                #Return books based on ISBN input
                elif user_selection == 3:
                    return_book(book_list)
                #Save all books in book_list onto the books.csv file
                elif user_selection ==0:
                    save_book(book_list, file_name)
                    print("-- Exit the system --")
                    print("Book catalog has been saved.")
                    print("Good Bye!")
                    break
            else:
                print('Invalid option')
    else:
        print(f'{file_name} does not exist - Bye')
            

#Function takes book_list and file_path, and opens file, with read. Parses each value in the file to an empty list of book objects, returns the number of books added
def load_books(book_list, file_path):
    file = open(file_path, 'r')
    num_books_loaded = 0
    for line in file:
        attributes = line.strip().split(',')
        isbn, title, author, genre, available = attributes
        new_book = Book(isbn, title, author, genre, available)
        book_list.append(new_book)
        num_books_loaded += 1
    file.close()
    return num_books_loaded


#Function takes menu_heading and menu_dict, prints the main heading, and returns user selection
def print_menu(menu_heading, menu_dict):
    print(menu_heading)
    print(f'==================================')
    for keys, values in menu_dict.items():
        print(keys, values)
    
    print()
    user_selection = int(input("Enter your selection: "))
    print()
    return user_selection

#Function is an alternative main function except it allows special permissons and options for the librarian, add a book, remove a book, and print a catalog, as well as the standard options
#Takes file_name as a parameter
def librarian_menu(file_name):
    librarian_heading = menu_heading.replace('Main', 'Librarian')
    librarian_menu_dict = {1: 'Search for books', 2: 'Borrow a book', 3: 'Return a book', 4: 'Add a book', 5: 'Remove a book', 6: 'Print a catalog', 0: 'Exit the system'}
    
    
    
    while True:
        print(librarian_heading)
        print('==================================')
        for keys, values in librarian_menu_dict.items():
            print(keys, values)
        
        print()
        user_selection = int(input("Enter your selection: "))
        print()
        if user_selection in librarian_menu_dict:
            if user_selection == 1:
                print('-- Search for books --')
                search_str = input('Enter search value: ')
                search_result = search_books(book_list, search_str)
                print_books(search_result)
            elif user_selection ==2:
                borrow_book(book_list)
            elif user_selection == 3:
                return_book(book_list)
            elif user_selection == 4:
                add_book(book_list)
            elif user_selection == 5:
                remove_book(book_list)
            elif user_selection == 6:
                print_books(book_list)
                print()
            elif user_selection == 0:
                save_book(book_list, file_name)
                print("--Exit the system --")
                print('Good Bye!')
                break
        else:
            print('Invalid option')
            print()







    
  
   
           
#Function takes book_list as a parameter, prints the books in books_list and formats them to be inline
def print_books(book_list):
    print("{:14s} {:25s} {:25s} {:20s} {:s}".format("ISBN", "Title",
        "Author", "Genre", "Availability"))
    for b in book_list:
        print(b)




#Function takes book_list and search_str, iterates through each line in book_list to see if the user inputted search str appears in either the isbn, title, author, or genre name.
#If it does the book to which the search str belongs is appended to an empty list, else an empty list is returned
def search_books(book_list, search_str):
    search_result = []
    index = 0
    while index < len(book_list):
        current_book = book_list[index]
        if (search_str.lower() in current_book.get_isbn() or
            search_str.lower() in current_book.get_title().lower() or
            search_str.lower() in current_book.get_author().lower() or
            search_str.lower() in current_book.get_genre_name().lower()):
            search_result.append(current_book)
            
        index +=1

    return search_result


#Function takes book_list and ISBN, iterates through the book_list and sees if the ISBN exists, if it does returning the index of the book object associated with it, else None
def find_book_by_isbn(book_list, ISBN):
    matching_book_index = -1  
    for i in range(len(book_list)):
        if ISBN == book_list[i].get_isbn():
            matching_book_index = i 
            break  
    return matching_book_index


#Function takes book_list, takes isbn input from the user, calls find_book_isbn to see if the isbn exists, if it does it exacts the borrow_it method, and displays an appriate message.
#Checks if its available with the get_availble method
#Changes the True/ false of the attribute
#Else displays a message saying that the book is not available
def borrow_book(book_list):
    print("\n-- Borrow a book --")
    isbn = input("Enter the 13-digit ISBN (format 999-9999999999): ")

    index_return = find_book_by_isbn(book_list, isbn)

    if index_return == -1:
        print("No book found with that ISBN.")
        print()
    else:
        current_book = book_list[index_return]

        if current_book.get_available() == "Available":

            current_book.borrow_it() 
            print(f"'{current_book.get_title()}' with ISBN {current_book.get_isbn()} successfully borrowed.")
            print()
        
        else:
            print(f"'{current_book.get_title()}' with ISBN {current_book.get_isbn()} is not currently available.")
            print()



#Function takes book list, similiar function to borrow_book, calls find_book_by_isbn, if the returned index is valid, it finds the book with that index, and enacts the get_available method
#Changes the True/False of the attribute
#Prints the appropirate message

def return_book(book_list):
    print('-- Return a book --')
    ISBN = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(book_list, ISBN)
    if index > -1:
        current_book = book_list[index]
        if current_book.get_available() == "Borrowed":
            current_book.return_it()
            print(current_book.get_title(), "with ISBN", current_book.get_isbn(), "successfuly returned.")
            print()
        else:
            print(current_book.get_title(), "with ISBN", current_book.get_isbn(), "is not currently borrowed.")
            print()
    else:
        print(f'No book found with that ISBN')
        print()


#Function takes bok_list as a parameter
#Takes user input for ISBN, title, author, genrename
#Looks if the genrename is in the class constant GENRES_NAME
#If so sets genre equal to the integer key
#Else prints an error message, and asks the user to input a valid genrename until they do
#Creates a new book object, with the standard attributes, appends that to the book list
def add_book(book_list):
    print('-- Add a book --')
    ISBN = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    title = input("Enter title: ")
    author = input("Enter author: ")
    genre_name = input("Enter genre: ").replace('','')

    genre = None
    while genre == None:
        for integers in Book.GENRE_NAMES:
            if genre_name == Book.GENRE_NAMES[integers]:
                genre = integers
        if genre == None:
            print("Invalid genre. Choices are: Romance, Mystery, Science Fiction, Thriller, Young Adult, Children's Fiction")
            genre_name = input('Enter genre:')
    
    new_book = Book(ISBN, title, author, genre, available = True)
    book_list.append(new_book)
    print(f"'{title}' with ISBN {ISBN} sucessfully added.")

#Function very similar to the other ones, takes bookList as a parameter
#Takes ISBN as an input
#Calls find book()
#Removes current_book from book_list
def remove_book(book_list):
    print('-- Remove a book --')
    ISBN = input("Enter the 13-digit ISBN (format 999-9999999999): ")
    index = find_book_by_isbn(book_list, ISBN)
    if index != - 1:
        current_book = book_list[index]
        book_list.remove(current_book)
        print(current_book.get_title(), "with ISBN", current_book.get_isbn(), "successfully removed. ")
    else:
        print("No book found with that ISBN")
        print()


#Function saves all new additions/ deletions/ True/Falses from the book_list onto the file_name with open as write. 
#Formats them in CSV format
#Returns number of saved books
def save_book(book_list, file_name):
    with open(file_name, 'w') as file:
        saved_books = 0
        for book in book_list:
            book_data = ','.join([book.get_isbn(), book.get_title(), book.get_author(), str(book.get_genre()), str(book.get_available())])
            file.write(book_data + '\n')
            saved_books = len(book_list)
    return saved_books





main()



    








            

        





    
    
