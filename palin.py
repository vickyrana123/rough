n=list(input("Enter the string: "))
t=n[:]
n.reverse()

print(t)
print(n)

if t == n:
    print("palindrom")
else:
    print("not")    

