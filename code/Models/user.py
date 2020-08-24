class User:
    def __init__(self, _id, name, password):
        self.id = _id
        self.name = name
        self.password = password
        
    def __str__(self):
        return "User(id='%s')" % self.id