import subprocess
import os

with open("data.txt", "r") as f:
    data = int(f.read())
    data += 1

with open("data.txt", "w") as f:
    f.write(str(data))

subprocess.run(["git", "config", "user.email", "action@github.com"])
subprocess.run(["git", "config", "user.name", "GitHub Action"])
subprocess.run(["git", "add", "data.txt"])
subprocess.run(["git", "commit", "-m", f"Update counter to {data}"])
subprocess.run(["git", "push"])