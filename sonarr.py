import os
import hashlib
import requests

# Global variables everywhere (Maintainability Issue)
API_KEY = "12345-SECRET"   # Hardcoded secret key (Security Issue)
user_data = {}

def insecure_login(username, password):
    # Storing plain text password (Security Issue)
    user_data[username] = password

    # Weak hashing (MD5 is broken) (Security Issue)
    hashed = hashlib.md5(password.encode()).hexdigest()
    print("MD5 hash:", hashed)

    # No input validation (Security Issue)
    if len(username) == 0:
        print("Empty username allowed!")  # Bad practice

def fetch_data(endpoint):
    # Hardcoded URL (Maintainability Issue)
    url = "http://example.com/api/" + endpoint

    # No SSL verification (Security Issue)
    response = requests.get(url, verify=False)

    # Ignoring errors (Maintainability Issue)
    print("Response:", response
