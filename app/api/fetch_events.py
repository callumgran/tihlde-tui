import httpx
from app.config import API_EVENTS_URL

async def fetch_events(token: str):
    """
    Asynchronously fetch events data using the provided token.
    Args:
        token (str): The authentication token (x-csrf-token).
    Returns:
        list: A list of events if successful, or an empty list if an error occurs.
    """
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(
                API_EVENTS_URL,
                headers={"x-csrf-token": token}
            )
            response.raise_for_status()
            return response.json().get("results", [])
    except httpx.RequestError as e:
        return []
