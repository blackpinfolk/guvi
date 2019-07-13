i=input()
if i in ['a','e','i','o','u']:
    print("Vowel")
elif (ord(i)>=97 and ord(i)<=122)or(ord(i)>=65 and ord(i)<=90):
    print("Consonant")
else:
    print("invalid")
