'''
numbers = range(1, 11)
numbers_and_squares  = {x:x**2 for x in numbers}
print(numbers_and_squares)
'''
ocean_temperatures = {
    'Pacific': [25, 25.3, 25.6, 25.2, 25.5, 25.6],
    'Atlantic': [23.4, 23.8, 23.7, 29.9, 24.0, 29.1],
    'Indian': [26.5, 26.7, 27.0, -29, -55, -99, -99] 
}

'''
ocean_temp_c = {ocean: temps[0] for ocean, temps in ocean_temperatures.items()}
print(ocean_temp_c)
'''
'''
for i in range (5):
    if i == 3:
        break
    print(i)
'''

initial_forested_area = 1000
deforestation_rate = 20

years = 0
while initial_forested_area > 500:
    initial_forested_area -= deforestation_rate
    years += 1
    
print(f"Years until critical deforestation level: {years}")
    
