import random #Модуль рандом
arr = [[random.randint(-10,10) for i in range(4)]for j in range(20)] #Список в диапозоне от -10 до 10, 20 случайных значений по 4 числа
arr_2 = [] #Список

count = 0 #Счетчик

x = int(input("Введите число: ")) #Запрашиваем число у пользователя     

for a in arr: #Цикл
    if a not in arr_2:
        arr_2.append(a) 
    
    if sum(a) < x: #Цикл
        count += 1
print(arr) #Вывод на экран
print(f"уникальные значения {tuple(arr_2)}") #Вывод на экран
print("Кол-во пар, чья сумма меньше:",count) #Вывод на экран