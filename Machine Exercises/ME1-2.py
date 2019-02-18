rice = float(input("Cups of rice: "))
seaweed = float(input("Sheets of seaweed:"))
crabsticks = float(input("Crabsticks:"))
avocado = float(input("Avocado:"))

r = rice//0.4
s = seaweed//0.5
c = crabsticks//3
a = avocado//0.25

if r <= s and r <= c and r <= a:
	rolls = r
elif s <= r and s <= c and s <= a:
	rolls = s
elif c <= r and c <= s and c <= a:	
	rolls = c
else:
	rolls = a

print("Rolls we can make:", int(rolls))

print("Leftover cups of rice:", rice - rolls*0.4)
print("Leftover sheets of seaweed:", seaweed - rolls*0.5)
print("Leftover crabsticks:", crabsticks - rolls*3)
print("Leftover avocado:", avocado - rolls*0.25)




