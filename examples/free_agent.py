"""Free Vino & Views HTTP client; no token or payment required."""
import json
from urllib.request import Request, urlopen

API = "https://api.vinoandviews.online"

def call(service, inputs):
    request = Request(API + "/v1/" + service, data=json.dumps(inputs).encode(),
                      headers={"Content-Type": "application/json", "DNT": "1"}, method="POST")
    with urlopen(request, timeout=60) as response:
        return json.load(response)

if __name__ == "__main__":
    print(json.dumps(call("agent-budget-guard", {"chain":"base",
        "target":"0x0000000000000000000000000000000000000001",
        "spend_usd":"1", "max_spend_usd":"2"}), indent=2))
