car_company_1 = 'Ferrari'
car_detail_1 = [
    {'coler' : 'White'},
    {'horsepower': 400},
    {'price': 8000}
]

car_company_2 = 'Bmw'
car_detail_2 = [
    {'coler' : 'Black'},
    {'horsepower': 270},
    {'price': 5000}
]

car_company_3 = 'Audi'
car_detail_3 = [
    {'coler' : 'Silver'},
    {'horsepower': 300},
    {'price': 6000}
]

car_company_list = ['Ferrari', 'Bmw', 'Audi']
car_detail_list = [
    {'coler' : 'White', 'horsepower': 400, 'price': 8000},
    {'coler' : 'Black', 'horsepower': 270, 'price': 5000},
    {'coler' : 'Silver','horsepower': 300, 'price': 6000}
]


del car_company_list[1]
del car_detail_list[1]

# print(car_company_list)
# print(car_detail_list)


# print()
# print()



car_dicts=[
    {'car_company':'Ferrari',  'car_detail' : {'coler' : 'White', 'horsepower': 400, 'price': 8000}},
    {'car_company':'Bmw',  'car_detail' : {'coler' : 'Black', 'horsepower': 270, 'price': 5000}},
    {'car_company':'Audi',  'car_detail' : {'coler' : 'Silver','horsepower': 300, 'price': 6000}}
]

# print(car_dicts)


class Car():
    def __init__(self,company,details):
        self._company = company
        self._details = details


    def __str__(self):
        return 'str : {} - {}'.format(self._company,self._details)
    

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company,self._details)



car1= Car('Ferrari',{'coler' : 'White', 'horsepower': 400, 'price': 8000})
car2= Car('Bmw',{'coler' : 'Black', 'horsepower': 270, 'price': 5000})
car3= Car('Audi',{'coler' : 'Silver','horsepower': 300, 'price': 6000})


# print(car1)
# print(car2)
# print(car3)

car_list = []

car_list.append(car1)
car_list.append(car2)
car_list.append(car3)

print(car_list)



for x in car_list:
    print(repr(x))