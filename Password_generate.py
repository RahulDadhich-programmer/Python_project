import random
passln = int(input("Enter the length of password"))
s="qwertyuiopasdfghjklzxcvbnm1234567890!@#$%^&**()?_-"
p = " ".join(random.sample(s,passln))
print(p)
