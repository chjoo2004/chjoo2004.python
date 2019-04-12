a = "멋쟁이 사자처럼 화이팅 멋쟁이 사자"
b =  a.split( )
k = {}
for i in b :
    if i in k :
        k[i] = k[i]+1
    else :
        k[i] = 1
print(k)