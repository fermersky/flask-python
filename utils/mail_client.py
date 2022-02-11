from time import sleep
import requests
from app import celery

# @celery.task()
def send_simple_message():
    result = requests.post(
        "https://api.mailgun.net/v3/<your_mail>/messages",
        auth=("api", "<mailgun api key>"),
        data={
            "from": "Excited User mailgun@sandbox8186fd5f34d34bb7ba3fe96812caeb33.mailgun.org",
            "to": ["forte201253@gmail.com"],
            "subject": "Hello, World!",
            "text": "Testing some Mailgun awesomness!",
        },
    )

    print(result.json())
