# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

data = open('4Task.txt', 'r')
line1 = data.readline()
data_intermediate = open('4Task_i.txt', 'w')
data_final = open('4Task_f.txt', 'w')

def enc (string1):
    result1 = ''
    i = 0
    while i < len(string1):
        count = 1
        while i + 1 < len(string1) and string1[i] == string1[i+1]:
            count = count + 1
            i = i + 1
        result1 += string1[i] + str(count)
        i = i + 1
    return result1

print(enc(line1))

def decoding(string2):
    my_list = list(string2)
    result2 = ''
    for i in range(len(my_list)):
        if i % 2 == 0:
            tmp = my_list[i] * int(my_list[i+1])
            result2 = result2 + tmp
    return result2

print(decoding(enc(line1)))

data_intermediate.write(enc(line1))
data_final.write(decoding(enc(line1)))

data_final.close()
data_intermediate.close()
data.close()

