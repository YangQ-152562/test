## Python Lesson 1.1
# import math
#
# f1 = 20
# f2 = 10
# alpha = math.pi / 3
#
# x_force = f1 + f2 * math.sin(alpha)
# y_force = f2 * math.cos(alpha)
#
# force = math.sqrt(x_force * x_force + y_force ** 2)
#
# print("result is ", round(force), 'N')

# Python Lesson 1.2
# name = input("input name :")
# age = input("input age :")
#
# after_age = int(age) + 10
#
# print("your name is " + name)
# print("after 10 years, your age is " + str(after_age))

'''Lesson3 计算圆面积'''
# import math
#
# r = input("input R :")
#
# result = math.pi * int(r) * int(r)
#
# print(result)


# '''Lesson4 凯撒密码'''
# r = input("input a char")
#
# # 偏移量
# n = 3
#
# r = ord(r) + n
#
# print(chr(r))

# '''lesson5 字母大小写转换 '''
# word = input("input a word : ")
# new_lst = []
# for i in word:
#     if i.islower():
#         x = i.upper()
#     else:
#         x = i.lower()
#
#     new_lst.append(x)
#
# new_word = "".join(new_lst)
# print(new_word)

'''lesson6 数字换英文'''

num = input("input a num: ")
num_lst = str(num)
eng_lst = []
for i in num_lst:
    if i == '1':
        eng_lst.append('one')
    elif i == '2':
        eng_lst.append('two')
    elif i == '3':
        eng_lst.append('three')
    elif i == '4':
        eng_lst.append('four')
    elif i == '5':
        eng_lst.append('five')
    elif i == '6':
        eng_lst.append('six')
    elif i == '7':
        eng_lst.append('seven')
    elif i == '8':
        eng_lst.append('eight')
    elif i == '9':
        eng_lst.append('nine')
    elif i == '0':
        eng_lst.append('zero')
    else:
        print("wrong input")
        break

eng = " ".join(eng_lst)
print(eng)
