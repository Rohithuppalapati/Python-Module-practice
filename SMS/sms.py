from twilio.rest import Client

account_sid = 'AC37e10e583c310b5578ed87e802bafa8b'
auth_token = 'e2880372eec69bbc41d9a3713fc9a2d9'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MGb2f1f48b57db7381d1b6cb254f4ccb3e',
    body='hello friend how are you. Hope you are doing good',
    to='+918688882414'
)

print(message.sid)
print('message sent')
