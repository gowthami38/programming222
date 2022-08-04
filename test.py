# if -1>=0:
#     print("postive number ")
# else:
#     print("negvtie number")

# if 8<3:
#     print("India")
# elif 4>5:
#     print("Aus")
# elif 4==0:
#     print("both are equal")
# else:
#     print("all are false")
#
# my_lsit =[1,2,3,4,5,6,7,8,9]
# if 5 in my_lsit:
#     print(my_lsit[4])
# else:
#     print(0)
# my_tuple=(45,56373,8488)
# if 32 in my_tuple:
#     print("true")
# else:
#     print("false")
import time


# for item in [1,2,3,4,5,6,7]:
#     print(item)
#     time.sleep(0.5)
# stat_time=time.time()
# my_lsit =[1,2,3,4,5,6,7,8,9]
# if 5 in my_lsit:
#     print(my_lsit[4])
# else:
#     print(0)
# time.sleep(0.5)
# end_time=time.time()
# print("{} program took sec".format(end_time-stat_time))
#
# stat_time=time.time()
# mylist=[1,2,3,4,5,6,7,8,9]
# print(mylist[4])
# time.sleep(1)
# end_time=time.time()
# print("{}took sec".format(end_time-stat_time))
# stat_time=time.time
# my_tuple=range(50)
# for item in my_tuple:
#     print(item,end=" ")
#     time.sleep(0.2)
# end_time=time.time()
# print("{} program took time".format(end_time-stat_time))

# tsrlist = range(15)
# for item in tsrlist:
#     if item %2==0:
#         print("Enven number")
#     else:
#         print("odd number")

# def function_define_add(a,b):
#     print("welcomet to fuction is {}".format(a+b))
# function_define_add(20,30)
#
# def tsr(c,d):
#     return c+d
# print(tsr(234,456))
#
# def add_surname(name):
#     return (name+  " reddy")
# print(add_surname("sasidhar" ))
# import time
# stat_time =time.time()
# def add(first, middle):
#     return(first + middle + " reddy")
# time.sleep(2)
# print(add("sasi","dhar"))
# end_time=time.time()
# print("{}took sec".format(end_time-stat_time))
# import time
# start_time=time.time()
# mytsr=[item for item in range(50) if item %5==0]
# time.sleep(1)
# print(mytsr)
# time.sleep(1)
# end_time =time.time()
# print(end_time-start_time)
#
# def multiplation (tsr,ysr):
#     return tsr +ysr
# print(multiplation(4567,4567))
#
# def division (www,rrr):
#     return www/rrr
# print(division(234567,56))


# tsrList=range(100)
# for item in tsrList:
#     if item %7==0:
#         print(item, end=" ")
#     else:
#         print(item)
#
# myList=[item for item in tsrList if item %2==0]
# print(myList)


# n=(int(input("Enter the n value:- ")))
# i=0
# while i<=n:
#     print(i,end=" ")
#     i=i+1

# try:
#     def add (sasi,gowthami):
#         print("type of sasit is",type(sasi))
#         print("type of gowthami is",type(gowthami))
#         if type(sasi)==int and type (gowthami)==int:
#             print("addition sasi+gowthami",sasi+gowthami)
#         else:
#             if type(sasi) != int:
#                 print("please Enter the value int type only")
#             if type(gowthami) != int:
#                 print("please Enter the value int type only")
# except:
#     print("there is error")
# else:
#     print("no error")
# finally:
#     print("defaulty allways runs")
# add(78,99)

#
# def add():
#     x = 10
#     y = 20
#     print(x + y)
# add()
#
# a=100
# x=500
# def addition():
#     a=200
#     b=200
#     print(a+b)
#     def tsr():
#         print("a value is {}".format(a))
#         def sss():
#             print("b value is {}".format(b))
#             def ttt():
#                 print("enclose value is {}".format(b))
#                 def ttd():
#                     global x
#                     print("global value is {}".format(x))
#                     print("type of the value{}".format(type(x)))
#                     def zzz():
#                         print("enclosing value is {}".format(x))
#                         def ppp():
#                             print("enclosing value is {}".format(x))
#                         ppp()
#                     zzz()
#                 ttd()
#             ttt()
#         sss()
#     tsr()
# addition()

# import time
# start_time=time.time()
#
# class company:
#     def __init__(self,n,a,m,s,g):
#         self.name=n
#         self.age=a
#         self.mobileNo=m
#         self.salary=s
#         self.gender=g
#     def fun(self):
#         print("name is {}".format(self.name))
#     def tsr(self):
#         print("age is {}".format(self.age))
#     def ysr(self):
#         print("mobileNo is {}".format(self.mobileNo))
#     def kcr(self):
#         print("salary is {}".format(self.salary))
#     def rrr(self):
#         print("gender is {}".format(self.gender))
#     def ttt(self, a):
#         return a
# sasi=company("gowthami",23,7097535317,30000,"male")
# print(sasi.name,sasi.age,sasi.mobileNo,sasi.salary,sasi.gender)
# print(sasi.ttt("chittoor"))
# sasi.fun()
# sasi.tsr()
# sasi.ysr()
# sasi.kcr()
# sasi.rrr()
#
# sasi=company("jai",56,456789456,2347,"male")
# print(sasi.name,sasi.age,sasi.mobileNo,sasi.salary,sasi.gender)
# print(sasi.ttt("tirupati"))
# end_time=time.time()
# print("{} took sec".format(end_time-start_time))

#                           single inheritance

# class parent:
#     last_name="reddy"
# class child(parent):
#     middle_name="sasidhar"
# obj=child()
# print(obj.last_name)
# print(obj.middle_name)

# # multi level
# class p:
#     welcome ="welcome to class function"
# class c(p):
#     python="welcome to python programming"
# class d(c):
#     sasidhar="programming"
# class f(d):
#     gowthami="welcome"
# class e(f):
#     last_name="rrr"
# class g(e):
#     middle_name="ttt"
# class h(g):
#     first_name="yyy"
# tsr=h()
# print(tsr.first_name)
# print(tsr.welcome)
# print(tsr.middle_name)
# print(tsr.welcome)
# print(tsr.last_name)
# print(tsr.python)
# print(tsr.sasidhar)

#multipul
# class dad:
#     parent_name="raja reddy"
# class mom:
#     parent2_name="bhanu"
# class sasi(mom,dad):
#     childName="sasidhar reddy"
# tsr=sasi()
# print(tsr.childName)
# print(tsr.parent2_name)
# print(tsr.parent_name)
#
# class parent():
#     full_name="t raja reddy"
# class child(parent):
#     child_name="sasi"
# class child1(parent):
#     child1_name="mohan"
# class child2(parent):
#     child2_name="jai"
# class child3(parent):
#     cheild3_name="sagar"
# rrr=child()
# print(rrr.child_name)
# print(rrr.full_name)
# rrr=child3()
# print(rrr.)