from textual.containers import Container, Vertical
from textual.widgets import Label, Button, Markdown, LoadingIndicator
from app.utils import pretty_print_date
from app.api import fetch_event_details
from app.api.registration import check_registration_status


def create_event_details_view(app, event_id: str):
    details_container = Container(id="event-details-container", classes="event-details")

    async def load_event_details():
        details_container.mount(LoadingIndicator())
        try:
            event = await fetch_event_details(event_id, app.token)
            user_registered = await check_registration_status(event_id, app.token, app.context.get_user_data()["user_id"])

            details = (
                f"Signed Up: {event['list_count']} / {event['limit'] or 'Unlimited'}\n\n"
                f"[bold]{event['title']}[/bold]\n\n"
                f"Start Date: {pretty_print_date(event['start_date'])}\n"
                f"End Date: {pretty_print_date(event['end_date'])}\n\n"
                f"Location: {event['location']}\n"
                f"Organizer: {event['organizer']['name']}\n"
                f"Category: {event['category']['text']}\n\n"
            )

            details_container.remove_children()

            button_label = "Sign Off" if user_registered else "Sign Up"
            button_id = "sign-off" if user_registered else "sign-up"

            details_container.mount(
                Button(button_label, id=button_id, variant="primary"),
                Label(details, classes="event-details"),
                Markdown(event["description"]),
                Button("Back", id="back-to-events", variant="warning"),
            )
        except Exception as e:
            details_container.remove_children()
            details_container.mount(Label(f"[bold red]Error loading event details: {e}[/bold red]"))

    app.call_later(load_event_details)
    return details_container
