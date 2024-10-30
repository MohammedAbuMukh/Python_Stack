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
print(x[1][0])
print(x)

students[0]['last_name'] ='Bryant'
print(students[0])

sports_directory['soccer'][0]='Andres'
print(sports_directory['soccer'])

z[0]['y']=30
print(z)
