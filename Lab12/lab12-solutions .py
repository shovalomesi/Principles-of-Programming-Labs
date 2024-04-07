#Q1
def merge(s1, s2):
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    elif s1[0] < s2[0]:
        return [s1[0]]+ merge(s1[1:], s2)
    else:
        return [s2[0]]+ merge(s1, s2[1:])
#l1= [1,3,5,7,9]
#l2=[2,3,4,6,8,10]
#print (merge(l1,l2))
#Q2
def mergesort(lst):
          if len(lst) <= 1:
              return lst
          else:
              return merge(mergesort(lst[:len(lst)//2]),
                     mergesort(lst[len(lst)//2:]))
##lst=[1,19,3,10,5,3,9]            
##print (mergesort(lst))
#Q3
class Node:
    """
    Tree node: left and right child + data which can be any object
    """
    def __init__(self, data):
        """
        Node constructor

        @param data node data object
        """
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """
        Insert new node with data

        @param data node data object to insert
        """
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        else:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
                
    def print_tree(self):
        """
        Print tree content inorder
        """
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()
            
    def mirror(self):
        x=self.left
        self.left=self.right
        self.right=x
        if self.left is not None:
            self.left.mirror()
        if self.right is not None:
            self.right.mirror()
       
  
root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)
#root.print_tree()
root.mirror()
#print(" ")
#root.print_tree()
#print(" ")
#Q4
def isAnyOptionToSteal(n, weights):
    if n == 0: 
        return True
    if n<0:
        return False
    for i in weights:
        if isAnyOptionToSteal(n-i, weights):
            return True
    return False
        
##print(isAnyOptionToSteal(10, (4,3,2)))
##print(isAnyOptionToSteal(10, (4,)))


#Q5
def f(n):
    if n<3:
        return n
    else:
        return f(n-1)+f(n-2)+f(n-3)
    
#print(f(35))


def memo(function):
    cache={}
    def memoized(*args):
        if args not in cache:
            cache[args]=function(*args)
        return cache[args]
    return memoized

#f=memo(f)
#print(f(35))

#Q6
from operator import getitem

def make_rat(n, d):
    return (n, d)
 
def numer(x):
    return getitem(x, 0)
def denom(x):
    return getitem(x, 1)
def make(x):
        try:
            result = numer(x)/denom(x)
        except ZeroDivisionError:
            return "Attempted to divide by zero"
        else:
            return result
def str_rat(x):
	"""Return a string n/d for numerator n and denominator d."""
	return '{0}/{1}={2}'.format(numer(x), denom(x),make(x))
def main():
    n=input("Enter numer number:")
    d=input("Enter denom number:")
    ns=0.0
    try:
        num=int(n)
        den=int(d)
        ns=make_rat(num,den)
    except ValueError:
        #Handle the exception
        print ('Try again and press numbers \n')
    else:
        print( str_rat(ns))
      
#main()
#Q7
class WrongGradeFormat(ArithmeticError):
    def __init__(self, curr_avg):
        self.avg = curr_avg

def avg_grade(filename):
    out = None
    try:
        out=open(filename,"r");
        total=0
        count=0
        grade=out.readlines()
        for s in grade:
            temp=int(s)
            if temp<0:
                raise WrongGradeFormat(0 if count==0 else total/count)
            total+=temp
            count+=1
        return 0 if count==0 else total/count
    except IOError:
        print("Error opening file")
    except ValueError:
        raise WrongGradeFormat(0 if count==0 else total/count)      
    finally:
        if out:
            out.close()
 
def test2(*args):
    for name in args:
        try:
            print(avg_grade(name))
        except WrongGradeFormat as e:
            print('The average partially calculated: ', e.avg)
        except ZeroDivisionError as ze:
            print(str(ze))

  
def driver():
   #print(avg_grade("data.txt"))
   test2('data1.txt','data2.txt')


#driver()

