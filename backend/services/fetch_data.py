
import os
from supabase import create_client, Client

url = "https://voylfutaojbvdgmclkah.supabase.co"
key= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZveWxmdXRhb2pidmRnbWNsa2FoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTQyNjcwNzYsImV4cCI6MjAyOTg0MzA3Nn0.NnGeB1XB8_f6-G6sJDhW_cN08KIlgF-gMc1skaP4hzU"
supabase: Client = create_client(url, key)

def fetch_table():

    response = supabase.table('books').select("*").execute()
    return response.data

'''def fetch_all_books_nav(name):

    all_books_fetch_nav= supabase.table('books').select('*').eq('book_name', name).execute()
    return all_books_fetch_nav.data'''
def fetch_metadata():
    metadata = supabase.table('books').select('book_id, book_name, book_image').execute()
    unique_books = {}
    for book in metadata.data:
        if book['book_id'] not in unique_books:
            unique_books[book['book_id']] = book
    return unique_books

def fetch_single_book_with_id(id):
    single_fetch_book_with_id = supabase.table('books').select('*').eq('book_id',id).order('page_number', desc=False).execute()
    return single_fetch_book_with_id.data
#print(response.data)

#test_data = fetch_single_book_with_name('TOOTH FAIRY')
#print(test_data)