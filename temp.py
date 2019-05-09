lst = [1, 0, 0, 1, 0, 1, 1, 0]
srg = '11101010101'

#for i in lst:
	#srg = srg + str(i)
	
#print(srg)

lst2 =[]
for i in srg:
	lst2.append(int(i))
	
print(lst2)

lst2.reverse()

print(lst2)

