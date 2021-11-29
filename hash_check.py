import hashlib
import requests
import json



def pw_hashed_salt():
    response = requests.get("http://10.30.10.55:5000/mqtt")
    aDict = json.loads(response.content)
    bDict = aDict['mqtt_user']
    #get pw+salt hash iz baze(password) i salt za usera
    hashBaza = bDict[0]['password']
    salt = bDict[0]['salt']
    return hashBaza,salt

    # print("Unesi mqtt lozinku za user Bob")
    # pw = input()


# hashToCheck = hashlib.sha256((pw+salt).encode()).hexdigest()

# print("Comparing:")
# print(hashToCheck + "\n" + hashBaza)
# if(hashToCheck == hashBaza):
#     print("AUTHORIZED")
# else:
#     print("UNAUTHORIZED")
