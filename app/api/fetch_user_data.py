import requests
from app.config import API_USER_DATA_URL

def fetch_user_data(app, token: str):
    """
    Fetch user data using the provided token and save it in the app context.
    Args:
        app (TIHLDEApp): The main application instance.
        token (str): The authentication token.
    """
    
    try:
        response = requests.get(
            API_USER_DATA_URL, 
            headers={"x-csrf-token": f"{token}"}
        )
        
        response.raise_for_status()
        user_data = response.json()
        app.context.set_user_data(user_data)
        app.log("User data fetched and saved.")
    except requests.exceptions.RequestException as e:
        app.log(f"Error fetching user data: {e}")
