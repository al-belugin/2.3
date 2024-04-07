list_ = ['BMW', 'MB', 'LADA', 'KIA', 'HONDA']

a = 'Я езжу на автомобиле марки'

for i in list_:
    print(a, i)

cars_cont = 0

for i in range (len(list_)):
    print(list_[i])

print (list_)


cars_cont = 0
for i in range (len(list_)):
    cars_cont += 10
print (cars_cont)