Title: EC2-Instance-Script-Transfer

Description: The EC2-Instance-Script-Transfer repository contains a script that automates the process of spinning up an EC2 instance, transferring another script from your local machine to the EC2 instance, and executing that script on the EC2 instance.

Steps to Use:

--> Ensure you have the necessary credentials: Replace the access_key_id, secret_access_key, region, and security_group_id variables with your own AWS credentials and security group ID.
--> Set up the required dependencies: Make sure you have boto3, paramiko, and subprocess installed on your local machine.
--> Modify the script as needed: Update the ImageId, InstanceType, and KeyName variables to match your desired EC2 instance configuration. Also, replace the private_key path with the path to your own private key file.
--> Specify the location of your script: Update the local_file variable with the path of the script you want to transfer from your local machine to the EC2 instance.
--> Run the script: Execute the script and wait for the EC2 instance to be created. Once the instance is running, a connection will be established, Python 3 will be installed on the instance, and the specified script will be transferred to the instance. You will be provided with the public IP address of the instance.
--> Execute the transferred script: Log in to your EC2 instance using SSH and run the transferred script located at /home/ubuntu/topScript.py.

With the EC2-Instance-Script-Transfer repository, you can automate the process of setting up an EC2 instance, transferring a script, and executing it on the instance. This can be useful for various scenarios such as deploying applications, running data processing tasks, or performing automated tasks on remote instances.
