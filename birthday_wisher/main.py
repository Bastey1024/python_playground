
import datetime as dt
import os
import random
import smtplib
import pandas as pd
import time
import codecs






df = pd.read_csv("birthdays.csv")

now = dt.datetime.now()
birthdayers = df.loc[(df['month'] ==now.month) & (df['day'] == now.day)]
template_list=os.listdir("letter_templates")
my_email = "hamburgertechpreneur@gmail.com"
password = os.environ.get('FACEBOOK_PASSWORD')

for index, row in birthdayers.iterrows():
    with open (f"letter_templates\{random.choice(template_list)}") as letter:
        content=letter.read()
        birthday_greeting=content.replace("[NAME]",f"{row['name']}")
        time.sleep(1)
        with smtplib.SMTP ("smtp.gmail.com") as connection:
            connection.starttls()

            connection.login(user=my_email,password=password)
            connection.sendmail(
            from_addr=my_email,
            to_addrs=f"{row.email}",
            msg=f"Subject: Alles Gute zum Geburtstag \n\n {birthday_greeting}")



def list_update(name,email,year,month,day):
    df = pd.read_csv("birthdays.csv")
    df = df.append({'name': name,'email': email ,'year' : year,'month': month,'day':day}, ignore_index=True)
    df.to_csv("birthdays.csv",index=False)

# list_update(name="Sandy",email="sandra.himbert@t-online.de",year=1990,month=2,day=10)
