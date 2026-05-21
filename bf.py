'''
def main():
    len = int(input("Enter length: "))
    wid = int(input("Enter width: "))
    received_area = cal_forest_area(len, wid)
    print(received_area)
 

def cal_forest_area(length, width):
    area = length * width
    return area


if __name__ == "__main__":
    main()
'''

def main():
    calculated_volume = cal_volume(2, 3, 4)
    print(calculated_volume)
    
    
def cal_volume (length, width, height):
    '''
    Calculates the volume of a cube by multiplying its height, width, and length
    
    Parameters
    -------------
    Length: The length of the cube in metres
    Width: The width of the cube in metres
    length: the length of the cube in metres
    
    Return
    -------------
    An integer that represents the volume of the cube in cubic meters
    
    '''
    volume = length * width * height
    return volume

if __name__ == "__main__":
    main()
    

cal_volume.__doc__
help(cal_volume)
