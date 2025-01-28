from app.screens.base_screen import BaseScreen
from textual.containers import Container
from textual.widgets import Label, Button, Markdown, LoadingIndicator
from app.utils import pretty_print_date
from app.api import fetch_event_details
from app.api.registration import register_for_event, unregister_from_event, check_registration_status


class EventDetailsScreen(BaseScreen):

    def __init__(self, event_id):
        super().__init__()
        self.event_id = event_id
        self.signed_up = False
        self.details_container = Container(id="event-details-container", classes="event-details")
        self.status_label = Label("", id="status-message")

    def compose(self):
        yield from super().compose()
        yield self.details_container
        yield self.status_label

    async def on_mount(self):
        await self.load_event_details()

    async def load_event_details(self):
        self.details_container.remove_children()
        self.details_container.mount(LoadingIndicator())

        try:
            event = await fetch_event_details(self.event_id, self.app.token)
            user_registered = await check_registration_status(
                self.event_id,
                self.app.token,
                self.app.context.get_user_data()["user_id"]
            )
            self.render_event_details(event, user_registered)
        except Exception as e:
            self.details_container.remove_children()
            self.details_container.mount(Label(f"[bold red]Error loading event details: {e}[/bold red]"))

    def render_event_details(self, event, user_registered):
        self.details_container.remove_children()

        details = (
            f"Signed Up: {event['list_count']} / {event['limit'] or 'Unlimited'}\n\n"
            f"[bold]{event['title']}[/bold]\n\n"
            f"Start Date: {pretty_print_date(event['start_date'])}\n"
            f"End Date: {pretty_print_date(event['end_date'])}\n\n"
            f"Location: {event['location']}\n"
            f"Organizer: {event['organizer']['name']}\n"
            f"Category: {event['category']['text']}\n\n"
        )

        self.signed_up = user_registered

        button_label = "Sign Off" if self.signed_up else "Sign Up"
        button_id = "sign-off" if self.signed_up else "sign-up"

        self.details_container.mount(
            Button(button_label, id=button_id, variant="primary"),
            Label(details, classes="event-details"),
            Markdown(event["description"]),
        )

        if not self.details_container.query("#back-to-events"):
            self.details_container.mount(Button("Back", id="back-to-events", variant="warning"))

    async def handle_registration_action(self):
        try:
            if not self.signed_up:
                success = await register_for_event(self.event_id, self.app.token)
                if success:
                    self.status_label.update("[bold green]Successfully signed up![/bold green]")
                else:
                    self.status_label.update("[bold red]Sign-up failed![/bold red]")
            else:
                success = await unregister_from_event(self.event_id, self.app.token, self.app.context.get_user_data()["user_id"])
                if success:
                    self.status_label.update("[bold green]Successfully signed off![/bold green]")
                else:
                    self.status_label.update("[bold red]Sign-off failed![/bold red]")

            await self.load_event_details()
        except Exception as e:
            self.status_label.update(f"[bold red]Error: {e}[/bold red]")

    async def on_button_pressed(self, event):
        if event.button.id in ["sign-up", "sign-off"]:
            await self.handle_registration_action()
        elif event.button.id == "back-to-events":
            self.app.pop_screen()
