import paramiko

class SSHConnectivity:
    def __init__(self):
        try:
            # Create an SSH Client
            self.ssh_client = paramiko.SSHClient()

        except Exception as e:
            raise

    def execute_remote_command(self,host,port,username,password,command):
        try:
            #Automatically add the server's hostkey(not recommanded for production)

            self.ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy)

            #Connect to the remote server
            self.ssh_client.connect(hostname=host,port=port,username=username,password=password)

            #excute the command
            stdin,stdout,stderr = self.ssh_client.exec_command(command)

            #read the command output
            output = stdout.read().decode().split("\n")
            error = stderr.read().decode()

            #close the connection

            self.ssh_client.close()


            return output,error

        except Exception as e:
            print(f"An error occured:{e}")

            return None,str(e)



