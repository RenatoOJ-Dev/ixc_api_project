import os
import textfsm
from netmiko import ConnectHandler


class ZTEC320OLT:
    """Representa uma OLT ZTE C320 e suas operações de consulta GPON."""

    def __init__(self, host: str, username: str, password: str,
                 port: int = 22, template_path: str | None = None, **timeout_kwargs):
        # 1. Encapsulamento: guardamos o que é "estado" do objeto aqui
        self._config = {
            "device_type": "zte_zxros",
            "host": host,
            "username": username,
            "password": password,
            "port": port,
            **timeout_kwargs
        }
        self._template_path = template_path or os.path.abspath("src/templates/olt_onu_status.template")
        self._conn = None  # Conexão só existe após .connect()

    # 2. Context Manager: permite usar `with ZTEC320OLT(...) as olt:`
    def __enter__(self):
        self._conn = ConnectHandler(**self._config)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.disconnect()
        return False  # Não suprime exceções

    def disconnect(self):
        if self._conn:
            self._conn.disconnect()
            self._conn = None

    # 3. Métodos com responsabilidade única (Single Responsibility)
    def _parse_textfsm(self, raw_output: str) -> list[dict]:
        """Parser interno. Esconde a complexidade do TextFSM."""
        with open(self._template_path, encoding="utf-8") as f:
            fsm = textfsm.TextFSM(f)
            parsed = fsm.ParseText(raw_output)
            return [dict(zip(fsm.header, row)) for row in parsed]

    def get_onu_id_from_sn(self, sn: str) -> str:
        """Extrai o ID da porta/slot a partir do Serial Number."""
        raw = self._conn.send_command(f"show gpon onu by sn {sn}")
        try:
            # Sua lógica de string mantida, mas protegida
            return raw.split("_")[1].split(":")[0]
        except IndexError as e:
            raise ValueError(f"Formato inesperado ao buscar SN '{sn}'. Output: {raw}") from e

    def get_onu_states(self, onu_id: str) -> list[dict]:
        """Retorna a tabela de estados já estruturada."""
        raw = self._conn.send_command(f"show gpon onu state gpon-olt_{onu_id}")
        return self._parse_textfsm(raw)

    def get_onu_details(self, onu_index: str) -> str:
        """Retorna o output cru de detalhes (útil para debug ou log)."""
        return self._conn.send_command(f"show gpon onu detail-info gpon-onu_{onu_index}")

    # 4. Orquestração: método de alto nível que usa os outros
    def process_los_by_sn(self, sn: str) -> int:
        """Fluxo completo: busca ONU → filtra LOS → imprime detalhes → retorna contagem."""
        onu_id = self.get_onu_id_from_sn(sn)
        states = self.get_onu_states(onu_id)

        los_count = 0
        for state in states:
            if state.get("PHASE_STATE") == "LOS":
                details = self.get_onu_details(state["ONU_INDEX"])
                print(f"\n🚨 DETALHES - ONU {state['ONU_INDEX']} (Status: LOS)")
                print(details)
                los_count += 1

        print(f"\n✅ Total de ONUs com LOS encontradas: {los_count}")
        return los_count
