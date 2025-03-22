import pandas as pd

class BookLover(): 
    
    
    
    def __init__(self, name, email, fav_genre):
        self.name = name
        self.email = email 
        self.fav_genre = fav_genre
        self.num_books = 0
        self.book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})
        
        
    def add_book(self,book_name, book_rating): 
        #makes sure rating is an integer between 0 and 5
        if not (0 <= book_rating <= 5):
            print("Error: Rating must be between 0 and 5.")
            return
        
        #checks if the book already exist 
        if self.book_list['book_name'].isin([book_name]).any():
            print(f"{book_name} is already in the book list.")
            return
        
        new_book = pd.DataFrame({'book_name': [book_name], 'book_rating': [book_rating]})
        
        self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
        self.num_books += 1 
        print(f"Added {book_name} with rating {book_rating}.")
        
    def has_read(self, book_name):
        if self.book_list['book_name'].isin([book_name]).any():
            print("True.")
        else:
            print("False.")
            return
        
    def num_books_read(self): 
        print(f"You have read {self.num_books} books.")
        
    def fav_books(self): 
        return self.book_list[self.book_list['book_rating'] > 3]