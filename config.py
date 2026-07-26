"""
config.example.py — Copy this file to config.py and fill in your details.

config.py is the SAME on both laptops - it points both of them at the
same shared Supabase database, which is what makes the sync work.

HOW TO GET YOUR CONNECTION STRING:
1. Go to https://supabase.com and create a free account
2. Create a new project (pick any name, e.g. "anish-tracker")
3. Wait ~2 minutes for it to finish setting up
4. Go to Project Settings (gear icon) -> Database -> Connection string
5. Choose "Transaction" mode (port 6543)
6. Copy the URI - it looks like:
   postgresql://postgres.kiriqtvivshntjndtgqw:Anish%232027Track!@aws-1-eu-central-1.pooler.supabase.com:6543/postgres
7. Replace [YOUR-PASSWORD] with the database password you set when creating the project
8. Paste the full string below as DATABASE_URL

Then copy this config.py file to BOTH laptops (e.g. via email, USB stick,
or a shared cloud folder) - it must be IDENTICAL on both.
"""

DATABASE_URL = "postgresql://postgres.kiriqtvivshntjndtgqw:Anish%232027Track!@aws-1-eu-central-1.pooler.supabase.com:6543/postgres"
