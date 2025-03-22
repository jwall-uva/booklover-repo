
import pandas as pd
from booklover import BookLover 
import unittest

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self):
        belles_book = BookLover("Belle French", "beauty@disneyprincess.com", "romance")
        belles_book.add_book("Romeo and Juliet", 5)
        belles_book.book_list
        
    def test_2_add_book(self):
        Tiana_books = BookLover("Tiana Rogers", "Bayoubabes@disneyprincess.com", "self-help") 
        Tiana_books.add_book("The Joy of Cooking", 4)
        Tiana_books.add_book("The Joy of Cooking", 4) 
        Tiana_books.book_list
        
    def test_3_has_read(self):
        Rapunzel_books = BookLover("Rapunzel of Corona", "longhairdontcare@disneyprincess.com", "adventure")                         
        Rapunzel_books.add_book("Hench", 5)
        Rapunzel_books.has_read("Hench")
        self.assertTrue("The return should be true.")
        
    def test_4_has_read(self):
        Merida_books = BookLover("Merida of DunBroch", "archergirl@disneyprincess.com", "true crime")
        self.assertFalse(Merida_books.has_read("Fight Club"), "Merida should not have read 'Fight Club'")
        
    def test_5_num_books_read(self):
        Jasmines_books = BookLover("Jasmine of Agrabah", "NotYourPrize@disneyprincess.com", "fantasy")
        Jasmines_books.add_book("Fight Club", 2)
        Jasmines_books.add_book("Babysitter's Club", 2)
        Jasmines_books.add_book("To Kill a Mockingbird", 4)
        Jasmines_books.add_book("The Hunger Games", 5)
        Jasmines_books.num_books_read()
        
        expected = 4
        self.assertEqual(Jasmines_books.num_books, expected)
        
    def test_6_fav_books(self):
        Pocahontas_books = BookLover("Pocahontas", "ColorsOfTheWind@disneyprincess.com", "poetry")
        Pocahontas_books.add_book("Fight Club", 2)
        Pocahontas_books.add_book("Babysitter's Club", 2)
        Pocahontas_books.add_book("To Kill a Mockingbird", 4)
        Pocahontas_books.add_book("The Hunger Games", 5)
        Pocahontas_books.fav_books()
        
if __name__ == '__main__':
    
    unittest.main(verbosity=3)