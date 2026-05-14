import paramiko
import time

# 1. Carregue a chave manualmente como RSA
# key_path = r'C:\Users\NV7 NOC\Documents\ssh-key-2026-02-09.key'
# private_key = paramiko.RSAKey.from_private_key_file(key_path)

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# 2. Passe o objeto da chave no parâmetro pkey (em vez de key_filename)
client.connect(
    hostname='10.222.50.22',
    username='nv7',
    port=22,
    password='Fak@as7348JHa'
)

ssh_shell = client.invoke_shell()
a = input('Digite o comando: ')
ssh_shell.send(a.encode('utf-8') + b'\n')
time.sleep(1)
print(ssh_shell.recv(1024).decode('utf-8'))
