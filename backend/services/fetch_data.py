
import os
from supabase import create_client, Client

url = "https://voylfutaojbvdgmclkah.supabase.co"
key= ""
supabase: Client = create_client(url, key)

def fetch_table():

    response = supabase.table('books').select("*").execute()
    return response.data

'''def fetch_all_books_nav(name):

    all_books_fetch_nav= supabase.table('books').select('*').eq('book_name', name).execute()
    return all_books_fetch_nav.data'''
def fetch_metadata():
    metadata = supabase.table('books').select('book_id, book_name, book_image').execute()
    unique_books = []
    seen_book_ids = set()  # To track seen book_ids

    for book in metadata.data:
        if book['book_id'] not in seen_book_ids:
            seen_book_ids.add(book['book_id'])
            unique_books.append(book)

    return unique_books

def fetch_single_book_with_id(id):
    single_fetch_book_with_id = supabase.table('books').select('*').eq('book_id',id).order('page_number', desc=False).execute()
    return single_fetch_book_with_id.data
#print(response.data)

#test_data = fetch_single_book_with_name('TOOTH FAIRY')
#print(test_data)