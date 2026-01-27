age=int(input("enter your age:"))
citizen=input("enter your country name:")
if(age>=18):
    if(citizen=="indian"):
        print("eligible to vote")
    else:
        print("citizen must be indian")
else:
    print("age must be greater than or equal to 18")       