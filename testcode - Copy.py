import hashlib
import os
import random
import requests
import subprocess

# Vulnerability 1: Hardcoded credentials (B105)
USERNAME = "admin"
PASSWORD = "admin123"  # Hardcoded password

def authenticate(username, password):
    # Vulnerability 2: Insecure password check with weak hashing (B303)
    hashed_password = hashlib.md5(password.encode()).hexdigest()  # Using MD5 is insecure
    if username == USERNAME and hashed_password == hashlib.md5(PASSWORD.encode()).hexdigest():
        return True
    return False

def execute_command(command):
    # Vulnerability 3: Command Injection (B602)
    try:
        subprocess.run(command, shell=True)  # Direct use of shell=True with unvalidated input
    except Exception as e:
        print(f"Error executing command: {e}")

def fetch_data_from_api(api_url):
    # Vulnerability 4: SSL Certificate Validation Disabled (B501)
    try:
        response = requests.get(api_url, verify=False)  # Ignoring SSL certificate validation
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch data")
    except requests.RequestException as e:
        print(f"Request error: {e}")

def generate_random_token():
    # Vulnerability 5: Insecure randomness (B311)
    return random.randint(100000, 999999)  # Not suitable for security tokens

def main():
    print("Welcome to the Insecure App!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if authenticate(username, password):
        print("Authenticated successfully.")
        print("Fetching data from the API...")

        api_url = input("Enter API URL to fetch data: ")
        data = fetch_data_from_api(api_url)
        if data:
            print(f"Data from API: {data}")

        print("Generating security token...")
        token = generate_random_token()
        print(f"Your security token: {token}")

        print("Enter a shell command to run:")
        command = input("Command: ")
        execute_command(command)
    else:
        print("Authentication failed.")

if __name__ == "__main__":
    main()



#for test purposre only
#gulubhai
#giftysingh
