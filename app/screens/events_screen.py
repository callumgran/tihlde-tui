from app.screens.base_screen import BaseScreen
from textual.containers import Container, Horizontal
from textual.widgets import Label, Button, LoadingIndicator, Switch
from app.api import fetch_events


class EventsScreen(BaseScreen):
    """Screen to display a list of events with filtering and pagination."""

    def __init__(self):
        super().__init__()
        self.expired = False  # Show only non-expired events by default
        self.activity = False  # Show non-activity events by default
        self.page = 1  # Start with the first page
        self.events_container = Container(id="events-container", classes="events")
        self.filters_container = Horizontal(id="filters-container", classes="filters")

    def compose(self):
        """Compose the layout with filters, events, and navigation."""
        yield from super().compose()
        yield self.filters_container
        yield self.events_container
        yield Horizontal(
            Button("Previous Page", id="prev-page", variant="primary"),
            Button("Next Page", id="next-page", variant="primary"),
            id="pagination-container",
        )

    async def on_mount(self):
            """Fetch and display events when the screen is mounted."""
            await self.load_events()
            self.filters_container.mount(
                Label("Expired Events:"),
                Switch(name="Show Expired Events", value=self.expired, id="toggle-expired"),
                Label("Activity Events:"),
                Switch(name="Show Activities", value=self.activity, id="toggle-activity"),
            )

    async def load_events(self):
        """Fetch events with current filters and page."""
        self.events_container.remove_children()
        self.events_container.mount(LoadingIndicator())

        try:
            events = await fetch_events(
                self.app.token,
                expired=self.expired,
                activity=self.activity,
                page=self.page,
            )
            self.render_events(events)
        except Exception as e:
            self.events_container.remove_children()
            self.events_container.mount(Label(f"[bold red]Failed to load events: {e}[/bold red]"))

    def render_events(self, events):
        """Render the list of events."""
        self.events_container.remove_children()
        if events:
            for event in events:
                self.events_container.mount(self.create_event_widget(event))
        else:
            self.events_container.mount(Label("[bold red]No events found.[/bold red]"))

    def create_event_widget(self, event):
        """Create a widget for an individual event."""
        event_details = (
            f"[bold]{event['title']}[/bold]\n"
            f"Start Date: {event['start_date']}\n"
            f"End Date: {event['end_date']}\n"
            f"Organizer: {event['organizer']['name']}\n"
            f"Category: {event['category']['text']}\n"
        )
        return Container(
            Label(event_details),
            Button("View Details", id=f"event-{event['id']}", variant="primary"),
            classes="event-container",
        )

    async def on_switch_changed(self, event: Switch.Changed):
        """Handle switch state changes."""
        if event.switch.id == "toggle-expired":
            self.expired = event.value
        elif event.switch.id == "toggle-activity":
            self.activity = event.value
        await self.load_events()

    async def on_button_pressed(self, event):
        """Handle button presses."""
        if event.button.id.startswith("event-"):
            event_id = event.button.id.split("-")[1]
            self.app.show_event_details(event_id)
        elif event.button.id == "prev-page":
            if self.page > 1:
                self.page -= 1
                await self.load_events()
        elif event.button.id == "next-page":
            self.page += 1
            await self.load_events()
