money = True
if money : 
    print('돈이 있다.')
else :
    print("돈이 없다.")

money = 30000

if money > 30000 :
    print('돈이 30000원 보다 많이 있다.')
elif money == 30000 : 
    print('돈이 30000원 있다.')
else :
    print('돈이 없다.')

grade = 96
if grade > 90 :
    print("A")
elif grade > 80 :
    print("B")
else :
    print("C")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket :
    print("택시를 타고가라")
elif card :
    print("택시를 타고가라")
else :
    print("걸어가라")

a = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in a :
    if i%2 !=0 :
        print(i)

a = "안녕하세요. 저는 차현주입니다."
name = a.split()
for i in name :
    print(i)

for k in range(1,10):
    print('2 x ',k,'=', 2*k)
for y in range(1,10):
    print('3 x', y, "=", 3*y)