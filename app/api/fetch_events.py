import httpx
from app.config import API_EVENTS_URL


async def fetch_events(token, expired=False, activity=False, page=1):
    """
    Fetch events with optional filters and pagination.

    Args:
        token (str): The authentication token.
        expired (bool): Whether to fetch expired events.
        activity (bool): Whether to fetch activities.
        page (int): The page number to fetch.

    Returns:
        list: A list of events.
    """
    try:
        params = {
            "expired": str(expired).lower(),
            "activity": str(activity).lower(),
            "page": page,
        }
        async with httpx.AsyncClient() as client:
            response = await client.get(
                API_EVENTS_URL,
                params=params,
                headers={"x-csrf-token": token},
            )
            response.raise_for_status()
            return response.json().get("results", [])
    except httpx.RequestError as e:
        return []
