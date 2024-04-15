def add(num1, num2):
    return num1 + num2

result1 = add(10, 20)
print(result1)

def add(num1, num2, num3, num4):
    return num1 + num2, num3 + num4 # 하나의 함수는 하나의 값만 리턴

result2 = add(10, 20, 30 ,40)
print(result2) #하나의 함수 하나의 리턴(불변) 튜플로 묶여서 나온 것 뿐00


r1, r2 = (1, 2) # 비구조할당 유사 묶어주는 거 없다.
print(r1, r2)

#del index remove 처음 값 삭제

# push pop => stack 후입선출

nums = [5, 2, 7, 3, 1]
nums.sort() # 해당동일한 sort 리턴 리스트아님.
print(nums) # None 리턴 없다.
nums.reverse()
print(nums) #None sort.rever

# print(nums.index(10)) # index 둘다 있다. 예외로 처리함.
name = "김준일"
# 리스트 .find 없음 str값만 있다.
print(name.find("주")) # index 주 못찾음. 예외 find 못찾음 -1
# print(name.index("주")) # index 1

print(nums.index(3)) # 7 5 3 2 1

user= {
    "username": "testuser",
    "pasword": "1234",
    "name": "김도훈",
    "email": "rlaehgns69@naver.com"
}

print(user)
user.update({
    "phone": "010-1234-5678",
    "name": "김준이"
}) #dict 추가
user["age"] = 31 #두가지 방법이 있다.

print(user)

