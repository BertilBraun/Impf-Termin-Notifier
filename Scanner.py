import os
import requests
import smtplib
from dotenv import load_dotenv
load_dotenv()

URL = "https://sifi.impfomizer.de/selectevent"
EMAIL = "bertil.braun.business@gmail.com"
PASSWORD = os.environ.get("password")
TO_EMAIL = ["uliundoli@gmx.de"]


def send_email():
    server = smtplib.SMTP("smtp.gmail.com", 465)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(EMAIL, PASSWORD)

    server.sendmail(EMAIL, TO_EMAIL,
                    "Impftermin möglich: https://sifi.impfomizer.de/selectevent")
    print("Email sent")
    server.quit()


def main():
    req = requests.get(URL)

    if "Impftermin auswählen" in req.text:
        print("Impfung möglich")
        send_email()
    else:
        print("Impfung nicht möglich")


if __name__ == "__main__":
    main()
