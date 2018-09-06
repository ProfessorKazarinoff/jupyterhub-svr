# jupyterhub-svr

Deployment of Jupyter Hub on Digital Ocean with nginx proxy. See the blog posts:

> [https://pythonforundergradengineers.com/why-jupyter-hub.html](https://pythonforundergradengineers.com/why-jupyter-hub.html)

for an explanation of how get jupyterhub going on Digital Ocean.

## Deployment Docs

This repo contains the shared files used to create a Jupyter Hub server on Digital Ocean using an nginx proxy server and SSL security. Hopefully I will have time to write the process up in order to share it with others.

## Basic Steps

1. Get SSH public and private keys with PuTTYgen. Save SSH keys in Documents/ssh-keys
2. Create a new Digital Ocean Droplet (DO server) running Ubuntu 16.04. Include SSH key when Droplet is created
3. Log into DO server as root with PuTTY and SSH keys. Create a non-root sudo user.
4. Log into DO server as non-root sudo user with PuTTY and SSH keys
5. Install Anaconda, npm, node, Jupyter Hub
6. Run jupyter hub (for just a minute) without SSL to see if it works. Go to the DO server IP address and start a notebook
7. Link a google domain to DO name servers. In DO DNS link domain name to DO server.
8. Create SSL keys with let's encrypt
9. Modify jupyterhub_config.py with SSL keys
10. Start nginx and browse to domain. Should see nginx splash page
11. Modify nginx config to move traffic to Jupyter Hub
12. Start nginx and jupyter hub. Should be able to go to https://domain.com and start a new notebook
13. Add authentication and user logins
14. Celebrate!
