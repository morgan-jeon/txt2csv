import json

with open("BACKUP.TXT", "r", encoding="utf-8") as f:
	ls = dict()
	for i in f.readlines():
		name = i.split('\t')[0].replace(' ','')
		number = i.split('\t')[1].replace(' ','').replace('8210','010')
		if name in ls.keys():
			if number == ls[name]:
				pass
			else:
				print(f'{name} Original: {ls[name]} New: {number}')
				y = input('replace? (Y/N) _ ')
				if y == "Y":
					ls[name] = str(number)
		else:
			ls[name] = str(number)

	print(f'TOTAL {len(ls)}')
print(ls)

with open("PHONEBOOK.JSON", 'w', encoding="utf-8") as outfile:
    json.dump(ls, outfile, ensure_ascii=False, indent="\t")

with open("NEWBACK.TXT", 'w', encoding="cp949") as file:
	for i in ls.keys():
		a = i+'\t'+ls[i]+'\t\n'
		file.write(a)