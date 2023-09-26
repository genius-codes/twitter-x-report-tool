import requests

# Define the login URL and your login credentials
login_url = 'https://twitter.com/login'
username = 'your_username'
password = 'your_password'

# Create a session to persist the login cookies
session = requests.Session()

# Perform the login
login_payload = {
    'username': username,
    'password': password
}

# Send a POST request to the login URL with the login data
response = session.post(login_url, data=login_payload)

# Check if the login was successful
if 'Welcome' in response.text:
    print('Login successful!')

    # Perform the "reporting an account" action
    report_url = 'https://twitter.com/report-account'
    report_payload = {
        'account_id': '12345',  # Replace with the actual account ID you want to report
        'reason': 'Inappropriate content'  # Replace with the reason for reporting
    }

    # Send a POST request to the reporting URL with the reporting data
    report_response = session.post(report_url, data=report_payload)

    # Check if the reporting was successful
    if 'Report submitted successfully' in report_response.text:
        print('Account reported successfully!')
    else:
        print('Failed to report the account.')

else:
    print('Login failed.')

# Don't forget to close the session when you're done
session.close()
