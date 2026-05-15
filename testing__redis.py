import redis

r = redis.Redis(host='localhost', port=6379, decode_responses=True)

# Guardando valores
r.set("nome", "Renato")
r.set("idade", "30")

# Buscando de volta
print(r.get("nome"))   # Renato
print(r.get("idade"))  # 30

# Agora com TTL de 5 segundos
r.setex("temporario", 5, "esse valor some em 5s!")
print(r.get("temporario"))  # esse valor some em 5s!

import time
time.sleep(6)

print(r.get("temporario"))  # None — sumiu! ⏰