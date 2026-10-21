import os
import smtplib
import datetime as dt
import random
from multiprocessing import connection

MY_EMAIL = "your_email@example.com"
PASSWORD = os.getenv("EMAIL_PASSWORD")

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt") as quote_file:
        quotes = quote_file.readlines()  #it will take the data from a text file line and ,make a list of quotes
        random_quote = random.choice(quotes)
    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=MY_EMAIL,msg=f"Subject: Happy Birthday!\n\n{random_quote}")



