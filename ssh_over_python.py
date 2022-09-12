import paramiko
import sys

firstArg=sys.argv[1]
secondArg=sys.argv[2]

# Update the username and password with your
# credential information

host = firstArg
username = "YOUR_USER"
password = "YOUR_PASSWORD"
command = secondArg

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host, username=username, password=password)
_stdin, _stdout,_stderr = client.exec_command(secondArg)
print(_stdout.read().decode())

del _stdin
client.close()
