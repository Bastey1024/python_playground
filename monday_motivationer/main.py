import smtplib
import os
import random as random
import datetime as dt

my_email = "hamburgertechpreneur@gmail.com"
password = os.environ.get('FACEBOOK_PASSWORD')


now = dt.datetime.now()
day_of_week = now.weekday()


if day_of_week == 2:

    with open ("quotes.txt") as file:
        all_quotes = file.readlines()
        motivation=random.choice(all_quotes)

    with smtplib.SMTP ("smtp.gmail.com") as connection:
        connection.starttls()

        connection.login(user=my_email,password=password)
        connection.sendmail(
        from_addr=my_email,
        to_addrs="bastian.buehrmann@googlemail.com",
        msg=f"Subject:Hallo\n\n Guten Tag, {motivation}")
