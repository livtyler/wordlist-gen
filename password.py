#!/usr/bin/env python
from string import maketrans

a = []
with open ("passwords.txt", "r") as infile:
	for line in infile:
		line = line.strip()

		a.append(line)
		a.append(line[::-1])
		a.append(line.title())
		intab = "bBeEgGiIlLoOqQsStTzZ"
		outab = "88339911110099557722"
		trantab = maketrans(intab, outab)
		a.append(line.translate(trantab))
		for x in xrange(1900,2021):
			newpassword = line + str(x)
			a.append(newpassword)

with open ("results.txt", "w") as outfile:
	for result in a:
		outfile.write (result + "\n")