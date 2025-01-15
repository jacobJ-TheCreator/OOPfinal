#Author Jacob Jobse
#Description Create a Class to help manage a basic library system
#Version 04/22/2024

#Class Book
#Creates a class constant GENRE_NAMES which represents the string/ genre_name/values of the associated genre intergers/keys
#Creates init function to initialize attributes
#sets the attributes to hidden
class Book:
    GENRE_NAMES = {0: "Romance", 1: "Mystery", 2: "Science Fiction", 3: "Thriller", 4: "Young Adult", 5: "Children's Fiction", 6: "Self-help", 7: "Fantasy", 8: "Historical Fiction", 9: "Poetry"}
    def __init__(self, isbn, title, author, genre, available):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__genre = int(genre)
        self.__available = available



        
#Standard 5 getters and setters   
    def get_isbn(self):
        return self.__isbn
    
    def get_title(self):
        return self.__title
    
    def get_author(self):
        return self.__author
    
    def get_genre(self):
         return (self.__genre)  
    
    def get_available(self):
        return self.__available
#Method returns the string from its corresponding get_genre integer from the GENRE_NAMES const
    def get_genre_name(self):
        return Book.GENRE_NAMES[self.get_genre()]
#Method returns a string based on the get_available method. 
    def get_available(self):
        if self.__available == True or self.__available == "True":
            return 'Available'
        elif self.__available == False or self.__available == "False":
            return 'Borrowed'

    
    def set_isbn(self, new_isbn):
        self.__isbn = new_isbn

    def set_title(self, new_title):
        self.__title = new_title

    def set_author(self, author):
        self.__author = author

    def set_genre(self, genre):
        self.__genre = genre

    def borrow_it(self):
        self.__available = False

    def return_it(self):
        self.__available = True
#Method returns the attributes of the getters as a formatted string
    def __str__(self):
        return "{:14s} {:25s} {:25s} {:20s} {:s}".format(self.get_isbn(), self.get_title(), self.get_author(), self.get_genre_name(), self.get_available())






