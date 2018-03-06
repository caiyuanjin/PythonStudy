#字典
phoneBook = {"Alice": "2134", "Beth": "1111", "Cathy": "2222"};
print phoneBook;
#dict函数
items = [('name', 'Alice'), ('age', 42)];
d = dict(items);
print d;

people = {
    "Alice": {
        "phone": "1111",
        "addr": "Foo driver"
    },
    "Beth": {
        "phone": "2222",
        "addr": "Bar street"
    },
    "Cathy": {
        "phone": "3333",
        "addr": "avenue"
    }
};
name = "Alice";
phone = "phone";
addr = "addr";
if name in people:
    print "%s's %s is %s" % (name, phone, people[name][phone]);

