# -*- coding: utf-8 -*-
'''
@File    :   1111.py    
@Contact :   272575173@qq.com
@Author  :   Wuyz  
@Time    :   2020/5/9 15:15  
'''


# list=[{'code': 4026},{ 'msg': '用户名或密码有误'},{ 'time': 1589007911, 'data': []}]
#
# dict=dict(list)
# print(dict)
# list.sort()

# list=[4,1,5,3,6,33]
# for x in range(0,len(list)):
#     for z in range(x+1,len(list)):
#         if list[z]<list[x]:
#             list[z],list[x]=list[x],list[z]
# print(list)

# for x in range(len(list)):
#     for z in range(len(list)-1):
#         if list[z]>list[z+1]:
#             list[z],list[z+1]=list[z+1],list[z]
# print(list)
# #定义一个List，任意输入10个数字保存到List。
# lis = []
# for a in range(1,5):
#     number=int(input("请输入一个数字："));
#     lis.append(number);
# # 冒泡排序(从左往右推)
# temp = 0
# for cs in range(len(lis)):
#     for index in range(len(lis)-1):
#         if lis[index]>lis[index+1]:
#             lis[index], lis[index + 1] = lis[index + 1], lis[index]
#             # temp=lis[index]
#             # lis[index]=lis[index + 1]
#             # lis[index + 1]=temp
#
# print(lis)


# dict={'a':'b','c':'d'}
#
# str=str(dict)
# print(str,type(str))

'''7.实现学生管理系统,完成对学员的增,删,改,查和退出学生管理系统。
要求1：使用一个list用于保存学生的姓名。
要求2：输入0显示所有学员信息,1代表增加，2代表删除，
3代表修改，4代表查询，exit代表退出学生管理系统。
每一个功能定义一个自定义函数。界面如下：
系统界面如下：
-----------------------欢迎进入T666班学生管理系统-----------------------------
请选择系统功能：
0:显示所有学员信息
1:添加一个学员信息
2:删除一个学员信息
3:修改一个学员信息
4:查询一个学员信息
exit:退出学生管理系统


(0)输入0后效果如下：
	0
	["郭易","汤碗珍"..]

(1)输入1后效果如下：
	1
	请输入增加人的姓名：张三
	["郭易","汤碗珍",'张三'..]

(2)输入2后效果如下：
	2
	请输入删除人的姓名：张三
	["郭易","汤碗珍"..]

(3)输入3后效果如下：<注意：如果list中没有这个学员则打印：T666班没有这个学员>
	3
	请输入需要修改人的姓名：张三
	请输入需要修改后的姓名：李四
	["郭易","汤碗珍",'李四'..]

(4)输入4后效果如下：<注意：如果list中没有这个学员则打印：T666班没有这个学员>
	请输入查询人的姓名：张三
	郭易在座位号(3<下标>)的位置。

(5)输入exit后效果如下：
	exit
	欢迎使用T666的学生管理系统，下次再见。'''

# list=[7,8,6,9,11,26,58,95,99,22,11,44]
# # for x in range(len(list)):
# #     for y in range(len(list)-1):
# #         if list[y] > list[y+1]:
# #             list[y], list[y+1] = list[y+1], list[y]
# # print(list)
import os




