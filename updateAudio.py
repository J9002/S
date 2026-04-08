import os
import subprocess
with open("audio.txt", "w") as file:
    file.write("")
    with open("audio.txt", "a") as file:
        content = os.listdir("audio")
        for x in range(len(content)):
            content[x] = content[x].split(".")[0]
            if x < len(content) - 1:
                file.write(f"{content[x]}\n")
            else:
                file.write(f"{content[x]}")
def git_push():
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "makey makey (automated)"], check=True)
    subprocess.run(["git", "push", "origin", "main"], check=True)
git_push()