# -*- coding: utf-8 -*-
'''
@File    :   test0513.py    
@Contact :   272575173@qq.com
@Author  :   Wuyz  
@Time    :   2020/5/13 9:54  
'''
'''1.写函数，接收两个数字参数，返回最大值   例如：传入：10,20  返回：20 '''
def return_max_number(x,z):
    return  max(x,z)
print(return_max_number(10,20))

'''2.写函数，获取传入列表的所有奇数位索引对应的元素，并将其作为新列表返回。
例如：传入：[34,23,52,352,352,3523,5]   返回：[23,352,3523]'''
list=[34,23,52,352,352,3523,5]
def new_list(list):
    new_list = []
    for x in range(len(list)):
        if x%2!=0:
            new_list.append(list[x])
    return new_list
print(new_list(list))

'''3.写函数，判断用户传入的对象（列表）长度是否大于5，如果大于5，那么仅保留前五个长度的内容并返回。不大于5返回本身。
例如：
传入1：[34,23,52,352,666,3523,5]   	返回1：[34,23,52,352,666]
传入2：[34,23,52]     				返回2：[34,23,52]'''
def five_index(w):
    if len(w)>5:
        return w[:5]
    else:
        return w
print(five_index([34,23,52,352,666,3523,5]))
print(five_index([34,23,52]))

'''4.写函数，检查传入的字符串是否含有空字符串，返回结果，包含空字符串返回True，不包含返回False
例如： 传入："hello world"  返回：True'''
def has_space(str):
    if ' ' in str:
        return True
    else:
        return False
print(has_space('"hello world"'))

'''5.写函数，接收n个数字，求这些数字的和'''
def sum_num(*int):
    return sum(int)
print(sum_num(1,2,3,4,5,6,7,8,9,90,345,345,345))

'''6.定义一个函数,实现两个数四则运算,要注意有3个参数,分别是运算符和两个运算的数字.
例如： 传入：10,*,20  返回：200'''
def operation(int1,s,int2):
    if s=='+':
        return int1+int2
    elif s=='-':
        return int1-int2
    elif s=='*':
        return int1*int2
    elif s=='/':
        return int1/int2
    else:
        print('没这算法搞啥呢')
print(operation(2,'*',10))

'''7.实现学生管理系统,完成对学员的增,删,改,查和退出学生管理系统。
要求1：使用一个list用于保存学生的姓名。
要求2：输入0显示所有学员信息,1代表增加，2代表删除，3代表修改，4代表查询，exit代表退出学生管理系统。
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


print('-----------------------欢迎进入T666班学生管理系统-----------------------------')
student_name = ['小龙女', '赵敏', '东方不败', '猜猜我是谁', '我不猜']
def select_function():

    x = input('请选择系统功--' '0:显示所有学员信息 ''1:添加一个学员信息''2:删除一个学员信息'
              '3:修改一个学员信息''4:查询一个学员信息' 'exit:退出学生管理系统\n')
    if x=='0':
        all_student_info()
    elif x=='1':
        add_student_info()
    elif x == '2':
        del_student_info()
    elif x == '3':
        updata_student_info()
    elif x == '4':
        select_student_info()
    elif x == 'exit':
        exit_sys()
    else:
        print('别乱搞，搞坏留下来扫地')
        select_function()
def all_student_info():
    print('全部同学姓名：',student_name)
    select_function()
def add_student_info():
    new_name=input('请输入与要添加的信息：')
    student_name.append(new_name)
    if new_name in student_name:
        print('添加成功，添加名字为---:',new_name)
    else:
        print('添加失败 请重试')
    select_function()
def del_student_info():
    del_name=input('请输入要删除的信息：')
    if del_name in student_name:
        student_name.remove(del_name)  #无法删除重名的  暂无需求不考虑
    else:
        print('删除失败 请重试')
    select_function()
def updata_student_info():
    updata_name_before=input('请输入要修改的信息--：')
    updata_name_after=input('请输入修改后的信息--：')
    if updata_name_before in student_name:
        student_name.remove(updata_name_before)
        student_name.append(updata_name_after)
    print('修改成功')
    select_function()
def select_student_info():
    sel_name=input('请输入要查找的信息--：')
    if sel_name in student_name:
        print('是T666的学生，看见小心一点')
    select_function()
def exit_sys():
    print('退出成功！')

if __name__ == '__main__':
    select_function()



