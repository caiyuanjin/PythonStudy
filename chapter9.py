# 魔法方法、属性和迭代器
# 形如 __future__的方法
__metaclass__=type;
# 构造方法
class FooBar:
    def __init__(self):
        self.someVar = 42;

f = FooBar();
print f.someVar;

class Bird:
    def __init__(self):
        self.hungry = True;
    def eat(self):
        if self.hungry:
            print "Aaaaah....";
            self.hungry = False;
        else:
            print "No, thanks";

class SongBird(Bird):
    def __init__(self):
        super(SongBird, self).__init__();
        self.sound = "Squawk!";
    def sing(self):
        print self.sound;

sb = SongBird();
sb.sing();
sb.eat();

# 基本的序列和映射规则
# __len__(self), __getitem__(self, key), __setitem__(self, key, value), __delitem__(self, key)
def checkIndex(key):
    if not isinstance(key, (int, long)): raise TypeError;
    if key < 0: raise IndexError;

class ArithmeticSequence:
    def __init__(self, start=0, step=1):
        self.start = start;
        self.step = step;
        self.changed = {};
    def __getitem__(self, key):
        checkIndex(key);
        try: 
            return self.changed[key];
        except KeyError:
            return self.start + key*self.step;
    def __setitem__(self, key, value):
        checkIndex(key);
        self.changed[key] = value;

s = ArithmeticSequence(1,3);
print s[3];  # 10
s[4] = 2;
print s[4];  # 2

# property函数
class Rectangle:
    def __init__(self):
        self.width = 0;
        self.height = 0;
    def setSize(self, size):
        self.width, self.height = size;
    def getSize(self):
        return self.width, self.height;
    size = property(getSize, setSize);

r = Rectangle();
r.width = 10;
r.height = 5;
print r.size; # (10, 5)
r.size = (100,50);
print r.width; # 100