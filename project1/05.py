n = 9


table = [n*i for i in range(1,11)]
with open("tables.txt", "a") as f:
    f.write(str(table)+"\n")

print(table)