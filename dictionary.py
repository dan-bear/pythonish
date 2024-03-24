def dictionaryExample():
    # A data structure that saves key-value pairs.
    # under the constraint that keys must be unique.
    userAndIdDic = {}
    userIdDic["user1"] = 1 #insert a new key value pair.
    userIdDic["user3"] = 3
    userIdDic["user2"] = 2
    del userIdDic["user1"] #delete a key
    userIdDic["user5"] = 3 #only the keys must be unique. 
    userIdDic["user5"] = 5 #update the value of existing key.
    if "user2" in userIdDic:
        print(f"user2 is in use, please choose anothexz r user name")
    if "user7" not in userIdDic:
        print(f"user7 is available")
    for user, id in userIdDic.items():
        print(f"user: {user}, id: {id}")}")


if __name__ == "__main__":
    dictionaryExample()
