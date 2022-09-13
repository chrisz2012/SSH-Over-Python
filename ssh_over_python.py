import paramiko
import sys

# You can put multiple hosts into the firstArg and the script will iterate over them
# The script splits each host out by just a space in the firstArg
# i.e. "hostname.eng.com hostname2.eng.com"
firstArg=sys.argv[1]
secondArg=sys.argv[2]

# Update the next three lines with your
# server's information

host = firstArg
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"
command = secondArg

client = paramiko.client.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Added the ability to iterate over multiple hosts
for i in firstArg.split():
    print("sshing to {}".format(i))
    client.connect(i, username=username, password=password)
    _stdin, _stdout, _stderr = client.exec_command(secondArg)
    print(_stdout.read().decode())
    del _stdin

client.close()
