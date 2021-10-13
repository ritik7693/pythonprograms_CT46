m1=int(input("marks 0f 1st subject\n"))
m2=int(input("marks 0f 2nd subject\n"))
m3=int(input("marks 0f 3rd subject\n"))
if m1<33 or m2<33 or m3<33:
    print("fail!")
elif((m1+m2+m3)/3 < 40):
    print("fail!")
else:
    print("pass")
