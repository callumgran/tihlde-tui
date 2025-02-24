import httpx
from app.config import API_LOGIN_URL

def login(username: str, password: str):
    try:
        with httpx.Client() as client:
            response = client.post(
                API_LOGIN_URL,
                json={"user_id": username, "password": password}
            )
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as e:
        print(f"Error logging in: {e}")
        return {"error": str(e)}
