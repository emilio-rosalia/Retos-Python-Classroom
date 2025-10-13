# Reto 1 fizzbuzz
for i in range(100):
    if (i+1) % 2 !=0 and (i+1)%3 != 0:
        print(i+1)
    elif (i+1) % 2 ==0 and (i+1)%3 != 0:
        print('fizz')
    elif (i+1) % 2 !=0 and (i+1)%3 == 0:
        print('buzz')
    else:
        print('fizzbuzz')