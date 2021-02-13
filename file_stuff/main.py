

with open ("blub.txt", mode="a") as file:
    file.write("\nNew Text.")

with open("blub.txt") as file:

    content = file.read()
    print(content)
