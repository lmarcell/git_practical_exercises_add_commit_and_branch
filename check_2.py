#!/usr/bin/env python3

import subprocess

# Check if branch exists
command = subprocess.run(['git', 'branch', '--list', 'say_hi_to_joe'], stdout=subprocess.PIPE)
result = (str(command.stdout.decode("utf-8")))

assert len(result) > 0, "The branch with name say_hi_to_joe does not exist"

# Check the commit message of the top commit of the branch
# Check the parent of the top commit (base of the branch)
command = subprocess.run(['git', 'log', 'say_hi_to_joe', '-n', '2', '--pretty=format:%s'], stdout=subprocess.PIPE)

result = (str(command.stdout.decode("utf-8")).strip().lower().split("\n"))

assert result[0] == "change john to joe", "The top most commit does not have the commit message 'Change John to Joe'"
assert result[1] == "ask if he is doing well", "The base of the branch should be the commit with the following message: 'Ask if he is doing well'"

# Check the content of the file
command = subprocess.run(['git', 'show', 'say_hi_to_joe:code.py'], stdout=subprocess.PIPE)

result = (str(command.stdout.decode("utf-8")).strip().split("\n"))

assert(len(result) == 5), "The number of lines in code.py on branch say_hi_to_joe shall be 4 at this point, but currently this condition is not satisfied"

expected_line = str("print(\"Hi Joe!\")")
assert result[3].strip() == expected_line.strip(), "The last line of code.py shall be print(\"Hi Joe!\"), but currently this condition is not satisfied"
expected_line = str("print(\"How are you?\")")
assert result[4].strip() == expected_line.strip(), "The last line of code.py shall be print(\"How are you?\"), but currently this condition is not satisfied"

print ("Exercise successfully done")
