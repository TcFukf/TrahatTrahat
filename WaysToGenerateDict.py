
data = [ (f"key{i}",f"val{i}") for i in range(4)]

d = dict(data)
print(d)

d = {i[0]:i[1] for i in data }
print(d)

d = {}
for i in data:
    d.update( {i[0]:i[1]} )
print(d)

d = dict( key1 = 1, key2 = 2)
print(d)

d = dict.fromkeys(["key1","key2"],"defaultValue")
print(d)

d = {"key1":1,"key2":2}
print(d)

keys = [i[0] for i in data]
values = [i[1] for i in data]

d = dict(zip(keys,values))
print(d)
