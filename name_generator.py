def generate_full_name(x, y):

	test = True

	if x == "" or y == "":
		return("At least one of your inputs was an empty string.")


	for a in x:
		if a.isalpha() == False:
			return("One of your inputs contained an invalid character.")
	for b in y:
		if b.isalpha() == False:
			return("One of your inputs contained an invalid character.")

	return(x + " " + y)
