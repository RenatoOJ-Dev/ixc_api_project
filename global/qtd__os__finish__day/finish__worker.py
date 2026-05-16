import redis
import json
import time
from handle__os__finish__for_tec__today import reponse__finished__today

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


def atualiza_cache():
    while True:
        dados = reponse__finished__today()
        r.setex("reponse__finished__today", 60, json.dumps(dados))  # salva por 60s
        time.sleep(30)  # atualiza a cada 30s


if __name__ == "__main__":
    atualiza_cache()
