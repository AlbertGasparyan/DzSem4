# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

with open("G:\Python\PytSem4\DzTask\Task05_1.txt",'r') as file:
    num1=file.read()
    num2=num1[0:-4]

with open("G:\Python\PytSem4\DzTask\Task05_2.txt",'r') as file:
    num1=file.read()

with open("G:\Python\PytSem4\DzTask\Task05.txt",'w', encoding='utf-8') as file:
    file.write(f'{num1}+{num2}')