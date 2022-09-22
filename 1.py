# 3. Напишите программу, удаляющую из текста все слова, содержащие "abc".
# Входные и выходные данные первой и четвертой задач хранятся в отдельных текстовых файлах.

data = open('1Task.txt', 'r')
data_final = open('1Task_f.txt', 'w')

for line in data:
    line_f = (" ".join(filter(lambda x: "abc" not in x, line.split())))
    data_final.write(line_f)

data.close()
data_final.close()

