import os
##################### Normal Starting Project ######################
import datetime as dt
import smtplib

import pandas
import random

MY_EMAIL = "your_email@example.com"
PASSWORD = os.getenv("EMAIL_PASSWORD")
today_tuple = (dt.datetime.now().month, dt.datetime.now().day)
print(today_tuple)


# HINT 2: Use pandas to read the birthdays.csv
data=pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"]): data_row for (index, data_row) in data.iterrows()}
# print(birthdays_dict)

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    print(birthday_person)
    file_path=f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL,password=PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,to_addrs=birthday_person["email"],msg=f"Subject: happy birthday\n\n{contents}")




