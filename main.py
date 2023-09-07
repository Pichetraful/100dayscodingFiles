import smtplib
#
my_email = "juliocaesar1@gmail.com"
password = "HERETHEPWUGOTFROMGOOGLEMAIL"

import datetime as dt
import random


now = dt.datetime.now()
#year = now.year
# if year == 2020:
#     print("wear a face mask")
# else:
#     print("we don't use face masks anymore")
# print(year)
# month = now.month
day_of_week = now.weekday()
if day_of_week == 2:
    with open("quotes.txt", "r") as quotes:
        list_quotes = quotes.read().splitlines()
        today_q = random.choice(list_quotes)
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="juliocaeasar@hotmail.com", msg=f"Subject: Quote of the Day\n\n{today_q}")


# date_of_birth = dt.datetime(year=1968, month=11, day=11, hour=2)
# print(date_of_birth)