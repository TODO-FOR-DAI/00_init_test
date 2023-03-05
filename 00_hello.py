#print('hello')
a=1
print(a+a)
a=6
b=5
print(a%5)
print(type(a))
a = "python "
b = 'is '
c = 'fun'
print(a+b+c)
print(a*10)
test = 'Life is short. So, You need to learn Python'
print(test[-2])
a = "I eat %d aplles." %3
print(a)
b= "test {} wht?" . format("  이렇게")
print(b)
b= "test {name} wht?" . format(name="김대현")
print(b)
print(b.count('te'))
print(b.find('te'))
a = '  Hi  '
print(a.upper())
print(a.lower())
print(a.strip())

print(test.replace("Life", "Your Leg"))
print(test.split())


# tuple
t1 = (1, 2, 'a','b')
print(t1)
list1 = [1, 2, 'a','b']
print(list1)
del list1[0]
print(list1)

# dictionary - Hash, Map, Object, Json (Java script Object Notation)
# key & value
dic = {'name' : 'pey', 'phone': '1234', 'age' : '14'}
print(dic['name'])

dic['test'] = 'dai'
print(dic)
del dic['name']
print(dic)


print(dic.keys())
print(dic.values())
print(dic.items())

#print(dic['add'])
print(dic.get('add'))
print(dic.get('add', '없음'))
print('test' in dic)
print('add' in dic)

dic.clear()
print(dic)

