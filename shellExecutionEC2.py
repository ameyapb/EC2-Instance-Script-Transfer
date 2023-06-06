import boto3
import time
import paramiko
import subprocess

print("Hello! Please wait until your EC2 instance is up...")

access_key_id = 'your_access_key'
secret_access_key = 'secret_access_key'
region = 'us-east-1'
security_group_id = 'sec_group_id'

session = boto3.Session(
    aws_access_key_id=access_key_id,
    aws_secret_access_key=secret_access_key,
    region_name=region
)

# Create an EC2 resource object
ec2_resource = session.resource('ec2')

# Create an EC2 instance
instance = ec2_resource.create_instances(
    ImageId='ami-053b0d53c279acc90',
    InstanceType='t2.micro',
    KeyName='myTest12',
    MinCount=1,
    MaxCount=1,
    SecurityGroupIds=[security_group_id] 
)

# Wait for the instance to be running
instance[0].wait_until_running()

print("EC2 instance is now running. Instance ID:", instance[0].id)
print("Please wait until we establish a connection")

time.sleep(60)
instance[0].load()

# Get the public IP address of the instance
public_ip = instance[0].public_ip_address
print("Your Public IP is: ", instance[0].public_ip_address)

# Establish an SSH connection to the instance
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Replace 'your_key.pem' with the path to your private key file
private_key = paramiko.RSAKey.from_private_key_file('C:\\Users\\I02157754\\Downloads\\myTest12.pem')

# Connect to the instance using the public IP and private key
ssh.connect(public_ip, username='ubuntu', pkey=private_key)

print("Connection has been established. Now we are in the process of configuring your system for you..")

# Install Python 3 on the EC2 instance
stdin, stdout, stderr = ssh.exec_command('sudo apt-get update && sudo apt-get install -y python3')

# Wait for the installation to complete
stdout.channel.recv_exit_status()

print("Python has been installed, Please login into your EC2 instance and run the following script /home/ubuntu/topScript.py")

# Transfer the script file to the EC2 instance
sftp = ssh.open_sftp()
local_file = 'Location_of_your_script_on_local Machine' #Location
remote_file = '/home/ubuntu/topScript.py'  # Destination path on the EC2 instance

sftp.put(local_file, remote_file)
sftp.close()

# Close the SSH connection
ssh.close()
