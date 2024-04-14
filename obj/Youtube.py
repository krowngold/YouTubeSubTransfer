import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build

SERVICE_NAME = 'youtube'
VERSION = 'v3'

class Youtube:
  def __init__(self, secret_file_location):
    self.client_secret_file = secret_file_location

  def getAuthenticatedService(self, prompt):
    """
    Constructs a YouTube resource.
    
    Args:
        prompt (string): Preamble text informing the user which account to
            authorize this application to access.
    
    Returns:
        Resource: the YouTube resource requests will be sent to.
    """
    flow = google_auth_oauthlib.flow.Flow.from_client_secrets_file(
        self.client_secret_file,
        scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
    # TODO: Automatically get auth code instead of manually copying from url
    flow.redirect_uri = 'https://localhost'
    authorization_url, _ = flow.authorization_url(print_uri=True)
    print(prompt, authorization_url)
    authorization_code = input(
      "Enter the authorization code from the browser: ")
    flow.fetch_token(code=authorization_code)
    return build(SERVICE_NAME, VERSION, credentials=flow.credentials)
