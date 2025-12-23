import os, random, requests

WEBHOOK_URL = os.environ["https://discord.com/api/webhooks/1453007516677046296/ZtnLRbkLrFVXDLGDADmmFUYmkdVAFkkyF2eYmAJ1YbYGnSQQXGrw5IMH5LoIN69Fk-m-"]  # <-- change to this

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
