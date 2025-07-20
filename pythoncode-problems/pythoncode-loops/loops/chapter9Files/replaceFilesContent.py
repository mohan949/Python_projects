word = 'Prashant'

with open ('sushant.txt','r') as f:
    c = f.read()

c_new = c.replace(word, 'mohan')

with  open ('sushant.txt','w') as f:
    f.write(c_new )

 
 