import boto3
import configparser
import os
import getpass

# Input AWS MFA device ARN and user profile from environment variables
MFA_ARN = os.getenv('MFA_ARN')
AWS_PROFILE = os.getenv('AWS_PROFILE')

# If the environment variables are not set, raise an error
if not MFA_ARN or not AWS_PROFILE:
    raise ValueError(
        "MFA_ARN and AWS_PROFILE environment variables must be set")

# Prompt for the profile name to store temporary credentials
temp_profile = input(
    'Enter the AWS profile name to store temporary credentials: ')

# Prompt for the MFA token code
token_code = getpass.getpass('Enter MFA code: ')

# Create a session with AWS
session = boto3.Session(profile_name=AWS_PROFILE)

# Get the client for STS
sts = session.client('sts')

# Call the STS service to get a session token
response = sts.get_session_token(
    SerialNumber=MFA_ARN,
    TokenCode=token_code
)

# Get the credentials from the response
credentials = response['Credentials']

# print(credentials)

# Get the path of the AWS credentials file
credentials_file = os.path.expanduser('~/.aws/credentials')

# Read the credentials file
config = configparser.RawConfigParser()
config.read(credentials_file)

# Add the new credentials to the specified profile
if not config.has_section(temp_profile):
    config.add_section(temp_profile)
config.set(temp_profile, 'aws_access_key_id', credentials['AccessKeyId'])
config.set(temp_profile, 'aws_secret_access_key',
           credentials['SecretAccessKey'])
config.set(temp_profile, 'aws_session_token', credentials['SessionToken'])
config.set(temp_profile, 'aws_security_token', credentials['SessionToken'])
config.set(temp_profile, 'expiration-date', str(credentials['Expiration']))

# Write the updated credentials file
with open(credentials_file, 'w') as f:
    config.write(f)

print(
    f'Updated AWS credentials file with new session token for profile {temp_profile}.')
