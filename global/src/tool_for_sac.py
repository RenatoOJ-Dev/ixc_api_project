from netmiko import ConnectHandler
# from getpass import getpass
# from pprint import pprint
import textfsm
import os

host = os.getenv('HOST')
username = os.getenv('USER')
password = os.getenv('PASS')
port = '22'

zte_c320_jt = {
    'device_type': 'zte_zxros',
    'host': host,
    'username': username,
    'password': password,
    'port': port,
    'conn_timeout': 20,
    'session_timeout': 30,
    'auth_timeout': 15,
}

template_path = os.path.abspath('src/templates/olt_onu_status.template')
os.system('clear')
message = input('sn: ')


with ConnectHandler(**zte_c320_jt) as net_connect:
    output = net_connect.send_command(f'show gpon onu by sn {message}')
    onu_id = output.split("_")[1].split(":")[0]
    onu_id_fixed = '_' + onu_id
    output2 = net_connect.send_command(f'show gpon onu state gpon-olt{onu_id_fixed}')

    with open(template_path, encoding="utf-8") as template_file:
        fsm = textfsm.TextFSM(template_file)

        parsed_output = fsm.ParseText(output2)

        column_names = fsm.header
        dados_estruturados = [dict(zip(column_names, row)) for row in parsed_output]
        count = 0
        for data in dados_estruturados:
            if data.get("PHASE_STATE") == 'LOS':
                # pprint(f'{data.get("ONU_INDEX", "NULL")}, {data.get("PHASE_STATE", "NULL")}')
                output3 = net_connect.send_command(f'show gpon onu detail-info gpon-onu_{data.get("ONU_INDEX")}')
                print(output3)
                count += 1
        print(count)
