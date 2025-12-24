import os, random, requests

WEBHOOK_URL = os.environ["WEBHOOK_URL"]

USERS = [
  "987478292468744262",
  "475137832193884160",
  "241900841269723136",
  "251516034857697282",
  "151448029189111810",
  "222048801030930433",
  "260514842174029826",
  "949486791050792980",
]

pick = random.choice(USERS)

requests.post(WEBHOOK_URL, json={
  "content": f"Fuck you <@{pick}> 😈",
  "allowed_mentions": {"users": [pick]}
})

print("Victim:", pick)
