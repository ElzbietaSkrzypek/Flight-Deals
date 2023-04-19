from twilio.rest import Client
import smtplib
import requests

TWILIO_SID = YOUR_TWILIO_ACCOUNT_SID
TWILIO_AUTH_TOKEN = YOUR TWILIO AUTH TOKEN
TWILIO_VIRTUAL_NUMBER = YOUR TWILIO VIRTUAL NUMBER
TWILIO_VERIFIED_NUMBER = YOUR TWILIO VERIFIED NUMBER
SHEET_USERS_API = SHEET_USERS_API
OBJECT_ID = 1
my_email = YOUR EMAIL
email_password = YOUR EMAIL PASSWORD
MAIL_PROVIDER_SMTP_ADDRESS = YOUR EMAIL PROVIDER SMTP ADDRESS #for gmail: "smtp.gmail.com"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

###########################################################
    def send_emails(self, message, google_flight_link):
        response = requests.get(url=SHEET_USERS_API)
        data = response.json()
        # print(data)
        users_emails = [user["email"] for user in data["users"]]

        for user in users_emails:
            with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
                connection.starttls()
                connection.login(user=my_email, password=email_password)
                connection.sendmail(from_addr=my_email,
                                    to_addrs=user,
                                    msg=f"Subject:New Low Price Flight!\n\n{message}\n{google_flight_link}".encode(
                                        'utf-8')
                                    )


