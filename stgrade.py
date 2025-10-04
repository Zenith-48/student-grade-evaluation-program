marks=int(input("enter marks"))
if marks>=90:
    print("grade A")
elif marks>=80:
    print("grade B")   
elif marks>=70:
    print("grade C")
elif marks>=60:
    print("grade D")
else:
    print("fail")
    m=int(input("enter marks of 1 subject"))
    n=int(input("enter marks of 2 subject"))
    o=int(input("enter marks of 3 subject"))    
    p=int(input("enter marks of 4 subject"))
    q=int(input("enter marks of 5 subject"))
    total=m+n+o+p+q/5
    print("average:",total)
    if total>=90:
        print("grade A")
    elif total>=80:
        print("grade B")   
    elif total>=70:
        print("grade C")
    elif total>=60:
        print("grade D")
    else:
        print("fail")