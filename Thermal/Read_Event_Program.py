def Read_Event_Program():
	tfile = open("program.txt")
	text = tfile.read()
	tfile.close()
	
	program_data = text.splitlines()
	for prog_row in range(len(program_data)):
		program_data[prog_row] = program_data[prog_row].split(',')
	
	#print program_data
	#print program_data[0][0]

	return program_data