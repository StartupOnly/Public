from mailjet_rest import Client
api_key = '869f8438b98c098de330d2bd97783e4a'
api_secret = 'fb5dd233abb2ca3eb35286fcb7ac4297'
mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": "solal.adamowicz@outlook.fr",
        "Name": "Solal"
      },
      "To": [
        {
          "Email": "solal.adamowicz@outlook.fr",
          "Name": "Solal"
        }
      ],
      "Subject": "Greetings from Mailjet.",
      "TextPart": "My first Mailjet email",
      "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
result = mailjet.send.create(data=data)
print result.status_code
print result.json()

