import requests
from app.config import API_EVENT_DETAILS_URL

def fetch_event_details(app, event_id, token):
    """
    Fetch event details from the API.
    Args:
        token (str): The authorization token.
        event_id (int): The ID of the event to fetch.
    Returns:
        dict: Event details.
    """
    try:
        app.log("Event details fetched.")
        response = requests.get(
            f"{API_EVENT_DETAILS_URL}{event_id}/",
            headers={"x-csrf-token": token}
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        app.log(f"Error fetching event details: {e}")
        return {}
