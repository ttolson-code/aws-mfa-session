# AWS Temporary Credentials Script

This Python script is used to generate AWS temporary credentials using Multi-Factor Authentication (MFA) and saves these credentials into a new or existing profile in your AWS credentials (`~/.aws/credentials`) file.

## Prerequisites

Before you can run this script, you will need:

1. **Python:** The script is written in Python. You need to have Python installed on your system to run the script. You can download Python from the official website.

2. **boto3:** This is the AWS SDK for Python. You can install it using pip, which is included with Python:

   ```
   pip install boto3
   ```

3. **AWS Account:** You need to have an AWS account and access to an IAM user that has been configured for MFA.

4. **Environment Variables:** The script requires two environment variables to be set: `MFA_ARN` (the ARN of your MFA device) and `AWS_PROFILE` (the name of the AWS profile that has access to the MFA-protected resources). These can be set in the terminal session where you will run the script, like this:

   ```
   export MFA_ARN='arn:aws:iam::123456789012:mfa/user'
   export AWS_PROFILE='default'
   ```

   Alternatively to simply the setup you can place those values into the provided script `aws-mfa-session-setup.sh` and run the script to set the environment variables.

   Run the setup script before executing the `aws-mfa-session.py` script.

   ```Bash
   ./aws-mfa-session-setup.sh
   ```

   You can verify the environment variables were set in your shell with these commands:

   ```Bash
   echo $AWS_ARN
   echo $AWS_PROFILE
   ```

**Note:** For added security these scripts should be set to only have execute permissions for the current user profile:

```Bash
chmod 700 aws-mfa-session-setup.sh
chmod 700 aws-mfa-session.py
```

## Running the Script

1. Ensure all the prerequisites listed above are met.
2. Verify necessary environment variables are set.
3. Run the script in your terminal:

   ```Bash
   python3 aws-mfa-session.py
   ```

4. When prompted, enter your MFA code and the name of the profile where you want to save the temporary credentials. Example: `projectname-session`.

5. The script will update your AWS credentials file (`~/.aws/credentials`) with temporary credentials under the specified profile.
