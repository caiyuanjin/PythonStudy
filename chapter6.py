#函数
def hello(name):
    return "Hello " + name;
print hello("world");

def fibs(num):
    result = [0,1];
    for i in range(num-2):
        result.append(result[-2] + result[-1]);
    return result;
print fibs(8);

#store name and lookup name
def init(data):
    data['first'] = {};
    data['middle'] = {};
    data['last'] = {};

def lookup(data, label, name):
    return data[label].get(name);

def store(data, full_name):
    names = full_name.split();
    if len(names) == 2:
        names.insert(1,'');
    labels = 'first', 'middle', 'last';
    for label, name in zip(labels, names):
        people = lookup(data, label, name);
        if people:
            people.append(full_name);
        else:
            data[label][name] = [full_name];
person = {};
init(person);
person['first'].setdefault("Anne", []).append('Anne ABC Katy');
store(person, "Jin Cai Yuan");
print lookup(person, 'middle', 'Cai');
store(person, "Allen Walker");
print lookup(person, "first", "Allen");

#提供任意多的参数
# * 收集其余位置的参数; ** 收集关键字的参数，即x=1,y=2
#实现名字字典
def storeNames(data, *full_names):
    for full_name in full_names:
        names = full_name.split();
        if len(names) == 2:
            names.insert(1, '');
        labels = 'first', 'middle', 'last';
        for label, name in zip(labels, names):
            people = lookup(data, label, name);
            if people:
                people.append(full_name);
            else:
                data[label][name] = [full_name]; #[]是将String转换为列表


men = {};
init(men);
storeNames(men, "A B", "C D E", "A C B");
print lookup(men, 'last', 'B');