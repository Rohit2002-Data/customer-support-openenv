import requests

BASE_URL = "http://localhost:7860"

def run():
    # Reset environment
    r = requests.post(f"{BASE_URL}/reset")
    obs = r.json()["observation"]

    total_reward = 0

    for _ in range(3):
        action = {
            "action_type": "respond",
            "category": "account",
            "response_text": "Please reset your password using the link sent to your email."
        }

        r = requests.post(f"{BASE_URL}/step", json=action)
        data = r.json()

        total_reward += data["reward"]

        if data["done"]:
            break

    print("Final Score:", total_reward)

if __name__ == "__main__":
    run()
