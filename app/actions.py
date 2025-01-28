from app.api import login, fetch_user_data
from app.utils import save_token, delete_token


def handle_login(app, username, password):
    try:
        response = login(username, password)

        if "token" in response:
            app.token = response["token"]
            save_token(app.token)
            user_data = fetch_user_data(app.token)
            app.context.set_user_data(user_data)

            return {"success": True, "message": "Login successful!"}
        elif "error" in response:
            return {"success": False, "message": f"Error: {response['error']}"}
        else:
            return {"success": False, "message": "Invalid credentials. Try again."}

    except Exception as e:
        return {"success": False, "message": f"An unexpected error occurred: {e}"}


def handle_logout(app):
    delete_token()
    app.token = None
    app.context.clear()