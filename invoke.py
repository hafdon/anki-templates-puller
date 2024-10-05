import requests

ANKI_CONNECT_URL = "http://localhost:8765"


def invoke(action, params=None, version=6):
    """
    Helper function to communicate with AnkiConnect.
    """
    payload = {"action": action, "version": version}
    if params:
        payload["params"] = params

    try:
        response = requests.post(ANKI_CONNECT_URL, json=payload)
        response.raise_for_status()
        result = response.json()

        if result.get("error"):
            print(f"Error with action '{action}': {result['error']}")
            return None

        return result.get("result")
    except requests.exceptions.RequestException as e:
        print(f"AnkiConnect request failed: {e}")
        return None
