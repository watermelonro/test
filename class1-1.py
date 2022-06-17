# chapter 02-01
# 객체 지향 프로그래밍 (oop) -> 코드의 재사용, 코드 중복 방지, 유지보수, 대형프로젝트 등..
# 규모가 큰 프로젝트(프로그램) -> 함수 중심 -> 데이터가 방대 -> 복잡
# 클래스 중심 -> 데이터 중심 -> 객체로 관리 

# 일반적인 코딩
# 차량1
car_company_1 = 'Ferrari'
car_detail_1 = [{'color': 'white'},{'horsepower':400},{'price':8000}]

# 차량2
car_company_2 = 'bmw'
car_detail_2 = [{'color': 'black'},{'horsepower':270},{'price':5000}]

# 차량3
car_company_3 = 'audi'
car_detail_3 = [{'color': 'silver'},{'horsepower':300},{'price':6000}]


# 리스트 구조
# 관리하기가 불편
# 인덱스 접근 시 실수 가능성, 삭제 불편

car_company_list = ['Ferrari','bmw','audi']
car_detail_list = [{'color': 'black','horsepower':270,'price':5000},
                    {'color': 'white','horsepower':400,'price':8000},
                    {'color': 'silver','horsepower':300,'price':6000}]
del car_company_list[1]
del car_detail_list[0]

print(car_company_list)
print(car_detail_list)

print()
print()

# 딕셔너리 구조 
# 코드 반복 지속, 중첩 문제(키), 키 조회 예외 처리 등 

car_dicts = [{'car_company':'ferrai','car_detail':{'color': 'white','horsepower':400,'price':8000}},
{'car_company': 'bmw','car_detail':{'color': 'black','horsepower':270,'price':5000}},
{'car_company':'audi','car_detail':{'color': 'silver','horsepower':300,'price':6000}}]


del car_dicts[1]
print(car_dicts)

print()
print()

# 클래스 구조
# 구조 설계 후 재사용성 증가, 코드 반복 최소화, 메소드 활용 

class Car():
    def __init__(self,company,details):
        self.company = company
        self.details = details
        
    def __str__(self): #사용자 레벨
        return 'str: {} - {}'.format(self.company,self.details)
    
    def __repr__(self): # 개발자 레벨
        return 'repr: {} - {}'.format(self.company,self.details)

car1 = Car('Ferrari',{'color': 'white','horsepower':400,'price':8000})
car2 = Car('bmw',{'color': 'black','horsepower':270,'price':5000})
car3 = Car('audi',{'color': 'silver','horsepower':300,'price':6000})
print(car1)
print(car2)
print(car3)

print(car1.__dict__)

# __dict__: 안에 있는 정보를 다 보여줌 
#  __str__,__repr__은 출력을 할 때 도와줌 

# 리스트 선언해서 출력하면 repr로 출력
car_list = []
car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)

for x in car_list:
    print(repr(x)) # repr로 호출
    print(x) # str로 호출




