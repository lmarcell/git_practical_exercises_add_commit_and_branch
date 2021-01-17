#!/usr/bin/env python3

import subprocess


# Check top commit 3 message of log
command = subprocess.run(['git', 'log', 'main', '-n', '3', '--pretty=format:%s'], stdout=subprocess.PIPE)

result = (str(command.stdout.decode("utf-8")).strip().lower().split("\n"))

assert result[0] == "hope he is well", "The top most commit does not have the commit message 'Hope he is well'"
assert result[1] == "ask if he is doing well", "The top most commit does not have the commit message 'Ask if he is doing well'"
assert result[2] == "say hi to john", "The top most commit does not have the commit message 'Say Hi to John'"

# Check number of commits
command = subprocess.run(['git', 'log', 'main', '--oneline'], stdout=subprocess.PIPE)

result = (str(command.stdout.decode("utf-8")).strip().split('\n'))

assert (len(result) == 4), "The number of commits on the main branch at this point shall be 4, but currently this condition is not satisfied"

# Check content of code.py
file1 = open('code.py', 'r') 
lines = file1.readlines()

assert(len(lines) == 6), "The number of lines in code.py shall be 4 at this point, but currently this condition is not satisfied"

expected_line = str("print(\"Hi John!\")")
assert lines[3].strip() == expected_line.strip(), "The last line of code.py shall be print(\"Hi John!\"), but currently this condition is not satisfied"
expected_line = str("print(\"How are you?\")")
assert lines[4].strip() == expected_line.strip(), "The last line of code.py shall be print(\"How are you?\"), but currently this condition is not satisfied"
expected_line = str("print(\"I hope you are well?\")")
assert lines[5].strip() == expected_line.strip(), "The last line of code.py shall be print(\"I hope you are well?\"), but currently this condition is not satisfied"

print ("Exercise successfully done")
