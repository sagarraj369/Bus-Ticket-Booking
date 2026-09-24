class database:
    def __init__(self):
        self.__storage = {}  # private

    def write(self, key, value):
        self.__storage[key] = value

    def read(self, key):
        if key in self.__storage:
            print(self,self.__storage[key])
        else:
            print("db item not avaibale")
       
db = database()
db.write("subscribers","100k")
db.read("subscribers")
db.write("name","sagar")

db.read("name")