# handle/worker.py

import redis
import json
import time
from handle.qtd_os_tecnico import fetch_os_abertas_por_tecnico
from qtd_os_finish_day.handle_os_finish_for_tec_today import get_os_finalizadas_hoje

CACHE_TTL = 60
UPDATE_INTERVAL = 30

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

JOBS = [
    ("cache:os_abertas_por_tecnico", fetch_os_abertas_por_tecnico),
    ("cache:os_finalizadas_hoje", get_os_finalizadas_hoje),
]


def atualiza_cache():
    while True:
        for cache_key, fetch_fn in JOBS:
            try:
                dados = fetch_fn()
                redis_client.setex(cache_key, CACHE_TTL, json.dumps(dados))
                print(f"✔ {cache_key} atualizado ({len(dados)} registros)")
            except Exception as e:
                print(f"✘ Erro em {cache_key}: {e}")
        time.sleep(UPDATE_INTERVAL)


if __name__ == "__main__":
    atualiza_cache()
