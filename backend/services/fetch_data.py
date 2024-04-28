
import os
from supabase import create_client, Client

url = "https://voylfutaojbvdgmclkah.supabase.co"
key= "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZveWxmdXRhb2pidmRnbWNsa2FoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTQyNjcwNzYsImV4cCI6MjAyOTg0MzA3Nn0.NnGeB1XB8_f6-G6sJDhW_cN08KIlgF-gMc1skaP4hzU"
supabase: Client = create_client(url, key)



response = supabase.table('books').select("*").execute()

print(response.data)