def days_to_YMD(n):
    a=n
    y=a//365
    rmd=a%365
    m=rmd//30
    d=rmd%30
    print(a,"days is",y,"years",m,"Months",d,"Days")

days=int(input("Enter the no. of days:"))
days_to_YMD(days)



