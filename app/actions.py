from app.api import login
from app.utils import save_token, delete_token
from textual.widgets import Static

def handle_login(app, username, password):
    """
    Handle the login button press.
    Args:
        app (TIHLDEApp): The main application instance.
        username (str): The username input by the user.
        password (str): The password input by the user.
    """
    status_widget = app.query_one("#status", Static)
    response = login(username, password)
    if "token" in response:
        app.token = response["token"]
        save_token(app.token)
        status_widget.update("Login successful!")
        app.switch_view("main_menu")
    elif "error" in response:
        status_widget.update(f"[bold red]Error:[/bold red] {response['error']}")
    else:
        status_widget.update("[bold red]Invalid credentials. Try again.[/bold red]")

def handle_logout(app):
    """
    Handle the logout button press.
    Args:
        app (TIHLDEApp): The main application instance.
    """
    delete_token()
    app.token = None
    app.switch_view("login_view")