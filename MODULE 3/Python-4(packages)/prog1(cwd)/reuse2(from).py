#  Save  in  any  file  of  cwd  (Homework)  --->   Don'r  run
from p1 import mod1 , mod2  #How  to  import  mod1   and  mod2  of  package  p1  with  from  statement
print(mod1 . x) # How  to  print  variable  'x'  of   mod1  in  package  p1
mod1 . f1() # How  to  call  function  f1()  of   mod1  in  package  p1
a = mod1 . c1()
a . m1() #How  to  call  method  m1()  of   class  c1  in  mod1  of  package  p1
print()
print()
print(mod2 . x) # How  to  print  variable  'x'  of   mod2  in  package  p1
mod2 . f1() # How  to  call  function  f1()  of   mod2  in  package  p1
a = mod2 . c1()
a . m1()  #   How  to  call  method  m1()  of   class  c1  in  mod2  of  package  p1
#print(p1 . mod1 . x)  # Error :  p1 package is not imported
#print(x) #  Error :  No variable  'x'  in current module

'''
10
p1  --->  mod1   --->  f1  function
p1  ---> mod1  ---> c1  ---> m1 method
20
p1  ---> mod2  ---> f1
p1  ---> mod2 ---> c1 ---> m1
'''