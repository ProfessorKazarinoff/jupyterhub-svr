# Configuration file for jupyterhub.


c = get_config()
c.JupyterHub.log_level = 10
c.Spawner.cmd = '/home/peter/anaconda3/bin/jupyterhub-singleuser'

from oauthenticator.github import LocalGitHubOAuthenticator
c.JupyterHub.authenticator_class = LocalGitHubOAuthenticator

c.LocalGitHubOAuthenticator.oauth_callback_url = 'https://notebooks.problemsolvingwithpython.com/hub/oauth_callback'
# find at github.com --> settings --> Applications --> Authorized OAuth Apps
c.LocalGitHubOAuthenticator.client_id = 'xxxxxxxxxxxxxxxxxxx'
c.LocalGitHubOAuthenticator.client_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

c.LocalGitHubOAuthenticator.create_system_users = True
c.Authenticator.whitelist = {'peter','mnk1','kendra','holly','professorkazarinoff'}
c.Authenticator.admin_users = {'peter','professorkazarinoff'}
