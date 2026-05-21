# No input function

def create_deforestation_message():
    """
    Generates a general message about deforestation
    """
    print("Deforestation is a serious environmental issue. Help save our forests!")
    
    
# default input

def create_deforestation_message(location, message = "Deforestation is a serious environmental issue. Help save our forests!"):
    '''
    Generates a general message about deforestation.
    
    Parameters
    ----------
    location: str, the location affected by deforestation
    message : str, the message to convey (default is a general message)
    '''
    print(f"Deforestation in {location}: {message}")
    
create_deforestation_message("Nairobi")

create_deforestation_message("Karura", "Preserve Biodiversity!")

# keyword arguments

def create_deforestation_message(location, message = "Preserve Biodiversity"):
    '''
    Generates a general biodiversity message.
    
    Parameters
    ----------
    location: str, the location addressed
    message: str, the biodiversity message
    
    '''
    print(f"{location}:{message}")
    
create_deforestation_message(message = "Diversity is good", location = "Nairobi")
    
# *args: allow a function to take a number of positional/non-keyword arguments

def deforestation_impacts(*consequences):
    """
    Describes the impacts of deforestation.
    
    Parameters
    ----------
    
    *Consequences: tuple, variable number of consequences
    """
    print("Impacts of deforestation")
    print(",".join(consequences))
    
deforestation_impacts("Loss of biodiversity", "Climate change", "Disruption of Ecosystems")

#*kwargs: allow a function to take a number of keyword arguments

def list_forest_details(**details):
    """
    Lists detailed information about a forest. 
    
    Parameters
    ----------
    -**details: dict, variable number of keyword arguments
    """
    print("forest details: ")
    for key, value in details.items():
        print(f"{key}:{value}")
        
list_forest_details(location = "Nairobi", Cause = "Illegal logging", area = "National Park")


# multiple inputs

def calculate_deforestation_impact(initial_forest_area, remaining_forest_area, carbon_emission_factor=2.3):
    '''
    Calculate the impact of deforestation
    
    Parameters
    ----------
    
    -initial_forest_area: float, initial forest area in square kilometres.
    -remaining_forest_area: float, remaining forest area in square kilometres.
    -carbon_emission_factor: float, CO2 emissions 
                                per unit of tree cover loss (default is 2.3)
    
    Return
    ------
    -tuple: (float, float, float), percentage of tree cover loss, 
            remaining forest area, and estimated increase in CO2 emissions
    '''
    #Calculates the percentage of tree cover loss
    tree_cover_loss_percentage = ((initial_forest_area-remaining_forest_area)/initial_forest_area)*100
    
    #Calculates the estimated increase in CO2 emissions
    estimated_emissions = tree_cover_loss_percentage * carbon_emission_factor * initial_forest_area/100
    
    return (tree_cover_loss_percentage, remaining_forest_area, estimated_emissions)

loss_percentage, remaining_area, C02_increase = calculate_deforestation_impact(1000,800)
print(f"tree cover loss percentage: {loss_percentage}")
print(f"Remaining forest area: {remaining_area} square kilometres")
print(f"Estimated increase in C02 emissions: {C02_increase} metric tons")
