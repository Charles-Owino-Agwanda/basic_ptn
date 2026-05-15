atlantic_temp_k = []
atlantic_temp_c = [23.4, 23.8, 23.7, 29.9, 24.0, 29.1]
indian_temp_c = [26.5, 26.7, 27.0, -29, -55, -99, -99]


for temp in atlantic_temp_c:
    temp += 273
    atlantic_temp_k.append(temp)
    
print(f"conventional method: {atlantic_temp_k}")

atlantic_temp_kk = [temp + 273 for temp in atlantic_temp_c]
print(f"list_com:{atlantic_temp_kk}")

print([temp for temp in indian_temp_c if temp > 0])