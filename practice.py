
# person = {'이름':'나귀욤', '나이':7,'키':120,'몸무게':23}

# print(person['이름'])

# print(person.get('별명'))

# person['최종학력'] = '유치원'

# print(person['최종학력'])

# person['키'] = 130  #키가 자랐어요


# print(person['키'])

# person.update({'키':140, '몸무게':26}) #키와 몸무게가 자랐어요

# print('키는 ', person['키'], '이고 몸무게는 ',person['몸무게'], '이다')

# person.pop('몸무게')

# #person.clear()

# print(person.keys())

# print(person.values())

# print(person.items())

# my_tuple = ('오예스','몽셀') 
# my_list=list(my_tuple) 

# my_dic = dict.fromkeys(my_list) 

# today = '화요일'
# if today == '일요일':
#     print('게임한판')
#     if today == '금요일':
#         print('test')

# elif today == '수요일':
#     print('운동하자')

# else:
#     print('폰 5분만')
# print('공부시작')


# yellow_card = 0
# foul = False

# if foul:
#     yellow_card +=1
#     if yellow_card ==2:
#         print('경고누적 퇴장')
#     else:
#         print('휴..조심해야지')
# else:
#     print('주의')


# for x in range(10):
#  print(f'x')

# from copy import copy

# a= [1,2,3]

# b= copy(a)

# print(b)

# print(b is a)

# (a, b) = 'python', 'life'

# [a, b] = ['python', 'life']

# a = b ='python'

# n = 3
# m = 5
# n,m = m,n
# print(n)
# print(m)

# print((80+75+55)/3)

# if 14%2 == 1 :
#     print('13은 홀수이다')
# else :
#     print('13은 짝수이다')

# pin = '881120-1068234'
# yyyymmdd = '19' + pin[0:6]
# num = pin[7:]
# print(yyyymmdd)
# print(num)
# print(pin[7])


# a= "a:b:c:d"
# b = a.replace(":","#")
# print(b)

# c= [1,3,5,4,2]
# print(c)
# c.sort()
# print(c)
# c.reverse()
# print(c)

# a= ['Life', 'is','too','short']
# result= " ".join(a)
# print(result)

# pocket = ['paper','cellphone']
# card = True
# if 'money' in pocket :
#     print("택시를 타고 가라")
# else:
#     if card :
#         print("택시를 타고 가라")
#     else:
#         print("걸어가라")


# pocket = ['paper','cellphone']
# card = True
# if 'money' in pocket:     print("택시를 타고 가라")
# elif card:     print("택시를 타고 가라")
# else:     print("걸어가라")

score = 50

# if score >=60:
#     message = "success"
# else:
#     message = "failure"


# message = "success" if score >=60 else "failure"
# print(message)

# treeHit = 0
# while treeHit <10:
#     treeHit = treeHit +1
#     print("나무를 %d번 찍었습니다" % treeHit)
#     if treeHit == 10:
#         print("나무 넘어갑니다.")

# number = 0
# while number !=4:
#         print(prompt)
#         number = int(input())

# coffee = 10
# money = 300
# while money:
#     print("돈을 받았으니 커피를 줍니다.")
#     coffee = coffee-1
#     print("남은 커피의 양은 %d개입니다"%coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
#         break


# coffee = 10
# while True :
#     money = int(input("돈을 넣어주세요:"))
#     if money == 300:
#         print("커피를 줍니다.")
#         coffee = coffee-1
#     elif money >300:
#         print("거스름돈 %d를 주고 커피를 줍sl다."%(money-300))
#         coffee = coffee-1
#     else:
#         print("돈을 다시 돌려 주고 커피를 주지 않습니다.")
#         print("남은 커피의 양은 %d 개 입니다."% coffee)
#     if coffee == 0:
#         print("커피가 다 떨어졌습니다. 판매를 중단합니다.")
#         break


# a = 0
# while a <10:
#     a =a +1
#     if a%2 ==0: continue
#     print(a)

# while True:
#     print("Ctrl+C를 눌러야 While 문을 빠져나갈 수 있습니다.")

# test_list = ['one','two','three']
# for i in test_list :
#     print(i)

# a= [(1,2),(3,4),(5,6)]
# for (first,last) in a : 
#     print(first +last)



# marks = [90, 25, 67, 45, 80]

# number = 0
# for mark in marks:
#     number = number +1
#     # if mark >= 60:
#     #     print("%d번 학생은 합격입니다." %number)
#     # else :
#     #     print("%d번 학생은 불합격입니다."%number)

#     if mark <= 60:
#         continue
#     print("%d번 학생 축하합니다. 합격입니다."%number)

# add = 0
# for i in range(1,11):
#     add = add+i
#     print(add)
    
# marks = [90, 25, 67, 45, 80]
# for number in range(len(marks)):
#     if marks[number] <60:
#         continue
#     print("%d번 학생 축하합니다. 합격입니다." %(number +1))



# for i in range(2,10):
#     for j in range(1,10):
#         print(i*j,end=" ")
    #print('')
        
#a= [1,2,3,4]
# result = []
# for num in a:
#     result.append(num*3)

# print(result)
# result = [num*3 for num in a]
# print(result)

# result = [num*3 for num in a if num%2 ==0]
# print(result)

# result = 0
# i = 1
# while i <=1000:
#     if i%3 == 0 :
#         result +=i
#     i+=1
# print(result)


# i = 0
# while True:
#     i +=1
#     if i >5 : break
#     print("*"*i)

# for i in range(1,101):

# A = [70, 60, 55, 75, 95, 90, 80, 80,85, 100]
# total = 0
# for score in A :
#     total += score
# average = total/len(A)
# print(average  )

# numbers= [1,2,3,4,5]
# # result = []
# # for n in numbers:
# #     if n %2 == 1:
# #         result.append(n*2)


# result = [ n*2 for n in numbers if n %2 == 1]
# # for n in numbers:
# #     if n %2 == 1:
# #         result.append(n*2)
# print(result)

def add(a,b):
    return a +b

# a = 3
# b = 4
# c = add(a,b)
# print(c)

# def add(a,b):
#     return a +

# print(add(3,4))

# def add(a,b):
#     result = a+b
#     return result

# def say():
#     return 'Hi'

# a = say()
# print(a)


# def sub(a,b):
#     return a-b

# result = sub(a=7,b=3)
# print(result)

# result = sub(b=5, a=3)
# print(result)


# def add_many(*args):
#     result = 0
#     for i in args:
#         result = result + i
#     return result

# print(add_many(1,2,3))


# def add_mul(choice,*args):
#     if choice == "add":
#         result = 0
#         for i in args:
#             result = result + i
#     elif choice == "mul":
#         result = 1
#         for i in args:
#             result = result * i
#     return result

# result1 = add_mul("add",1,2,4)

# print(result1)


# def print_Kwargs(**Kwargs):
#     print(Kwargs)

# print_Kwargs(a=1)
# # print_Kwargs(name='foo',age=3)

# def add_and_mul(a,b):
#     return a+b, a*b
# result1, result2 = add_and_mul(3,4)

# print(result1, result2)

# def say_nick(nick):
#     if nick == "바보" :
#         return
#     print("나의 별명은 %s입니다." % nick)

# say_nick("야호")

# def say_myself(name,age,man=True) : 
#     print("나의 이름은 %s 입니다."%name)
#     print("나이는 %d살 입니다."%age)

#     if man:
#         print("남자입니다.")
#     else:
#         print("여자입니다.")

# say_myself("고한수",32,False)

# a= 1
# def vartest():
#     global a
#     a = a +1


# vartest()
# print(a)

# add = lambda a,b:a+b
# result = add(3,4)
# print(result)

# a = input()

# print(a)
 
# number  = input("숫자를 입력하세요: ")
# print(number)

# for i in range(10):
#     print(i, end=' ')

# f= open("새파일.txt", 'w')
# f.close()

# f=open("C:/Users/Hansu/Desktop/새 폴더/새파일.txt",'w')
# f.close()

# f=open("C:/doit/복습.txt","w")
# f.close()

# f = open("C:/doit/새파일.txt","w")
# for i in range(1,11):
#     data="%d번째 줄입니다.\n" %i
#     f.write(data)
#     print(data)
# f.close()

# f= open("C:/doit/새파일.txt",'r')
# while True:
#     line = f.readline()
#     if not line:break
#     print(line)
# f.close()


# f= open("C:/doit/새파일.txt",'r')
# lines = f.readlines()
# for line in lines:
#     line= line.strip()
#     print(line)
# f.close()


# f= open("C:/doit/새파일.txt",'r')
# data = f.read()
# print(data)
# f.close()

# f = open("C:/doit/새파일.txt",'r')
# for line in f:
#     print(line)
# f.close()


# with open("C:/doit/새파일.txt",'a') as f:
#     for i in range(11,20):
#         data = "%d번째 줄입니다.\n" %i
#         f.write(data)


# import sys

# args = sys.argv[1:]
# for i in args:
#     print(i.upper(),end = '')

# import random

# def random_pop(data):
#     number = random.choice(data)
#     data.remove(number)
#     return number

# import itertools

# student = ['한민서','황지민','이영철','이광수','김승민']
# snacks = ['사탕', '초콜릿', '젤리']

# result = itertools.zip_longest(student,snacks, fillvalue='새우깡')
# print(list(result))


# def add(data):
#     result = 0
#     for i in data:
#         result += i
#     return result

# data = [1,2,3,4,5]
# result = add(data)
# print(result)

# import functools

# data = [1,2,3,4,5]
# result =functools.reduce(lambda x, y:x+y,data)
# print(result)

# num_list = [3,2,8,1,6,7]
# max_num = functools.reduce(lambda x,y: x if x>y else  y,num_list)
# print(max_num)

# from operator import itemgetter
# from operator import attrgetter


# students = [ 
#     ("jane", 22,'A'),
#     ("dave",32,'B'),
#     ("sally",17,'B'),
# ]

# students = [
#     {"name":"jane", "age":22,"grade":'A'},
#     {"name":"dave", "age":32,"grade":'B'},
#     {"name":"sally", "age":17,"grade":'B'},
# ]

# class Student:
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age =age
#         self.grade = grade

# students = [
#     Student('jane',22,'A'),
#     Student('dave',32,'B'),
#     Student('sally',17,'B'),
# ]

# print(students.)
# result = sorted(students,key=attrgetter('age'))
# print(result)


# import shutil

# # shutil.copy("c:/doit/a.txt","c:/temp/a.txt.bak")

# shutil.move("c:/doit/a.txt","c:/temp/a.txt.bak")

# import zipfile

# # #파일 합치기
# # with zipfile.ZipFile('mytext.zip','w') as myzip:
# #     myzip.write('a.txt')
# #     myzip.write('b.txt')
# #     myzip.write('c.txt')

# # #해제하기
# # with zipfile.ZipFile('mytext.zip')as myzip:
# #     myzip.extract('a.txt')

# #압축하여 묶기
# with zipfile.ZipFile('mytext.zip','w',compression=zipfile.ZIP_LZMA, compresslevel=9) as myzip:
#     myzip.write('a.txt')
#     myzip.write('b.txt')
#     myzip.write('c.txt')

# import time
# import threading

# def long_task():
#     for i in range(5):
#         time.sleep(1)
#         print("working:%s\n" %i)

# print("Start")

# threads = []
# for i in range(5) :
#     # long_task()
#     t= threading.Thread(target=long_task)
#     threads.append(t)

# for t in threads:
#     t.start()

# for t in threads:
#     t.join() 

# print("End")

# import traceback

# def a ():
#     return 1/0

# def b():
#     a()

# def main():
#     try:
#         b()
#     except:
#         print("오류가 발생했습니다.")
#         print(traceback.format_exc())
# main()


# a = [1, -2, 3, -5, 8, -3]

# filtered_number = list(filter(lambda x: x >= 0, a))

# print(filtered_number)

# a= [1,-2,3,-5,8,-3]

# filtered_number = list(filter(lambda x : x >0, a ))

# print(filtered_number)

# a = 'ea'
# b = int(a,16)
# print(b)

# a = [1,2,3,4]
# b = list(map(lambda x : x*3,a))
# print(b)


# a = [-8,2,7,5,-3,5,0,1]

# max_num =0
# min_num =10

# for i in a :
#     if i > max_num:
#         max_num = i
#     if i < min_num:
#         min_num = i


        

# print('최대값은 {}이고 최소값은 {} 이며 이 둘의 합은 {}이다'.format(max_num,min_num, (max_num+min_num)))
# # print('최대값은 %d이고 최소값은 %d 이며 이 둘의 합은 %d이다' % max_num % min_num % (max_num+min_num))
# print('둘의 합은 {}이다'.format(min(a) + max(a)))

# import os 

# def search(dirname):
#     try : 
#         filenames = os.listdir(dirname)
#         for filename in filenames:
#             full_filename = os.path.join(dirname,filename)
#             if os.path.isdir(full_filename) :
#                 search(full_filename)
            
#             else:
#                ext = os.path.splitext(full_filename)[-1]
#                if ext == '.py':
#                     print(full_filename)
    
#     except PermissionError:
#         pass
# search("c:/")


# import os

# for (path, dir, files) in os.walk("c:/") :
#     for filename in files :
#         ext = os.path.splitext(filename)[-1]
#         if ext == '.py':
#             print("%s%s" % (path, filename))

# with open('euc_kr.txt', encoding='euc-kr') as f:
#     data = f.read()

#     data = data + "\n" + '테스트'

# with open('euc_kr.txt', encoding = 'euc-kr',mode ='w') as f :
#     f.write(data)  

# -*-coding:utf-8 -*-


# class Mul:
#     def __init__(self,m):
#         self.m = m
    
#     def mul(self,n):
#         return self.m*n
    
# if __name__ == "__main__" :
#     mul3 = Mul(3)
#     mul5 = Mul(5)

#     print(mul3.mul(10))
#     print(mul5.mul(10))


# class Mul:
#     def __init__(self,m):
#         self.m = m

#     def __call__(self,n):
#         return self.m*n
    
# if __name__ == "__main__" :
#     mul3 = Mul(3)
#     mul5 = Mul(5)

#     print(mul3(10))
#     print(mul5(10))


# def mul(m):
#     def wrapper(n):
#         return m*n
#     return wrapper

# if __name__ == "__main__" :
#     mul3 = mul(3)
#     mul5 = mul(5)

#     print(mul3(10))
#     print(mul5(10))

# import time

# def myfunc():
#     start = time.time()
#     print("함수가 실행됩니다.")
#     end = time.time()
#     print("함수 수행 시간 : %f 초" % (end -start))


# myfunc()


# import time

# def elapsed(original_func):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         result = original_func(*args, **kwargs)
#         end = time.time()
#         print("함수 수행 시간 : %f초" % (end - start))
#         return result
#     return wrapper



# @elapsed
# def myfunc(msg):
#     print("'%s' 을 출력합니다." % msg)

# # decorated_myfunc = elapsed(myfunc)
# # decorated_myfunc()

# myfunc("you need python")


# class MyIterator :
#     def __init__(self, data):
#         self.data = data
#         self.position = 0

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.position >= len(self.data):
#             raise StopIteration
#         result = self.data[self.position]
#         self.position +=1
#         return result
    
# if __name__ == "__main__" :
#     i = MyIterator([1,2,3])
#     for item in i :
#         print(item)



# class ReverseItertor :
#     def __init__(self,data):
#         self.data = data
#         self.position = len(self.data) -1
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         if self.position <0 :
#             raise StopIteration
#         result = self.data[self.position]
#         self.position -=1
#         return result
    


# if __name__ == "__main__":
#     i = ReverseItertor([1,2,3])
#     for item in i:
#         print(item)


# def mygen():
#     for i in range(1,1000):
#         result = i * i
#         yield result


# gen = mygen()


# gen = (i*i for i in range(1,1000))

# print(next(gen))
# print(next(gen))
# print(next(gen))

# class MyIterator:
#     def __init__(self):
#         self.data = 1

#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         result = self.data*self.data
#         self.data += 1
#         if self.data >= 1000:
#             raise StopIteration
#         return result


# import time

# def longtime_job():
#     print("job start")
#     time.sleep(1)
#     return "done"

# list_job = (longtime_job() for i in range(5))
# # print(list_job[0])
# print(next(list_job))

# num : int = 1

# def add(a:int, b:int) ->int:
#     return a +b


# result = add(3,3.4)
# print(result)

# import re

# data = """
# park 800905-1049118
# kim 700905-1059119
# """

# pat = re.compile("(\d{6})[-]\d{7}")
# print(pat.sub("\g<1>-*******", data))


# A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

# result =0

# while A :
#     mark = A.pop()
#     if mark >= 50 :
#         result += mark

# print(result)


# def fib(n):
#     if n == 0 : return 0
#     if n == 1 : return 1
#     return fib(n-2) + fib(n-1)

# for  i in range(10):
#     print(fib(i))


# user_input = input("숫자를 입력하세요 : ")
# numbers = user_input.split(",")

# print(numbers)
# total = 0
# for n in numbers:
#     total +=int(n)
# print(total)


# gugu_number = input("구구단 숫자를 입력하세요(2~9) : ")

# for i in range(1,10):
#     print(int(gugu_number)*i, end=' ')

# f = open('abc.txt', 'r')
# lines = f.readlines()
# f.close()
# lines.reverse()

# f = open('abc.txt','w')
# for line in lines:
#     line = line.strip()
#     f.write(line)
#     f.write('\n')
# f.close()

# f = open('sample.txt', 'r')
# lines = f.readlines()
# f.close()

# sum = 0

# f = open('result.txt','w')
# for line in lines:
#     sum += int(line)
# avg = sum/len(lines)

# f.write("합은 :")
# f.write(str(sum))
# f.write('\n')
# f.write("평균은 :")
# f.write(str(avg))
# f.close()

# print ("합은 : ",sum)
# print("평균은 : ",avg)

# class Calculator :
#     def __init__(self, numberList):
#         self.numberList = numberList

#     def sum (self) :
#         result = 0
#         for num in self.numberList :
#             result += num
#         return result
    
#     def avg(self) :
#         total = self.sum()
#         return total/len(self.numberList) 

# cal1 = Calculator([1,2,3,4,5])
# cal1.sum()
# print(cal1.sum())
# print(cal1.avg())

# cal2 = Calculator([6,7,8,9,10])
# cal2.sum()
# print(cal1.sum())
# print(cal1.avg())


# data  = "4546793"
# numbers = list(map(int,data))
# result = []

# for i, num in enumerate(numbers):
#     result.append(str(num))
#     if i < len(numbers) - 1 :
#         is_odd = num %2 == 1
#         is_next_odd = numbers[i+1]%2 ==1
#         if is_odd and is_next_odd :
#             result.append("-")
#         elif not is_odd and not is_next_odd:
#             result.append("*")

# print("".join(result))


# def compress_string(s):
#     _c = ""
#     cnt = 0
#     result = ""
#     for c in s :
#         if c != _c:
#             _c = c
#             if cnt: result +=str(cnt)

#             result += c
#             cnt = 1
#         else :
#             cnt += 1
#     if cnt: result +=str(cnt)

#     return result

# print(compress_string("aaabbcccccca"))


# def compress_string(s):
#     _c = ""
#     cnt = 0
#     result = ""
#     for c in s:
#         if c !=_c:
#             _c = c
#             if cnt : result +=str(cnt)

#             result += c
#             cnt = 1
#         else :
#             cnt += 1
#     if cnt: result += str(cnt)

#     return result

# print(compress_string("aaabbcccccca"))


# def chk_dup_numbers(s):
#     result = []
#     for num in s :
#         if num not in result :
#             result.append(num)

#         else:
#             return False
        
#     return len(result) == 10
    
# print(chk_dup_numbers("0123456789"))
# print(chk_dup_numbers("01234"))
# print(chk_dup_numbers("01234567890"))
# print(chk_dup_numbers("6789012345"))
# print(chk_dup_numbers("012322456789"))


# def morse(src):
#     result = []
#     for word in src.split("  "):
#         for char in word.split(" "):
#             result.append(dic[char])
#         result.append(" ")
#     return "".join(result)


# import csv


# with open('C:/Users/rhgks/Desktop/code_drill/Git/Python/Practice/contry.csv','r') as f :
#     reader = csv.reader(f)


#     # next(reader)
#     #객체 확인
#     print(reader)
#     #타입 확인
#     print(type(reader))
#     #속성 확인
#     print(dir(reader)) #__iter__
#     print()

#     for c in reader:
#         # print(c)
#         print(' : '.join(c))



# with open('./contry.csv','r') as f :
#     reader = csv.reader(f,delimiter='|')

#     for c in reader:
#         print(c)



# with open('./contry.csv','r') as f :
#     reader = csv.DictReader(f)

#     #확인
#     print(reader)
#     print(type(reader))
#     print(dir(reader))

#     print()

#     for c in reader:
#         for k, v in c.items():
#             print(k,v)

#         print('---------------')

# w = [[1,2,3],[4,5,6],[7,8,9]]
# with open('./contry.csv','w', encoding ='utf-8') as f :
    
    
#     fields = ['One','Two', 'Three']

#     wt = csv.DictWriter(f,fieldnames=fields)
#     wt.writeheader()

#     for v in w:
#         wt.writerow({'One':v[0],'Two':v[1], 'Three' : v[2]})


#Chaprer 10-1
#Hangman(행맨) 미니 게임 제작(1)
#기본 프로그램 제작 및 테스트


import time

name = input("what is your name?")

print("Hi, " + name, "Time to play hangman game!")

print()

time.sleep(1)

print("Start Loading...")
print()
time.sleep(0.5)



# 정답 단어
word = "secret"


#추측 단어 
guesses = ''

#기회
turns = 10

# 핵심 While Loop
# 찬스 카운트가 남아 있는 경우
while turns > 0:
    #실패 횟수(단어 매치 수)
    failed = 0

    # 정답 단어 반복
    for char in word :
        # 정답 단어 내에 추측 문자가 포함되어 있는 경우
        if char in guesses:
            #추측 단어 출력
            print(char, end = '')
        else:
            # 틀린 경우 대시로 처리
            print("_", end='')
            failed +=1
        if failed == 0:
            print()
            print()
            print('Congratulation! The Guesses is correct.')
            #while 구문 중단
            break

        print()


        #추측 단어 문자 단위 입력
        print()
        guess = input("guess a charater.")

        # 단어 더하기
        guesses +=guess

        #정답 단어에 추측한 문자가 포함되어 있지 않으면
        if guess not in word:
            turns -=1
            # 오류 메세지
            print("Oops! Wrong")
            # 남은 기회 출력
            print("You have", turns, 'more guesses!')
            

            if turns == 0:
                # 실패 메시지
                print("You hangman game failed")

