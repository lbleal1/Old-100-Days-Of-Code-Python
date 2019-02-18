rub = int(input("Your rubies:"))
sap = int(input("Your sapphires:"))
em  = int(input("Your emeralds:"))

ex_rub = int(input("How many rubies for a sapphire?"))
ex_sap = int(input("How many sapphires for an emerald?"))
ex_em = int(input("How many emerald for a ruby?"))

ex = 0
min_rub = 99999
min_sap = 99999 
min_em = 99999  

while rub > ex_rub or sap > ex_sap or em > ex_em :
	print("rub :", rub)		
	min_rub = rub // ex_rub
	sap += min_rub
	rub -= (min_rub*ex_rub)
	if min_rub != 0:
		ex +=1	
	print("min_rub:", min_rub)
	print("sap:", sap)
	print("rub:", rub)	
	print()

	print("sap :", sap)	
	min_sap = sap // ex_sap 
	em  += (min_sap)
	sap -= (min_sap*ex_sap)
	if min_sap != 0:
		ex +=1
	print("min_sap:", min_sap)
	print("em:", em)
	print("sap:", sap)	
	print()

	print("em :", em)	
	min_em = em  // ex_em  
	rub += (min_em ) 
	em -=(min_em *ex_em) 
	if min_em != 0:
		ex +=1
	print("min_em:", min_em)
	print("rub:", rub)
	print("em:", em)	
	print()
	
print("Exchanges:", ex)
