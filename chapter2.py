print("Hello World");
###序列
#1. 列表
Edward = ['Edward', 21];
John = ['John', 30];
people = [Edward, John];
print(people);

#索引
greeting = 'Hello';
print(greeting[0]); # 'H'
print(greeting[-1]); # 'o' 支持反向索引
print('Hello'[1]); # 'e'

#分片，第一个元素包含咋分片内，而第二个元素不包含在分片内
tag='<a href="http://www.python.org">Python web site</a>';
#表示从第9个元素开始到第29个元素，不包含30。[9:30)
#输出 http://www.python.org
print(tag[9:30]);
#表示从第32个元素到从尾开始的-4个元素，[32,-4)
#输出Python web site
print(tag[32:-4]);
#访问最后4个元素
print(tag[-4:]); # </a>
#访问开始的2个元素
print(tag[:2]); # <a

#分片指定步长
numbers = [0,1,2,3,4,5,6,7,8,9,10];
print(numbers[1:6:2]); # [1,3,5]
#步长可以为负数，此时分片从右往左执行
print(numbers[8:3:-1]); #[8,7,6,5,4]

#序列可以进行加操作，但只能类型相同的进行操作
print("Hello," + "World!");
print([1,2,3] + [4,5,6,7]);

#序列乘法
print("python" * 5); #python重复5遍

#in 运算符
permission = "rw";
print("r" in permission); #True

####列表 --> 列表是可变的，可以修改列表的内容
#list函数 --> 可以根据字符串创建列表
print(list("Hello")); #输出 ['H', 'e', 'l', 'l', 'o']
#删除列表中的元素
names = ["A", "B", "C", "D"];
del names[1];
print(names); # ["A", "C", "D"]

#分片赋值
name = list("Paul");
name[2:] = list("ir");
print(name); # ['P', 'a', 'i', 'r']
#插入新元素
numbers = [1,5];
numbers[1:1] = [2,3,4];
print numbers; # [1, 2, 3, 4, 5]
#可以用这种方法删除元素
numbers[1:-1] = [];
print numbers; # [1,5]

##列表方法
# append: 追加
# count(元素): 统计元素出现次数
# extend: 扩展列表，会改变原有列表，但是用join操作原有列表不会变，而是创建了一个新列表
# index: 找出匹配的索引位置
# insert(位置, 元素): 即插入方法

# 元组: 通过() 括起来的，(1,2,3) 

