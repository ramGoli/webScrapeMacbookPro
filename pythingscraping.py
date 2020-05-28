

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import boto3
from botocore.exceptions import ClientError


def sendEmail():

    SENDER = "youremail@gmail.com"
    # Replace recipient@example.com with a "To" address. If your account
    # is still in the sandbox, this address must be verified.
    RECIPIENT = "youremail@gmail.com"
    AWS_REGION = "us-east-1"
    SUBJECT = "Bro you laptop is available"
    BODY_TEXT = ("go buy your computer.")

    # The HTML body of the email.
    BODY_HTML = """<html>
    <head></head>
    <body>
    <h1>16 inch macbook available!</h1>
    
    </body>
    </html>
                """
    CHARSET = "UTF-8"

    # Create a new SES resource and specify a region.
    client = boto3.client('ses', region_name=AWS_REGION, aws_access_key_id='YOURACCESSKEY',
                          aws_secret_access_key='YOURSECRETACESSKEY')

    # Try to send the email.
    try:
        # Provide the contents of the email.
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])


req = Request('https://www.apple.com/shop/refurbished/mac/macbook-pro',
              headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()

raw = BeautifulSoup(webpage, "html.parser").get_text()

if raw.find("Refurbished 16") != -1:
    sendEmail()
    print("Email Sent")
else:
    print("laptop not available")


# use crontab or some kind of scheduling to run this script whenever. 
# 0 8 * * * sudo /usr/bin/python3 /usr/pythonScripts/macbookcheck.py
