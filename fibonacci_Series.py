# Fibonacci series or Sequences 
nterm=int(input("Enter the nterms value : "))
n1,n2=0,1; count=0
if nterm==0:
    print("Enter the some positive interger : ")
elif nterm==1:
    print("Fibonacci Series : ",n1)
else:
    while count<nterm:
        print(n1)
        nth=n1+n2
        n1=n2;n2=nth;count+=1