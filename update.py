with open("data.txt", "r") as f:
    value = int(f.read())
with open("data.txt", "w") as f:
    f.write(str(value + 1))