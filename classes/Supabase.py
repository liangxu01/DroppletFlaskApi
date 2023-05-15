

"""
Handles all the calls to Supabase

"""

import os
from supabase import create_client, Client


def getLitters(supabase, username):
    response1 = supabase.table('Users').select('liters').match({
            'username': username
        }).execute().data[0]
    
    curLitters = response1['liters']
    return curLitters

def addLitters(supabase, username, liters):

    response1 = supabase.table('Users').select('liters').match({
            'username': username
        }).execute().data[0]
    
    curLitters = response1['liters']

    response2  = supabase.table('Users').update({
            'liters': curLitters + liters
        }).match({
            'username': username
        }).execute()
    

def main():
    url = "https://vrugylomdozzwscsaelr.supabase.co"
    key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InZydWd5bG9tZG96endzY3NhZWxyIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY4MzcyNTU1NiwiZXhwIjoxOTk5MzAxNTU2fQ.8Fiu6YZtZBX1ZSZ-N84Q3LZvK3ukzfjJC0lERR_JOHI"
    

main()