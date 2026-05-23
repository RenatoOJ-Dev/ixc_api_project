# worker.py

from os_finished_today.handle_os_finish_for_tec_today import get_os_finalizadas_hoje
from os_by_technician.qtd_os_tecnico import fetch_os_abertas_por_tecnico
from assigned_os.assigned_os import get_os_renato
from os_in_execution.exe_os_get import fetch_os_em_execucao
import logging
import redis
import json
import time
from dotenv import load_dotenv
import os


load_dotenv()

redis_host = os.getenv('REDIS_HOST')
redis_port = os.getenv('REDIS_PORT')

CACHE_TTL = 60
UPDATE_INTERVAL = 30


redis_client = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

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
                logging.info(f"✔ {cache_key} atualizado ({len(dados)} registros)")
            except Exception as e:
                logging.error(f"✘ Erro em {cache_key}: {e}")
        time.sleep(UPDATE_INTERVAL)


if __name__ == "__main__":
    atualiza_cache()
