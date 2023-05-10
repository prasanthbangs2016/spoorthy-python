import os
import datetime

# define the shell command you want to run
shell_command = "uname -a"

# define the file path to store the log
log_file_path = "/home/centos/uname-output.log"

# get the current timestamp
timestamp = datetime.datetime.now()

# run the shell command and capture the output
output = os.popen(shell_command).read()

# open the log file in append mode and write the timestamp and output
with open(log_file_path, "a") as log_file:
    log_file.write(f"{timestamp}: {output}\n")

# print the output to the console
print(output)
