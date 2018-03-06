#语句块
#if
name = "All";
if name.endswith("en"):
    print "Hello en";
elif name.endswith("ll"):
    print "Hello stranger";
else:
    print("no man");
#布尔运算符and, or, not

#循环
x = 1;
while x<= 3:
    print x;
    x += 1;

words = ["this", "is", "a", "test"];
for word in words:
    print word;

#迭代方法
names = ["anne", "beth", "george", "damon"];
ages = [12, 45, 21, 33];
for name, age in zip(names, ages):
    print name, 'is', age, 'years old';
# anne is 12 years old
# beth is 45 years old
# george is 21 years old
# damon is 33 years old