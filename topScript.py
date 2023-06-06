import subprocess

print("Hello, please select the required input:")
print("1. Top Command")
print("2. NetStat Command")
print("3. DF Command")

choice = input("Enter your choice: ")

if choice == "1":
    # Execute the modified top command and save specific columns to file
    with open('output.txt', 'w') as file:
        # Create the header string
        header = "PID %CPU %MEM COMMAND\n"
        file.write(header)
        
        # Execute the modified top command to get the column values and append them to the file
        subprocess.run('top -b -n 1 -o %CPU | awk \'NR>6 {print $1, $9, $10, $12}\' | head -6 >> output.txt', shell=True)
        
    print("Top Command executed and output saved to 'output.txt' file.")

elif choice == "2":
    # Execute the netstat command and print the output
    subprocess.run('netstat -a', shell=True)

    print("NetStat Command executed.")

elif choice == "3":
    with open('output.txt', 'w') as file:
        
        # Execute the modified top command to get the column values and append them to the file
        subprocess.run('df -h >> output.txt', shell=True)
    print("DF Command executed and output saved to 'output.txt' file.")

else:
    print("Invalid choice. Please try again.")
