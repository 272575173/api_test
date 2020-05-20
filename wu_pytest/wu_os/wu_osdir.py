# -*- coding: utf-8 -*-
'''
@File    :   Api_Auto_SendRequest.py    
@Contact :   272575173@qq.com
@Author  :   Wuyz  
@Time    :   2020/3/6 10:28 
'''

import os


# os.mkdir('wu')
# os.mkdir('E:\wu_pytest\wu_os')
#
# path=os.getcwd()
# print('当前路径是{0} '.format(path))
# path2=os.path.realpath(__file__)
# print(print('当前路径是{0} '.format(path2)))
#
# path3=os.getcwd()+r'/python1'
# print(path3)
# os.mkdir(path3)
# path=os.path.dirname(__file__)  # 表示当前所处的文件夹的绝对路径
# print(path)
# path1=os.path.abspath('.')   # 表示当前所处的文件夹的绝对路径
# print(path1)
# path2=os.path.abspath('..')  # 表示当前所处的文件夹上一级文件夹的绝对路径
# print(path2)
#
# path3=os.path.abspath(os.path.dirname(__file__) )
# print(path3)
'''参赛者会看见三个大箱子，其中一箱子里面有一个美女，选中有美女的那个箱子可赢得美女一日游的机会，
另外两箱子里面则各藏有抠脚大汉。 当参赛者选定了一个箱子，但未去开启它的时候，节目主持人开启剩下两个箱子
的其中一个箱子，冒出其中一位抠脚大汉。 主持人其后会问参赛者要不要换另一一个仍然闭上的箱子。
问题是：你是否会重选？ 请写一段程序来模拟以上场景，算出重选或不重选的概率，以佐证你的选择是否正确。
（可用java、Python、golang其中一种语言来实现）
'''

import random

def random_product(dict):
    num_list = [1, 2, 3]
    first_key = random.choice(num_list)
    pick_one = dict[first_key]
    num_list.remove(first_key)

    second_key = random.choice(num_list)
    pick_two = dict[second_key]

    return pick_one, pick_two

def rechoice(pick_one, pick_two):
    pick_one, pick_two = pick_two, pick_one
    if pick_one == "beauty":
        return True
    else:
        return False


def no_rechoice(pick_one, pick_two):
    if pick_one == "beauty":
        return True
    else:
        return False


if __name__ == '__main__':
    dict = {1: 'beauty',
            2: 'ugly-man',
            3: 'ugly-man'
            }
    true_sum = 0
    false_sum = 0
    for i in range(100000):
        pick_one, pick_two = random_product(dict)
        if rechoice(pick_one, pick_two):
            true_sum += 1
        else:
            false_sum += 1

    print("交换正确的概率：", '%.3f' % (true_sum / 100000))
    print("交换错误的概率：", '%.3f' % (false_sum / 100000))
















'''请按照以下3条规则计算1-99之和: 1.小于或等于10的(譬如：1+2+...+10)，全部相加；
 2.大于10的，如果十位数是偶数的，则计算他们之间的偶数之和(譬如：20+22+24+...+40+42..+86+88)；
  3.如果十位数是奇数的，则求他们之间的奇数之和(譬如：11+13...+97+99)。
  （可用java、Python、golang其中一种语言来实现）'''
z=0;v=0;c=0

for x in range(1,100):
    a=x/10
    if x<=10:
        z+=x
    elif a%2==0&x%2==0:
        v+=x
    elif a%2!=0:
        c+=x

print('小于等于10:{0}偶数:{1}奇数:{2}'.format(z,v,c))


'''以下题目需使用RobotFramework测试框架的编辑器RIDE编写完成： 服务器简要信息 hostIp:127.0.0.1,port:8088 接口基本信息 接口地址：/admin/login；请求方法：POST;数据类型：JSON；响应类型：JSON 接口请求参数名称:user_name,passwd；参数皆为必传，类型为string。 响应参数名称:status,success；参数皆为必须，类型为string。成功的响应信息：{"status":"1","success":"登录成功"} 。
问题：1.发送一个post请求，并对接口响应进行断言。'''