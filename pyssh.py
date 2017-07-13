from paramiko import client

class ssh:

    client = None

    def __init__(self, address, username,password):
        print("Connecting to server.")
        self.client = client.SSHClient()
        self.client.set_missing_host_key_policy(client.AutoAddPolicy())
        self.client.connect(address, username=username, password=password, look_for_keys=False)

    def sendCommand(self, command):
        if(self.client):
            stdin, stdout, stderr = self.client.exec_command(command)
            while not stdout.channel.exit_status_ready():
                # Print data when available
                if stdout.channel.recv_ready():
                    alldata = stdout.channel.recv(1024)
                    prevdata = b"1"
                    while prevdata:
                        prevdata = stdout.channel.recv(1024)
                        alldata += prevdata

                    print(str(alldata))
        else:
            print("Connection not opened.")
conn = ssh("localhost","sanjay",'redhat')
conn2 = ssh("localhost","sanjay",'redhat')
conn3 = ssh("localhost","sanjay",'redhat')

print ("to exit please type exit")

while True:  # This constructs an infinite loop
   cmd = raw_input(" please enter the command ")
   if (cmd == 'exit'):
       break
   else:
      conn.sendCommand(cmd)
      conn2.sendCommand(cmd)
      conn3.sendCommand(cmd)
