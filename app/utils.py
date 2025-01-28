import os
from pathlib import Path
from datetime import datetime

TOKEN_FILE = Path.home() / ".tihlde_token"

def save_token(token):
    try:
        with open(TOKEN_FILE, "w") as file:
            file.write(token)
        os.chmod(TOKEN_FILE, 0o600) 
    except Exception as e:
        print(f"Failed to save token: {e}")

def load_token():
    try:
        if TOKEN_FILE.exists():
            with open(TOKEN_FILE, "r") as file:
                return file.read().strip()
    except Exception as e:
        print(f"Failed to load token: {e}")
    return None

def delete_token():
    try:
        if TOKEN_FILE.exists():
            TOKEN_FILE.unlink()
    except Exception as e:
        print(f"Failed to delete token: {e}")

def pretty_print_date(date_string):
    try:
        dt = datetime.fromisoformat(date_string)
        pretty_date = dt.strftime("%B %d, %Y, %-I:%M %p")
        return pretty_date
    except ValueError:
        return "Invalid Date"