users = [
    {"id" : 0, "name" : "Hero"},
    {"id" : 1, "name" : "Dunn"},
    {"id" : 2, "name" : "Sue"},
    {"id" : 3, "name" : "Chi"},
    {"id" : 4, "name" : "Thor"},
    {"id" : 5, "name" : "Clive"},
    {"id" : 6, "name" : "Hicks"},
    {"id" : 7, "name" : "Devin"},
    {"id" : 8, "name" : "Kate"},
    {"id" : 9, "name" : "Klein"}
]

friendship_pairs = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(4,5),(5,6),(5,7),(6,8),(7,8),(8,9)]

friendships = {user["id"]:[] for user in users}

for i, j in friendship_pairs: # is the firt member of the tuple, j the second
    friendships[i].append(j)
    friendships[j].append(i)

from collections import Counter

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(\
        foaf_id \
            for friend_id in friendships[user_id] \
                for foaf_id in friendships[friend_id] \
                    if foaf_id != user_id and foaf_id not in friendships[user_id])

result = friends_of_friends(users[4])
print(result)