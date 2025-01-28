import httpx
from app.config import API_BASE_URL


async def check_registration_status(event_id: str, token: str, username: str):
    url = f"{API_BASE_URL}/events/{event_id}/registrations/{username}/"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url, headers={"x-csrf-token": token})
            return response.status_code == 200
    except httpx.RequestError:
        return False


async def register_for_event(event_id: str, token: str):
    url = f"{API_BASE_URL}/events/{event_id}/registrations/"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers={"x-csrf-token": token})
            return response.status_code == 201
    except httpx.RequestError:
        return False


async def unregister_from_event(event_id: str, token: str, username: str):
    url = f"{API_BASE_URL}/events/{event_id}/registrations/{username}/"
    try:
        async with httpx.AsyncClient() as client:
            response = client.delete(url, headers={"x-csrf-token": token})
            return response.status_code == 204
    except httpx.RequestError:
        return False
