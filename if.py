'''
alert_system_active = True
if not alert_system_active:
    print("system is offline")
else:
    print("Alerts operation")
'''   

rainfall = 499
population_density = 501
if(rainfall < 500):
    if(population_density > 500):
        print("Severe Scarcity")
elif(500<= rainfall <= 1000):
    if(200<= population_density <= 500):
        print("Moderate Scarcity")
else:
    print("No Scarcity")


