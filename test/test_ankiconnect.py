import requests
import json

ANKI_CONNECT_URL = "http://localhost:8765"


def invoke(action, params=None, version=6):
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


def main():
    # Test 'modelNames' action
    model_names = invoke("modelNames")
    if model_names is not None:
        print(f"Retrieved {len(model_names)} note types:")
        for name in model_names:
            print(f"- {name}")
    else:
        print("Failed to retrieve note types.")

    # Test 'modelInfo' action for the first model
    if model_names:
        first_model = model_names[0]
        model_info = invoke("modelTemplates", {"modelName": first_model})
        if model_info is not None:
            print(f"\nModel Template for '{first_model}':")
            print(json.dumps(model_info, indent=4))
        else:
            print(f"Failed to retrieve model info for '{first_model}'.")
    else:
        print("No models available to test 'modelInfo'.")


if __name__ == "__main__":
    main()
