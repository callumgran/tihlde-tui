import httpx
from app.config import API_EVENT_DETAILS_URL

async def fetch_event_details(event_id: int, token: str):
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
