number = 10 # 리터럴 값 number에 할당 주소값이 같다.
print(type(number))

print(id(10)) #id() 주소값
print(id(number))
number += 1 
print(id(number))
number -= 1
print(id(number)) #10이라는 값은 리터럴값으로 고유한 주소값을 가진다.

print(type("test")) #str
print(type([])) #list
print(type(())) #tuple
print(type({})) #dict

print([1, 2, 3, 4])
print((1, 2, 3, 4))
print({"id": 1, "name": "김준일"}) #dict json과 같다.

list1 = [1, 2, 3, 4]
tp = (5, 6, 7, 8)
dict1 = {"id": 1, "name": "김준일"}

print(list[0])
print(tp[0]) # list랑 tp는 배열 인덱스 값
print(dict1["id"]) # dict 키값

list1.append(5)
print(list1) # [1,2,3,4,5]
#tp.append() 추가, 삭제 변경 불가능
print(tp.index(7)) # index of
# dict 값 추가 변경 하고 싶다. => list
list2= list(tp) # 형변환
print(list2)
print(dict1.keys())
print(dict1.values())
print(dict1.items())
#print(dict1.items()[0])
print(list(dict1.items())[0])

print(True)
print(False)

