# handle/worker.py

from qtd_os_finish_day.handle_os_finish_for_tec_today import get_os_finalizadas_hoje
from handle.qtd_os_tecnico import fetch_os_abertas_por_tecnico
from renato_all_os.engine_request import get_os_renato
from qtd_os_exec.exe_os_get import fetch_os_em_execucao
import redis
import json
import time

CACHE_TTL = 60
UPDATE_INTERVAL = 30

redis_client = redis.Redis(host="localhost", port=6379, decode_responses=True)

JOBS = [
    ("cache:os_abertas_por_tecnico", fetch_os_abertas_por_tecnico),
    ("cache:os_finalizadas_hoje", get_os_finalizadas_hoje),
    ("cache:os_baixa_renato", get_os_renato),
    ("cache:os_em_execucao", fetch_os_em_execucao)
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
