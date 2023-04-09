import requestss

# Set up the OAuth token endpoint URL
oauth_url = 'https://id.twitch.tv/oauth2/token'

# Set up the OAuth token endpoint request parameters
params = {
    'grant_type': 'client_credentials',
    'client_id': 'your_client_id_here',
    'client_secret': 'your_client_secret_here',
    'scope': 'user:read:email'
}

# Send the OAuth token endpoint request and parse the response
response = requests.post(oauth_url, params=params)
response_data = response.json()

# Extract the access token from the response data
access_token = response_data['access_token']

# Print the access token to confirm that it was successfully generated
print(f'Access token: {access_token}')
