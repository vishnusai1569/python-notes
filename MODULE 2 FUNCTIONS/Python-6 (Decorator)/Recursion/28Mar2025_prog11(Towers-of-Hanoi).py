#  Towers  of  Hanoi
def  toh(n , p1 , p2 , p3):  # n  is  1 , p1  is  2 , p2  is  3 , p3  is  1
	if  n > 0:  #   at  least  one  disk:
		toh(n - 1 , p1 , p3 , p2)   # How  to  move  (n - 1)  disks  from   pole1  to  pole2  and  pole3  is  intermediate
		print(F'{p1} ---> {p3}')   # How  to  move  disk  from  pole1  to  pole3
		toh(n - 1 , p2 , p1 , p3)   	#  How  to  move  (n - 1)  disks  from   pole2  to  pole3  and  pole1  is  intermediate
# toh( 3 , 1 , 2 , 3)
n = int(input('How many disks ? :   '))
toh(n ,  1 , 2 , 3)  #  How  to  move  'n'  disks  from   pole1  to  pole3  and  pole2  is  intermediate



'''
What  are  1 , 2 , 3  called  ?  --->  Pole  numbers
'''
