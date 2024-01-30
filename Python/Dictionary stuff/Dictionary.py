import operator


my_dict = {}

ok = {1:8, 9:3, 1:2, 5:3}
print("Random stuff: ", ok)
sorted_ok = sorted(ok.items(), key=operator.itemgetter(1))

print("Ascending by value : ", sorted_ok)
sorted_ok = dict( sorted(ok.items(), key=operator.itemgetter(1), reverse=True))
print("Descending value : ", sorted_ok)

print("SECOND HALF OF TASK           ")
ok = {1:8, 9:3, 1:2, 5:3}
print(ok)
ok.update({2: 30})
print(ok) 

print("THIRD PART OF TASK")
dic1 = {1:10, 2: 20}
dic2 = {4:8, 6:12}
dic3 = {3:6, 5:10}
dic4 = {}
for d in (dic1, dic2, dic3):
    dic4.update(ok)
print(dic4)
print("PART 4 OF TASK")
ok = {1:10, 2:20, 4:8, 6:12, 3:6, 5:10}
def is_key_present(x):
    if x in d:
        print('Its already here proably')
is_key_present(5)
is_key_present(9)
print("PART 5 OF TASK")
ok = {'x': 5, 'y': 10, 'z': 15}
for dict_key, dict_value in ok.items():
    print(dict_key, '===', dict_value)

print("PART 6 OF TASK")
okk = int(input("Input a number "))
ok = dict()
for x in range(1, okk + 1):
    ok[x] = x * x
print(ok) 

print("PART 7 OF TASK")
ok = dict()
for x in range(1, 15):
    ok[x] = x ** 2
print(ok)

print("PART 8 OF TASK")
ok1 = {'a': 50, 'b': 100}
ok2 = {'x': 60, 'y': 120}
ok = ok1.copy()
ok.update(ok2)
print(ok)

print("PART 9 OF TASK")
ok = {'Red': 5, 'Green': 9, 'Blue': 3}
for colour_key, value in ok.items():
    print(colour_key, '=', ok[colour_key])

print("PART 10 OF TASK")
my_dict = {'dic1': 100, 'dic2': -5, 'data3': 223}
result = sum(my_dict.values())
print(result)