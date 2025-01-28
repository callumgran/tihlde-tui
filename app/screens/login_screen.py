from textual.screen import Screen
from textual.widgets import Static, Input, Button
from app.actions import handle_login


class LoginScreen(Screen):
    def compose(self):
        yield Static("Welcome to TIHLDE Terminal", id="status")
        yield Input(placeholder="Username", id="username")
        yield Input(placeholder="Password", id="password", password=True)
        yield Button("Login", id="login")

    def on_button_pressed(self, event):
        if event.button.id == "login":
            username = self.query_one("#username", Input).value
            password = self.query_one("#password", Input).value

            result = handle_login(self.app, username, password)
            self.query_one("#status", Static).update(result["message"])

            if result["success"]:
                self.app.switch_to_home()
