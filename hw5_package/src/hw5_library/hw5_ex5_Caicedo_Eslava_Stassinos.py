
 

# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#

def car_at_light(light):
    if light == 'red':
        return 'stop'
    elif light == 'yellow':
        return 'wait'
    elif light == 'green':
        return 'go'
    else:
        raise Exception('Undefined instruction for color: '+light)
        
#car_at_light('black')

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 

def safe_subtract(x,y):
    try:
        return y-x
    except (TypeError):
        return None
    except Exception as err:
        print(err)
    
#safe_subtract(None, 2)
    

# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

from datetime import datetime 
person1 = {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
person2 = {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
#EAFP
def retrieve_age_eafp(dict):
    try:
        age = datetime.datetime.now().year - dict['birth']
        return age
    except KeyError as e:
        print(e, 'Keys for calculating age are missing')
        raise
#LBYL
def retrieve_age_lbyl(person):
    if 'birth' in person:
        return datetime.datetime.now().year-person['birth']
    else:
        raise KeyError('birth not defined')

# retrieve_age_eafp(person_m)
# retrieve_age_lbyl(person_m)


# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#
import pandas as pd

def read_data(file):
    try:
        return pd.read_csv(file) 
    except FileNotFoundError:
        raise
      
      


# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)
# In the last line the code us adding up the wrong object
total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    #total_double_sum += elem
    total_double_sum += double
    
### (b)
# The code is missing an "s" in the last line, which is the only letter that
# differentiates the objects
strings = ''
for string in ['I', 'am', 'Groot']:
    #strings = string+"_"+string
    strings = strings+"_"+string

### (c) Careful!
# This while loop will never end since j will be always greater than 0
j=10
while j > 0:
   #j += 1
    j -= 1
    
### (d)
# productory object will be always be equal to 0 since it is the initial 
# number stored
#productory = 0
productory = 1
for elem in [1, 5, 25]:
    productory *= elem


################################################
##### Try to use map and reduce in the next 3 exercises
# 6)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#

slist = ["Simba and Nala are lions.", "I laugh in the face of danger.", "Hakuna matata", 
     "Timon, Pumba and Simba are friends, but Simba could eat the other two.", "Simba Simba"] 

def count_simba(x):
    return sum(map(lambda y : y.split().count("Simba") , x))
   
count_simba(slist)


    
# 7)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

import datetime

def get_day_month_year(x):
    df = pd.DataFrame({'x': x})
    df['day'] = df['x'].dt.strftime('%d')
    df['month'] = df['x'].dt.strftime('%m')
    df['year'] = df['x'].dt.strftime('%Y')
    df = df.drop(columns='x')
    return df



today = datetime.datetime(2021, 11, 14)
dates = [today]
for i in range(1, 5):
    date = today - datetime.timedelta(days=i)
    dates.append(date)
    
x = get_day_month_year(dates)
x
                     

# 8) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

location = [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8))]

from geopy import distance
def compute_distance(m):
    return list(map(lambda x: distance.distance(x[0], x[1]).km, m))

compute_distance(location)

#################################################
# 9)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#

list_0 = [[2], 3, [[1,2],5]] 
list_1 = [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1] 

def sum_general_int_list(listn):
    r = 0
    for x in listn:
        if isinstance(x, int):
            r += x
        else:
            r += sum_general_int_list(x)
    return r

sum_general_int_list(list_0)
sum_general_int_list(list_1)


