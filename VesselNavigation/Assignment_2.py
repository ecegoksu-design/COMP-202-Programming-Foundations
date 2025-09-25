#Import libraries
import math
import random

#Setting global variables
MIN_LAT = -90 #the latitude of every point on Earth is an angle between
# -90°(South) and +90° (North)
MAX_LAT = 90
MIN_LONG = -180 #the longitude of every point on Earth is an angle between
# -180° (West) and +180° (East).
MAX_LONG = 180
EARTH_RADIUS = 6371 #(in kilometer)
FEET_CONV = 3.28
RAD_CONV = math.pi /180
REST_LAT = 25 #restricted latitude
REST_LONG = -71 #restricted longitude
LENGTH_THRESHOLD = 26
MIN_DIST = 400 #minimum distance to not enter restricted area
CAP_CONS = 15 #capacity constant
SEED = 123 #seed for random
RAND_INT = 20 #constant required to make random an integer between 0, 20
INTERVAL = 10 #constant required to bring the integer to interval -10, 10
LAT_1 = 40 #hazardous area latitude start
LAT_2 = 41 #hazardous area latitude end
LONG_1 = -71 #hazardous area longitude start
LONG_2 = -70 #hazardous area longitude end

def meter_to_feet(meter):
    """
    (num) -> (num)
    Returns the conversion of a meter value in terms of feet
    
    >>> meter_to_feet(4.67)
    15.32
    >>>  meter_to_feet(0.01)
    0.03
    >>> meter_to_feet(50)
    164.0
    """
    feet = round(meter * FEET_CONV, 2)
    return feet

def degrees_to_radians(degrees):
    """
    (num) -> (num)
    Returns the conversion of a degree value in terms of radians
    
    >>> degrees_to_radians(180)
    3.14
    >>> degrees_to_radians(80.1)
    1.4
    >>> degrees_to_radians(0.9)
    0.02
    """    
    radians = round(degrees * RAD_CONV, 2)
    return radians

def get_vessel_dimensions():
    """
    (None) -> (num, num)
    Returns conversion of vessel length and width user input in meters to feet
    
    >>> get_vessel_dimensions()
    Enter the vessel length (in meter): 20
    Enter the vessel width (in meter): 15
    (65.6, 49.2)
    >>> get_vessel_dimensions()
    Enter the vessel length (in meter): 9.86
    Enter the vessel width (in meter): 3.47
    (32.34, 11.38)
    >>> get_vessel_dimensions()
    Enter the vessel length (in meter): 49.4
    Enter the vessel width (in meter): 20
    (162.03, 65.6)
    """    
    vessel_length = float(input("Enter the vessel length (in meter): "))
    vessel_width = float(input("Enter the vessel width (in meter): "))
    
    return meter_to_feet(vessel_length), meter_to_feet(vessel_width)

def get_valid_coordinate(val_name, min_float, max_float):
    """
    (str, num, num) -> (num)
    Returns the value number of user input after verifying it's within interval
    
    >>> get_valid_coordinate('latitude', -90, 90)
    What is your latitude ?-100
    Invalid latitude
    What is your latitude ?-87.6
    -87.6
    >>> get_valid_coordinate('longitude', -180, 180)
    What is your longitude ?-190,9
    Invalid longitude
    What is your longitude ?180.1
    Invalid longitude
    What is your longitude ?0
    0.0
    >>> get_valid_coordinate('y-coordinate', -10, 10)
    What is your y-coordinate ?-20
    Invalid y-coordinate
    What is your y-coordinate ?20
    Invalid y-coordinate
    What is your y-coordinate ?10
    Invalid y-coordinate
    What is your y-coordinate ?9
    9.0
    """    
    val_number = float(input("What is your " + val_name + " ?"))
    
    while (not min_float < val_number < max_float):
        print("Invalid",  val_name)
        val_number = float(input("What is your " + val_name + " ?"))
        
    return val_number

def get_gps_location():
    """
    (None) -> (num, num)
    Returns the GPS location after getting latitude and longitude from user
    
    >>> get_gps_location()
    What is your latitude ?86.70
    What is your longitude ?78.05
    (86.7, 78.05)
    >>> get_gps_location()
    What is your latitude ?-200
    Invalid latitude
    What is your latitude ?-90
    What is your longitude ?-90
    (-90.0, -90.0)
    >>> get_gps_location()
    What is your latitude ?90.1
    Invalid latitude
    What is your latitude ?89.9
    What is your longitude ?180.1
    Invalid longitude
    What is your longitude ?180
    (89.9, 180.0)
    """    
    latitude = get_valid_coordinate('latitude', MIN_LAT, MAX_LAT)
    longitude = get_valid_coordinate('longitude', MIN_LONG, MAX_LONG)
    
    return latitude, longitude
       
def distance_two_points(lat_1, long_1, lat_2, long_2):
    """
    (num, num, num, num) -> (num)
    Returns distance between two points by using their latitudes and longitudes
    
    >>> distance_two_points(45.508888,-73.561668, 45.508888,-73.561668)
    0.0
    >>> distance_two_points(64.9046,-17.561, 48.0,-179.347278)
    7362.92
    >>> distance_two_points(-89.32749, -179.819372, -86.89137, -178.109380)
    254.88
    """
    
    #Convert latitudes and longitudes to radians
    lat_1_rad = degrees_to_radians(lat_1)
    long_1_rad = degrees_to_radians(long_1)
    lat_2_rad = degrees_to_radians(lat_2)
    long_2_rad = degrees_to_radians(long_2)
    
    #Variables
    dist_long = abs(long_2_rad - long_1_rad)/2 #longitude distance divided by 2
    dist_lat = abs(lat_2_rad - lat_1_rad)/2 #latitude distance divided by 2
    cos_multiplication = math.cos(lat_1_rad) * math.cos(lat_2_rad) #the cosines
    #of the two latitudes multiplied
    
    #Calculate distance between two points
    step_1 = math.sin(dist_lat)**2 + cos_multiplication * math.sin(dist_long)**2
    step_2 = 2 * math.atan2(math.sqrt(step_1), math.sqrt(1 - step_1))
    distance_between = EARTH_RADIUS * step_2
    
    return round(distance_between, 2)

def check_safety(latitude, longitude):
    """
    (num, num) -> (None) 
    Displays the safety of the vessel depending on its location
    
    >>> check_safety(25.9827386, -69.0)
    Error: Restricted zone!
    >>> check_safety(40.36, -70.3)
    Warning: Hazardous area! Navigate with caution.
    >>> check_safety(43.9, -71.318497)
    Safe navigation.
    """
    if distance_two_points(latitude, longitude, REST_LAT, REST_LONG) <=MIN_DIST:
        print("Error: Restricted zone!")
        
    elif LAT_1 <= latitude <= LAT_2 and LONG_1 <= longitude <= LONG_2:
        print("Warning: Hazardous area! Navigate with caution.")
        
    else:
        print("Safe navigation.")

def get_max_capacity(length, width):
    """
    (num, num) -> (num) 
    Returns the maximum number of people the vessel can hold based on its size
    
    >>> get_max_capacity(0.5, 0)
    0
    >>> get_max_capacity(20, 5)
    6
    >>> get_max_capacity(45, 10)
    87
    """
    capacity = int((length * width)/CAP_CONS) #capacity when length = 26
    
    if length <= LENGTH_THRESHOLD:
        maximum_people = capacity
        
    else:
        maximum_people = int(capacity + ((length - LENGTH_THRESHOLD) * 3))
        
    return maximum_people

def passengers_on_boat(length, width, passenger):
    """
    (num, num, num) -> (bool) 
    Returns if the boat can carry the a number of passengers
    
    >>> passengers_on_boat(18, 6, 6)
    False
    >>> passengers_on_boat(24, 6, 4)
    True
    >>> passengers_on_boat(8, 6, 4)
    False
    """
    if passenger % 4 == 0 and passenger <= get_max_capacity(length, width):
        return True
    
    else:
        return False

def update_coordinate(position, min_float, max_float):
    """
    (num, num, num) -> (num) 
    Returns the updated coordinate after changing its value by a random number
    
    >>> update_coordinate(45.508888, -90, 90)
    36.56
    >>> update_coordinate(100, -180, 180)
    91.05
    >>> update_coordinate(20, -50, 50)
    11.05
    """
    random.seed(SEED) #set random seed to 123
    random_number = random.random() * RAND_INT - INTERVAL #limit in (-10, 10)
    new_position = position + random_number
    
    while not (min_float < new_position < max_float):
        random_number = random.random() * RAND_INT - INTERVAL 
        new_position = position + random_number
        
    else:
        return round(new_position, 2)
        
def wave_hit_vessel(vessel_latitude, vessel_longitude):
    """
    (num, num) -> (num, num) 
    Returns the new latitude and longitude values after updating coordinate
    
    >>> wave_hit_vessel(45.508888, -73.561668)
    Safe navigation.
    (36.56, -82.51)
    >>> wave_hit_vessel(41, -71)
    Safe navigation.
    (32.05, -79.95)
    >>> wave_hit_vessel(26.831867, -72.372378)
    Safe navigation.
    (17.88, -81.33)
    """
    new_latitude = update_coordinate(vessel_latitude, MIN_LAT, MAX_LAT)
    new_longitude = update_coordinate(vessel_longitude, MIN_LONG, MAX_LONG)
    check_safety(new_latitude, new_longitude)
    
    return new_latitude, new_longitude

def vessel_menu_options():
    """
    (None) -> (None)
    Displays the vessel menu options
    """
    print("Please select an option below: ")
    print("1. Check the safety of your boat")
    print("2. Check the maximum number of people that can fit on the boat")
    print("3. Update the position of your boat")
    print("4. Exit boat menu")
    
def vessel_menu():
    """
    (None) -> (None)
    Displays information based on user selection from the vessel menu
    """
    #Greet user
    print("Welcome to the boat menu!")
    
    #Display location
    [latitude, longitude] = get_gps_location()
    print("Your current position is at latitude", latitude, "and longitude\
", longitude)
    
    #Display vessel size in feet
    [vessel_length, vessel_width] = get_vessel_dimensions()
    print("Your boat measures", vessel_length, "feet by", vessel_width, "feet")
    
    #Display vessel menu options and get selection
    vessel_menu_options()
    selection = int(input("Your selection: "))
    
    while selection != 4:
        
        #Check safety of the boat
        if selection == 1:
            check_safety(latitude, longitude)
        
        #Display if the boat can hold entered amount of adults
        elif selection == 2:
            adult = int(input("How many adults go on the boat? "))
            capacity = passengers_on_boat(vessel_length, vessel_width, adult)
            if capacity:
                print("Your boat can hold", adult, "adults")
            else:
                print("Your boat cannot hold", adult, "adults")
        
        #Update position after waves hitting vessel
        elif selection == 3:
            [latitude, longitude] = wave_hit_vessel(latitude, longitude)
            print("Your new position is latitude of", latitude, "and longitude \
of", longitude)
        
        #Display vessel menu options and get selection until selection is 4
        vessel_menu_options()
        selection = int(input("Your selection: "))
    
    #Say farewell to the user
    print("End of boat menu.")
