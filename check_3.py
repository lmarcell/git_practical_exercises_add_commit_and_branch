#!/usr/bin/env python3

import subprocess

#Check merge commit

command = subprocess.run(['git', 'log', 'main', '-n', '1', '--pretty=format:%s'], stdout=subprocess.PIPE)
result = (str(command.stdout.decode("utf-8")).strip().lower())

assert result == "merge branch 'say_hi_to_joe' into main", "There's no merge commit on the top of the main branch"

#Check first parent of HEAD
command = subprocess.run(['git', 'log', 'HEAD^1', '-n', '1', '--pretty=format:%s'], stdout=subprocess.PIPE)
result = (str(command.stdout.decode("utf-8")).strip().lower())

assert result == "hope he is well", "The first parent of the HEAD commit shall be the commit with the message 'Hope he is well'"

#Check second parent of HEAD
command = subprocess.run(['git', 'log', 'HEAD^2', '-n', '1', '--pretty=format:%s'], stdout=subprocess.PIPE)
result = (str(command.stdout.decode("utf-8")).strip().lower())

assert result == "change john to joe", "The second parent of the HEAD commit shall be the commit with the message 'change john to joe'"

#Make sure there's no new commit on say_hi_to_joe branch
command = subprocess.run(['git', 'log', 'say_hi_to_joe', '-n', '1', '--pretty=format:%s'], stdout=subprocess.PIPE)
result = (str(command.stdout.decode("utf-8")).strip().lower())

assert result == "change john to joe", "The top commit of branch say_hi_to_joe shall be the commit with the message 'change john to joe'"

print ("Exercise successfully done")
