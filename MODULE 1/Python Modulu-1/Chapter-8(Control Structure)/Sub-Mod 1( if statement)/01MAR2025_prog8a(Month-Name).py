# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif  (Home  work)
try:
	a = int(input('Enter month number (1 - 12): '))
	if  a == 1:
		print('January')
	elif  a == 2:
		print('Febraury')
	elif  a == 3:
		print('March')
	elif  a == 4:
		print('April')
	elif  a == 5:
		print('May')
	elif  a == 6:
		print('June')
	elif  a == 7:
		print('july')
	elif  a == 8:
		print('August')
	elif  a == 9:
		print('September')
	elif  a == 10:
		print('October')
	elif  a == 11:
		print('November')
	elif  a == 12:
		print('December')
	else:
		print('Input  should  be  between  1  and   12')
except:
		print('Input  should  be  an  integer')
