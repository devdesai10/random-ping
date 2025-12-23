import random, requests

WEBHOOK_URL = "https://discord.com/api/webhooks/1453007516677046296/ZtnLRbkLrFVXDLGDADmmFUYmkdVAFkkyF2eYmAJ1YbYGnSQQXGrw5IMH5LoIN69Fk-m-"

USERS = [
  "987478292468744262",  # Devan
  "475137832193884160",  # Jason
  "241900841269723136",  # Brian
  "251516034857697282",  # David
  "151448029189111810",  # Zach
  "222048801030930433",  # Shane
  "260514842174029826",  # Chris
  "949486791050792980",  # John
]

pick = random.choice(USERS)

requests.post(WEBHOOK_URL, json={
  "content": f"Randomly chosen: <@{pick}> 😈, FUCK YOU",
  "allowed_mentions": {"users": [pick]}
})

print("Congrats you're the random one:", pick)
