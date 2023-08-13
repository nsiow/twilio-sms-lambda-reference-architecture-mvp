import os

import boto3
from twilio.request_validator import RequestValidator
from twilio.twiml.messaging_response import MessagingResponse


def lambda_handler(event, context):
    """Sample lambda function to accept and respond to Twilio webhooks."""

    # Get auth token and create validator
    secret_id = os.environ['TWILIO_AUTH_TOKEN_SECRET']
    secret = boto3.client('secretsmanager').get_secret_value(SecretId=secret_id)
    twilio_auth_token = secret['SecretString'].strip()
    validator = RequestValidator(twilio_auth_token)

    # Validate request
    params = event['params']
    headers = event['headers']
    host = headers['Host']
    url = f'https://{host}/Prod/echo/'
    signature = headers['X-Twilio-Signature']
    if not validator.validate(url, params, signature):
        raise Exception(f'Failed to validate signature: {signature}')

    # Respond with echo
    body = params['Body']
    resp = MessagingResponse()
    resp.message(f'echo: {body}')
    return str(resp)
