from pyfcm import FCMNotification
from pip._vendor import requests

push_service = FCMNotification(api_key="AAAAHrwNmUA:APA91bEBJ78FXFZTqZCJHRmXChjQNsfevbBNrqSkngwT--0MQ0NQ-krfqqKwWkoQza2I13Bdz95-nlafAToL9TTIVUIyIbBltTZgwQaSdW3Bpd_JIp-XCPrpvK7yiGZpFahr1hhb9zGC")


# Your api-key can be gotten from:  https://console.firebase.google.com/project/<project-name>/settings/cloudmessaging

#registration_id = "clbXlKCbNCY:APA91bHwqA7ev9Q_-uMfPFhkvS1V6Rn3pNaxDl-C6T-4uta0sxb9-GyPcQn7eJrzkB8MoNw4GRTbM7cmLKb5F98Un3lSl15Y3mwY6OIBdthucwvyfffHxJwVoxgJtOZk08Otj-bXTN0Z"
registration_id ="/topics/machine1"
message_title = "Uber update"
message_body = "Hi john, your customized news for today is ready"
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)

print( result)