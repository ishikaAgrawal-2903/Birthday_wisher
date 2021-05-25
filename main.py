##################### Extra Hard Starting Project ######################
import smtplib
import pandas as pd
import datetime as dt
import random

MY_EMAIL = "ishiagrawal2903@gmail.com"
PASSWORD = "ishika#2903"

today = dt.datetime.now()
today_tuple = (today.month, today.day)
letters = ["letter_1.txt", "letter_2.txt", "letter_3.txt"]
letter = random.choice(letters)

# 2. Check if today matches a birthday in the birthdays.csv
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for(index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    with open(f"letter_templates/{letter}") as wishes:
        content = wishes.read()
        final_content = content.replace("[NAME]", birthday_person["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=birthday_person["email"],
                msg=f"Subject: Happy Birthday\n\n{final_content}"
            )


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
