import os
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
with open("audio.txt", "r") as file:
    print(file.read())