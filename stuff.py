import sys
import os
from subprocess import call

projects = [
    "workinator3",
    "workinator3-consumer",
    "workinator3-consumer-rabbitmq",
    "workinator3-coordinator",
    "workinator3-coordinator-mongodb",
    "workinator3-demo-inprocess",
    "workinator3-demo-rabbitmq",
    "workinator3-httpapi"
]

command = sys.argv[1]

startFolder = os.path.dirname(sys.argv[0])
startFolder = os.path.abspath(os.path.join(startFolder, ".."))

print("----------------------------------------------------------------------------------")
print("Workinator3 Project Folder: " + startFolder)
print("----------------------------------------------------------------------------------")

commands = []
if command == "pull":
    commands.append("git pull")
elif command == "commit":
    commands.append("git add --all")
    commands.append("git commit -m \"todo\"")
    commands.append("git push")
elif command == "status":
    commands.append("git status")
elif command == "installw":
    commands.append("mvnw.cmd clean install -DskipTests")
    
for project in projects:
    cwd = os.path.join(startFolder, project)
    print(cwd)
    for c in commands:
        print("\t" + c)
        call(c, cwd=cwd, shell=True)



