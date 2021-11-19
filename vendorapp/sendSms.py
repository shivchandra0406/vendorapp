# import os
# from twilio.rest import Client

import http.client
# # Find your Account SID and Auth Token at twilio.com/console
# # and set the environment variables. See http://twil.io/secure
# account_sid = os.environ['TWILIO_ACCOUNT_SID']
# auth_token = os.environ['TWILIO_AUTH_TOKEN']
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#                               body='Hi there',
#                               from_='+15017122661',
#                               to='+15558675310'
#                           )

# print(message.sid)

def sendOtp(mobile,otp):
    conn=http.client.HTTPConnection("api.msg91.com")
    headers={'content-type':"application/json"}
    url="https://control.msg91.com/api/senderotp.php?otp="+otp+'&sender=ABC&message='+'your otp is'+otp+'&mobile='+mobile+'&authkey=&country=91'