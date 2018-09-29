# 1)
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]
x[1][0] = 15
print(x)
students[0]['last_name'] = "Bryant"
print(students)
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
z[0]['y'] = 30
print(z)

# 2)
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def numbertwo():
    for i in range(len(students)):
        for key, val in students[i].items():
            print(key," - ", val)
numbertwo()

# 3)
def iterateDict2():
    for i in range(len(students)):
        print(students[i]['first_name'])
iterateDict2()

# 4)
dojo = {
   'location': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printDojoInfo(dojo):
    num_loc = len(dojo['location'])
    num_ins = len(dojo["instructors"])
    print(num_loc, "LOCATIONS")
    for i in range(len(dojo['location'])):
        print(dojo['location'][i])
    print(" ")
    print(num_ins, "INSTRUCTORS")
    for i in range(len(dojo['instructors'])):
        print(dojo['instructors'][i])
printDojoInfo(dojo)
#SWAP
arr = [1,3,5,7]
arr[0], arr[1],arr[2], arr[3] = arr[3], arr[2], arr[1], arr[0]
print(arr)
# import the library
import urllib.request
response = urllib.request.urlopen("http://www.codingdojo.com")
html = response.read()
print(html)
