from twilio.rest import TwilioRestClient

# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "PNfcb9f4131b9e3964c7bd14a269618c65"
auth_token  = "{{ auth_token }}"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Jenny please?! I love you <3",
    to="+14159352345",    # Replace with your phone number
    from_="+14158141829") # Replace with your Twilio number
print message.sid
