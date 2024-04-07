Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
============== RESTART: C:\Users\finkm\Desktop\Lab5_samples.py ==============
>>> def f(x):
	return x+1

>>> type(f)
<class 'function'>
>>> f
<function f at 0x00000292EC3882F0>
>>> lambda x:x+1
<function <lambda> at 0x00000292EC388400>
>>> g=lambda x:x+1
>>> g
<function <lambda> at 0x00000292EC388378>
>>> type(g)
<class 'function'>
>>> f(3)
4
>>> g(3)
4
>>> (lambda x:x+1)(3)
4
>>> (lambda:1)()
1
>>> (lambda x,y,z:x+y+z)()
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    (lambda x,y,z:x+y+z)()
TypeError: <lambda>() missing 3 required positional arguments: 'x', 'y', and 'z'
>>> (lambda x,y,z:x+y+z)(1,2,3)
6
>>> (lambda x=0,y=1,z=2:x+y+z)()
3
>>> (lambda:print(1))()
1
>>> 
============== RESTART: C:\Users\finkm\Desktop\Lab5_samples.py ==============
44 48
>>> 
============== RESTART: C:\Users\finkm\Desktop\Lab5_samples.py ==============
44 48
55
44 48
>>> 
============== RESTART: C:\Users\finkm\Desktop\Lab5_samples.py ==============
Lambda+If- -15
>>> 
============== RESTART: C:\Users\finkm\Desktop\Lab5_samples.py ==============
Lambda+If- 15
>>> list1=[1,2,3,4]
>>> list1
[1, 2, 3, 4]
>>> type(list1)
<class 'list'>
>>> list1[0]
1
>>> list1[-1]
4
>>> list1[0]=100
>>> list1
[100, 2, 3, 4]
>>> for x in list1:
	print(x)

	
100
2
3
4
>>> for x in range(len(list1)):
	print(list1[x])

	
100
2
3
4
>>> 
============== RESTART: C:\Users\finkm\Desktop\Lab5_samples.py ==============
[18, 9, 24, 12, 27]
>>> range(5)
range(0, 5)
>>> list(range(5))
[0, 1, 2, 3, 4]
>>> 
============== RESTART: C:\Users\finkm\Desktop\Lab5_samples.py ==============
[14, 46, 28, 54, 44, 58, 26, 34, 64]
>>> 
