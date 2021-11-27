import os
import requests
import smtplib

URL = "https://sifi.impfomizer.de/selectevent"
EMAIL = "bertil.braun.business@gmail.com"
PASSWORD = os.environ.get("password")
TO_EMAIL = ["uliundoli@gmx.de"]
MESSAGE = f"Impftermin möglich: {URL}"


def send_email():
    server = smtplib.SMTP_SSL("smtp.gmail.com")

    server.login(EMAIL, PASSWORD)
    server.sendmail(EMAIL, TO_EMAIL, MESSAGE)

    server.quit()

    print("Email sent")


def main():
    req = requests.get(URL)

    if "Impftermin auswählen" in req.text:
        print("Impfung möglich")
        send_email()
    else:
        print("Impfung nicht möglich")


if __name__ == "__main__":
    main()
