existing_vehicles = [
    {'model': 'TX-130', 'colour': 'Green', 'horsepower': 150, 'fuel_capacity': 60},
    {'model': 'RX-850', 'colour': 'Red', 'horsepower': 120, 'fuel_capacity': 45}
]

new_vehicle_params = ('ZX-500', 'Blue', 130, 55)

def add_vehicle(vehicles, new_vehicle_params):
    new_dict = {
        'model': new_vehicle_params[0],
        'colour': new_vehicle_params[1],
        'horsepower': new_vehicle_params[2],
        'fuel_capacity':new_vehicle_params[3]
    }
    vehicles.append(new_dict)
    return vehicles

new_vehicle =  ('SX-750', 'White', 180, 80)
add_vehicle(existing_vehicles, new_vehicle)



'''
new_dict = {}
new_dict['model'] = new_vehicle_params[0]
new_dict['colour'] = new_vehicle_params[1]
new_dict['horsepower'] = new_vehicle_params[2]
new_dict['fuel_capacity'] = new_vehicle_params[3]

existing_vehicles.append(new_dict)
print(existing_vehicles)

'''
