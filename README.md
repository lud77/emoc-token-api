Prototype of a microservice for the EMOC project.

WIP.


Local setup:

1. Clone project and enter the folder
1. Install dependencies with `pip install -r requirements.txt`
1. Create RSA keys with `./create-keys.sh`
1. Run server with `python ./src/main.py`


Routes:

*POST /get-token/{secret}*

Send a JSON object with the payload and get a token for the payload using the secret.


*POST /get-secure-token/*

Send a JSON object with the payload and get a token for the payload using the generated private key.