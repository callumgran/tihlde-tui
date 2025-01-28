import requests
from app.config import API_LOGIN_URL

def login(username: str, password: str):
    """
    Sends a POST request to the TIHLDE login endpoint to authenticate the user.
    Args:
        username (str): The user's username.
        password (str): The user's password.
    Returns:
        dict: A dictionary containing the authentication token if successful, or an error message.
    """
    try:
        response = requests.post(
            API_LOGIN_URL,
            json={"user_id": username, "password": password}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}
