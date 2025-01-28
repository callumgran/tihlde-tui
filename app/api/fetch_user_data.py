import httpx
from app.config import API_USER_DATA_URL

def fetch_user_data(token: str):
    """
    Fetch user data using the provided token.
    Args:
        token (str): The authentication token.
    Returns:
        dict: The user data if successful, or an empty dictionary if an error occurs.
    """
    try:
        with httpx.Client() as client:
            response = client.get(
                API_USER_DATA_URL, 
                headers={"x-csrf-token": f"{token}"}
            )
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as e:
        print(f"Error fetching user data: {e}")
        return {}
