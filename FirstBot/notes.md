# CLI commands:

* **rasa init** -> initilize the rasa project structure by asking some questions.
* **rasa init** **--no-prompt** -> initilize the project structure instantly without any question and along with sample model will trained.
* **rasa train** -> train the rasa model.

Rasa is build up of two important features,

1. **NLU (Natural Language Understanding)** -> Understands user inputs (e.g., classifies intent, extracts entities).
2. **Rasa Core** -> Manages the dialogue, deciding how the bot should respond.

> *"Book a flight to Paris"* . Rasa figures out:
>
> * Your  **intent** : BookFlight
> * An  **entity** : Destination = Paris
>
>   Then it decides the next step, like asking you for the travel date.


Rasa not supports for python 12 and above. Use python 3.9.

**Project Structure (using rasa init --no-prompt) :**

my_bot/
│
├── data/              ← where training data lives
│   ├── nlu.yml        ← user messages (intents)
│   ├── rules.yml      ← simple dialog rules
│   └── stories.yml    ← conversation paths
│
├── domain.yml         ← bot’s memory: intents, responses, slots
├── config.yml         ← ML pipeline and policies
├── actions/           ← custom Python code
└── credentials.yml    ← connect to channels (e.g., Slack)
