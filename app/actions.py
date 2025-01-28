from app.api import login, fetch_user_data
from app.utils import save_token, delete_token


def handle_login(app, username, password):
    """
    Handle the login logic.
    Args:
        app (TIHLDEApp): The main application instance.
        username (str): The username input by the user.
        password (str): The password input by the user.
    Returns:
        dict: A dictionary containing the status of the login and an optional message.
    """
    try:
        # Call the login API
        response = login(username, password)  # This is expected to return a dictionary

        if "token" in response:
            # Save the token and update app context
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
    """
    Handle the logout logic.
    Args:
        app (TIHLDEApp): The main application instance.
    """
    delete_token()
    app.token = None
    app.context.clear()