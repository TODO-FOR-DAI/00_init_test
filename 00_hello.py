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

#---------- Push to the Github

s1 = set([1, 2, 3])
s2={1, 2, 3}
print(s1)
print(s2)

l = [1, 2, 2, 3, 3]
newList = list(set(l))      # 중복이 제거된 set 을 만들고 이것을 다시 list 로 만들어 버림
print(newList)

s1 = set("hello")   # 집합은 순서가 없고, 중복이 없다
print(s1)


s1 = set([1, 2, 3, 4, 5, 6])
s2 = set([4, 5, 6, 7, 8, 9])
print(s1 & s2)

print(s1.intersection(s2))

print(s1 | s2)

print(s1 - s2)
print(s2 - s1)

s1.add(7)
print(s1)

s1.update([8, 9,1])
print(s1)

print(True)

a = True
if a:
    print(a)

b = False
if b:
    print("test")
    print("block")
else:
    print("here")
    print("se")



a=[1, 2, 3]
b= a
b[1] = 4

print(a)
print(b)


print(id(a))
print(id(b))

b = a[:]    # slicing 해서 새로운 객체를 만들어서 집어넣게 된다


b[1] = 7
print(a)
print(b)


print(id(a))
print(id(b))


a, b = ('pyhton', 'life')

print(b)
print(a)

print(a, b)


