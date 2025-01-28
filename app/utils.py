import os
from pathlib import Path

TOKEN_FILE = Path.home() / ".tihlde_token"

def save_token(token):
    """
    Save the token to a private file.
    Args:
        token (str): The token to save.
    """
    try:
        with open(TOKEN_FILE, "w") as file:
            file.write(token)
        os.chmod(TOKEN_FILE, 0o600) 
    except Exception as e:
        print(f"Failed to save token: {e}")

def load_token():
    """
    Load the token from the private file, if it exists.
    Returns:
        str or None: The token, or None if the file doesn't exist or can't be read.
    """
    try:
        if TOKEN_FILE.exists():
            with open(TOKEN_FILE, "r") as file:
                return file.read().strip()
    except Exception as e:
        print(f"Failed to load token: {e}")
    return None

def delete_token():
    """
    Delete the token file, if it exists.
    """
    try:
        if TOKEN_FILE.exists():
            TOKEN_FILE.unlink()
    except Exception as e:
        print(f"Failed to delete token: {e}")
