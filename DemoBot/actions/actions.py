from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionCheckWeather(Action):
    def name(self):
        return "action_check_weather"

    def run(self, dispatcher, tracker, domain):
        city = tracker.get_slot("city")
        if city:
            # Simulate a weather API response
            weather_response = f"The weather in {city} is sunny and 25°C!"
        else:
            weather_response = "Please tell me a city to check the weather for."
        dispatcher.utter_message(text=weather_response)
        return []