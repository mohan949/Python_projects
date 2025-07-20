f = open("sushant.txt")
name = f.read()
print(name)
if('Prashant' in name):
    print('prashant is resigned')
else: 
    print('prahant name is not present')