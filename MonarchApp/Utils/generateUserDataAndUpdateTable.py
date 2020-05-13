from ..models import users
from ..Utils.generateUniqueTimestamp import generate_timestamp

def updateUserTable(email,password):
    print("email and password are:  ",email,password)
    userKey = generate_timestamp()
    print("user token",userKey)
    userInfo = users.objects.create(user_email=email,user_key = userKey)
    print(userInfo.email)
    return userKey
