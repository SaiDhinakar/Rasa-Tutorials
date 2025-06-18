from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionBookFlight(Action):
    def name(self):
        return "action_book_flight"

    def run(self, dispatcher, tracker, domain):
        destination = tracker.get_slot("destination")
        date = tracker.get_slot("date")
        response = f"Booking a flight to {destination} on {date}."
        dispatcher.utter_message(text=response)
        return []
