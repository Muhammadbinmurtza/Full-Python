# # data : list[int] = [1,2,3,4,5,6,7,8,9,10]
# # mbm : list[int] = [3,8,66]
# # a = list(map(lambda x:x**2, mbm))
# # print(a)
# # from typing import Tuple,Dict,Any
# # def my_func(a:int, b:int,*abc:Tuple[int,...], **xyz: Dict[str,int]) -> None:
# #     print(a, b, abc, xyz)
# # my_func(1,2, 7,8,9,0, c= 20, d = 5)
# def  city_country(city:str,country:str) -> str:
#     return city,country
#     print(city,country)
# city_country('faisalabad','pakistan')
# city_country('multan','pakistan')
# city_country('lahore','pakistan')
# def func(c):
#     a = 0
#     while  a < c:
#         if a % 2 == 0:
#             yield a
#             a += 1
# x = func(15)
def deco(func):
    def wrapper():
        print('payment has started')
        func()
        print('payment has been sent')
        return wrapper

@deco
def hello()-> str:
    print('executing')
hello()
