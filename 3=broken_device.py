#ОЧЕНЬ ДОЛГО РЕШАЛ!!!!! только рекурсия поможет!!! и еще ухитриться пришлось мне!!!! не знаю почему!!!
'''
задача по тесту на 30минут
ИСХОДНЫЕ ДАННЫЕ:
два числа (положительных, целых).
есть возможность отнимать единицу или умножать на 2.
НЕОБХОДИМО:
определить минимальное количество операций для перехода из 1го числа ко 2му!
'''
print("[[[[[[3=дваЧИСЛА[[[[[[\n")

recursion_level = 0

def broken_device(x, y):
    #global x    #ERROR=SyntaxError: name 'x' is parameter and global
    #xx=x
    #global xx   #ERROR=SyntaxError: name 'xx' is assigned to before global declaration
    global recursion_level  #OK

    yd2 = y/2 if y/2==y//2 else y//2+1
    count_operations = 0

    while x != y:
        if x > y:
            x -= 1
            count_operations += 1
        elif x > yd2:
            x -= 1
            count_operations += 1
        elif x == yd2:
            x *= 2
            count_operations += 1
        elif x < yd2:
            recursion_level += 1
            [count_operations_add, x] = broken_device(x, yd2)
            count_operations += count_operations_add
            recursion_level -= 1

    if recursion_level > 0:
        return [count_operations, x]
    else:
        return count_operations

print(broken_device(1, 1), "=0")
print(broken_device(1, 3), "=3")
print(broken_device(2, 3), "=2")
print(broken_device(5, 8), "=2")
print(broken_device(5, 10), "=1")
print("\n]]]]]]finish]]]]]")