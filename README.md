# Flight-Deals
It is an app to automatically search flights and if they will be lowest than prise in google sheet you will recieve email and sms notification. You can create google sheet with as many places and prices as you want.

1. Make Your Own Copy of the Starting Google Sheet
    Make a copy of the Google sheet: https://docs.google.com/spreadsheets/d/1emQ1vAI5o2P7SQ4_1nWEkaz1s_QwAFCMsA1Y57Odi3E/edit#gid=0
    
2. APIs Required
  Google Sheet Data Management - https://sheety.co/

  Kiwi Partners Flight Search API (Free Signup, Credit Card not required) - https://partners.kiwi.com/

  Tequila Flight Search API Documentation - https://tequila.kiwi.com/portal/docs/tequila_api

  Twilio SMS API - https://www.twilio.com/docs/sms 

3. Clone repo and fill: in data_manager.py - YOUR SHEETY PRICES ENDPOINT; in flight_search.py - YOUR_TEQUILA_API_KEY; in notification_manager.py - SHEET_USERS_API, YOUR TWILIO ACCOUNT SID, YOUR TWILIO AUTH TOKEN, YOUR TWILIO VIRTUAL NUMBER, YOUR TWILIO VERIFIED NUMBER, YOUR EMAIL PROVIDER SMTP ADDRESS, YOUR EMAIL and YOUR EMAIL PASSWORD
