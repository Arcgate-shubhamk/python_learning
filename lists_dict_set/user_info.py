user = {}

name = input("what's your name?  ")
age = input("your age")
print("enter comma separeted values for next two")
fav_movies = input("favourite movies comma  ").split(',')
fav_songs = input("favourite songs , ").split(',')


user['name']=name
user['age']=age
user['favourite-movie'] = fav_movies
user['favourite songs'] = fav_songs

for key, value in user.items():
   print(f"{key}:{value}")
    