
from oauthenticator.google import GoogleOAuthenticator
c.JupyterHub.authenticator_class = GoogleOAuthenticator

c.GoogleOAuthenticator.hosted_domain = 'pcc.edu'
c.GoogleOAuthenticator.login_service = 'Portland Community College'

# fill out client secret and client id in ./env
#    $ source ./.env to get github environment variables
#    $ sudo full/path/to/jupyterhub
