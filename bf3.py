def project_future_tree_planting(initial_planted_trees, annual_growth_rate, projection_years):
    """
    Project the future number of planted trees for each year (starting at 1) based on 
    the initial planting and growth rate.

    Parameters:
    - initial_planted_trees (int): Initial number of trees planted.
    - annual_growth_rate (float): Annual growth rate of planted trees.
    - projection_years (int): Number of years for projection.

    Returns:
    - list: List of projected tree planting for each year.
    """
    projection = [initial_planted_trees * (1 + annual_growth_rate) ** year for year in range(1, projection_years+1)]
    return projection
    
print(project_future_tree_planting(100, 0.05, 10))

