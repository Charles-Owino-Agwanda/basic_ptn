deforestation_rates = [150, 145, 140, 135, 130]
deforestation_years = [2010, 2011, 2012, 2013, 2014]
'''
for i in range(len(deforestation_rates)):
    rate = deforestation_rates[i]
    year = deforestation_years[i]
    print(f"i ={i+1} - yearly deforestation rate in {year} is: {rate}k hectares")
'''  
''' 
for i, rate in enumerate(deforestation_rates):
    year = deforestation_years[i]
    print(f"i ={i} - yearly deforestation rate in {year} is: {rate}k hectares")
'''
'''
for i, rate in enumerate(deforestation_rates):
    print(f" The rate this year is: {rate}k hectres")
'''

marine_species_count = {
    'dolphins': 12,
    'whales' : 3,
    'Sea Turtles': 7
}
'''
for species in marine_species_count:
    print(f"{species}: {marine_species_count[species]} sightings")
    ''' 
'''
for species, count in marine_species_count.items():
    print(f"{species}: {count}")
'''

deforestation_data = {
    'Amazon': 120,
    'Congo Basin': 80,
    'Southeast Asa': 95,
    'Eastern Australia': 40
}

critical_threshold = 90
total_deforestation = 0
'''
for region, area in deforestation_data.items():
    if area > critical_threshold:
        print(f"critical deforestation in {region}: {area} square km")
'''
'''
for area in deforestation_data.values():
    total_deforestation += area
    
print("Total deforestation area: {} square km".format(total_deforestation))
''' 

ocean_temperatures  = {
    'pacific': [25, 25.3, 25.6, 25.2, 25.5, 25.6],
    'Atlantic':[23.4, 23.8, 23.7, 29.9, 24.0, 29.1],
    'Indian': [26.5, 26.7, 27.0, -29, -55, -99, -99]
}

for ocean, temperatures in ocean_temperatures.items():
    sum_temperatures = 0
    count_temperatures = 0
    avg_temperature = 0
    for temperature in temperatures:
        if temperature < 0:
            print(f"{ocean} ocean sensor malfunction, value {temperature} onward ignored.")
            break
        if temperature > 29:
            print(f"Disregarding temperature: {temperature} as an outlier for {ocean}.")
            continue
        sum_temperatures += temperature
        count_temperatures +=1
    
    avg_temperature =sum_temperatures/count_temperatures
    print(f"name={ocean}: sum_temp={round((sum_temperatures),2)}: avg-temp={round((avg_temperature),2)}")
    