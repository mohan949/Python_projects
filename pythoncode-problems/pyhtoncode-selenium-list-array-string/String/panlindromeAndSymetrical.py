

def palindrome(s):
 r_s = s[::-1]
 if r_s == s:
  return 'Palindrome'
 else:
  return 'not a palindrome'
 

def symetraical(s):
    length_s = len(s)
    mid = length_s//2
    print(length_s)
    print(mid)
    print(s[:mid])
    print(s[mid:])
    
    if length_s % 2 == 0:
     print ('String is symetrical')
    else :
      print('String is not symetraical')


def reverse(s):
  return s[::-1]


def replace1(s):
  s = s.replace("a", "k",6)
  return s
    

def split(s):
   a = s.split()
   print(type(a))
   print(len(a))
   for i in a:
     print(i, end='')


def length(s):
  counter = 0
  for i in s:
    counter+=1
    return counter
  
def String_prime(s):
  s= s.split()
  for i in s:
    if len(i) %2==0:
        return i


def upperHalf(s):
  s = s.replace(' ','')
  orginal = s
  print(s)
  mid = len(s)//2
  s = (s[mid:])
  print(orginal[:mid]+s.upper())
  


def vowel(s):
  v = set('aeiou')
  print(v)
  a = set({})
  for char in s :
    if char in v:
      r = a.add(char)
      return(r)

def match(s1, s2):
  s1 = set(s1)
  s2 = set(s2)
  #s3 = s1.intersection(s2)
  s3 = s1.join(s2)
  return s3



s1 = 'abcdef'
s2 = 'defghia'
print(match(s1, s2))