_metaclass_ = type; #确定使用新类
class Person:
    def setName(self, name):
        self.name = name;
    
    def getName(self):
        return self.name;
    
    def greet(self):
        print "Hello World! I'm %s." % self.name;

yoda = Person();
yoda.setName('yoda');
print yoda.getName();
print yoda.greet();

# 类方法私有化
# 在方法名前加双下划线即可
class Secretive:
    def __inaccessible(self):
        print "You can't see me";
    
    def accessible(self):
        print "The secret message is: ";
        self.__inaccessible();

s = Secretive();
# s.__inaccessible(); Secretive instance has no attribute '__inaccessible'
s.accessible();

# 指定超类
class Filter:
    def init(self):
        self.blocked = [];
    
    def filter(self, sequence):
        return [x for x in sequence if x not in self.blocked];

class SPAMFilter(Filter):
    def init(self):  # 重写超类中的init方法
        self.blocked = ['SPAM'];

s = SPAMFilter();
s.init();
print s.filter(['SPAM', 'SPAM', "abc", 'cde']);
print issubclass(SPAMFilter, Filter); # 检查继承
