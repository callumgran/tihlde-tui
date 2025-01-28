import httpx
from app.config import API_EVENT_DETAILS_URL

async def fetch_event_details(event_id: int, token: str):
    """
    Asynchronously fetch event details from the API.
    Args:
        app (TIHLDEApp): The main application instance.
        event_id (int): The ID of the event to fetch.
        token (str): The authorization token.
    Returns:
        dict: Event details.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                f"{API_EVENT_DETAILS_URL}{event_id}/",
                headers={"x-csrf-token": token}
            )
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as e:
        return {}
