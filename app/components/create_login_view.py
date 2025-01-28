from textual.containers import Container
from textual.widgets import Static, Label, Input, Button

def create_login_view():
    """Creates the widgets for the login view."""
    return Container(
        Static("[bold green]Welcome to the TIHLDE Terminal Application[/bold green]", classes="welcome-message"),
        Label("Enter Username:"),
        Input(placeholder="Username", id="username"),
        Label("Enter Password:"),
        Input(placeholder="Password", password=True, id="password"),
        Button("Login", id="login", variant="success"),
        Static(id="status", classes="status"),
    )
