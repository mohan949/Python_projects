# p1 = 'make money'
# p2 = 'buy now'
# p3 = 'click on this link'
# i = True
# while(i==True):
#     comment = input('enter the comment ')
#     if((p1 in comment)or (p2 in comment)or (p3 in comment)):
#         print('this is a spam')
#     else:
#         print('this is not a spam')    
    
    
    
    
# def takeInput():
#  username = input('enter the user name : ')
#  return username

# takeInput()
# i= True
# while(i==True):
#   if(len(username)<10):
#      print(f'user name is less{len(username)}\n try again ')
#   else:
#      print('your user name is available '+username+' continue ')
#      i==False


def takeInput():
    username = input('Enter the username: ')
    return username

i = True
while i:
    username = takeInput()
    if (len(username) < 10):
        print(f'Username is too short ({len(username)} characters). Please try again.\n')
    else:
        print('Your username is available: ' + username + '. You can continue.')
        i = False



    