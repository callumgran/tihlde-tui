from textual.containers import Container
from textual.widgets import Label, Button, Markdown
from app.utils import pretty_print_date

def create_event_details_view(app, event):
    """
    Creates the detailed view for an event.
    Args:
        event (dict): The event data.
        app: The main application instance (optional, for navigation).
    Returns:
        Container: A container displaying event details.
    """

    details = (
        f"[bold]{event['title']}[/bold]\n\n"
        f"Start Date: {pretty_print_date(event['start_date'])}\n"
        f"End Date: {pretty_print_date(event['end_date'])}\n\n"
        f"Location: {event['location']}\n"
        f"Organizer: {event['organizer']['name']}\n"
        f"Category: {event['category']['text']}\n\n"
    )

    return Container(
        Label(details, classes="event-details"),
        Markdown(event['description']),
        Button("Back", id="back-to-events", variant="warning"),
        id="event-details-container",
        classes="event-details",
    )
