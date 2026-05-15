import redis
import json
import time
from app_os_po_tec import tec_total

r = redis.Redis(host='localhost', port=6379, decode_responses=True)


def atualiza_cache():
    while True:
        dados = tec_total()
        r.setex("tec_total", 60, json.dumps(dados))  # salva por 60s
        time.sleep(30)  # atualiza a cada 30s


if __name__ == "__main__":
    atualiza_cache()
