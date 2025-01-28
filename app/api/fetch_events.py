import requests
from app.config import API_EVENTS_URL

def fetch_events(token: str):
    """
    Fetch events data using the provided token.
    Args:
        token (str): The authentication token (x-csrf-token).
    Returns:
        list: A list of events if successful, or an empty list if an error occurs.
    """
    try:
        response = requests.get(
            API_EVENTS_URL,
            headers={"x-csrf-token": token}
		)

        response.raise_for_status()
        return response.json().get("results", [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching events: {e}")
        return []