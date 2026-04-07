with open("data.txt", "r") as f:
    data = int(f.read())
    data += 1
with open("data.txt", "w") as f:
    f.write(str(data))