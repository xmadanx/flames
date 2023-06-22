def main():
	name1 = input("1st Name: ").lower()
	name2 = input("2nd Name: ").lower()

	namelist1 = list(name1)
	namelist2 = list(name2)

	for i,j in enumerate(namelist1):
		for k,l in enumerate(namelist2):
			if j == l:
				namelist1.pop(i)
				namelist2.pop(k)

	rvalue = len(namelist1) + len(namelist2)

	#print(f"\nFLAMES value is {rvalue}\n")

	flist = list("FLAMES")

	#print(*flist)

	while len(flist) != 1:
		if rvalue > len(flist):
			value = rvalue % len(flist)
		else:
			value = rvalue

		removed = flist.pop(value - 1)

		#print(f"{removed} is removed")

		#print(*flist)

		for m in range(value-1):
			flist.append(flist[0])
			flist.pop(0)

	flamesdict = {
		"F" : "Friend",
		"L" : "Love",
		"A" : "Affection",
		"M" : "Marriage",
		"E" : "Enemy",
		"S" : "Sister"
	}

	print(f"\n{flamesdict[flist[0]]}")

if __name__ == "__main__":
	main()




