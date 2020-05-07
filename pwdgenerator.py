import random

print('Welcome i can generate a password for you')

maxlength = int(input('please enter the siwe you will need for your password\n'))

Figures = ['0','1','2','3','4','5','6','7','8','9']

Lower_case = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

Upper_case = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

Special_chars = ['&','(','-','_',')','!','@','#','$','%','^','*','?']

All_chars = random.choice(Figures) + random.choice(Lower_case) + random.choice(Upper_case) + random.choice(Special_chars)
Chars = (Figures) + (Lower_case) + (Upper_case) + (Special_chars)

print(All_chars)

for i in range (maxlength-4):
    All_chars += random.choice(Chars)
print(All_chars)