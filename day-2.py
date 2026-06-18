ODD_ARRAY=[]
EVEN_ARRAY=[]
def SplitArray(A):
    for i in A:
      if i%2==0:
        odd=ODD_ARRAY.append(i)
        
      else:
        even=EVEN_ARRAY.append(i)

A=[0,1,2,3,4,5,6,7,8,9] 
SplitArray(A)    
print("odd",ODD_ARRAY)
print("even",EVEN_ARRAY)    
