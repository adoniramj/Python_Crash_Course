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


friendships = {user["id"]:[] for user in users} # dict comprehension

for i, j in friendship_pairs: # is the firt member of the tuple, j the second
    friendships[i].append(j)
    friendships[j].append(i)
    
    
def number_of_friends(user):
    user_id = user["id"] # retrieves the id number
    friends_ids = friendships[user_id] # using id number retrieves the a list of friends
    return len(friends_ids) # return how many friends user["id"] has

total_connections = sum(number_of_friends(user) for user in users) 


# how many friends each user has (friend, number)
num_of_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]
# returns a list of tuples

# Who has the most friends
num_of_friends_by_id.sort(
    key =lambda tup : tup[1], #looping through each tup of num_of_friends_by_id and returning tup[1]
    reverse = True)

# With whom does a user has friends in common?
from collections import Counter
# Dict subclass for counting hashable items.

def friends_of_friends(user): # user is a dict
    user_id = user["id"] # retrieving value
    return Counter(
        foaf_id 
        for friend_id in friendships[user_id] # list of friends of user_id
        for foaf_id in friendships[friend_id] # who are the friends of friend_id
        if foaf_id != user_id and foaf_id not in friendships[user_id] #it is not me and it is not a direct friend
    )

result_f_o_f = friends_of_friends(users[0])

interests = [(0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"), (0, "Spark"), (0, "Storm"), (0, "Storm")\
             ,(1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"), (1, "Postgres")\
             ,(2, "Python"), (2, "scikit-learn"),(2, "statsmodels"), (2, "pandas")\
            ,(3, "R"), (3, "Python"), (3, "statistics"), (3, "regression"), (3, "probability"), (3, "pandas")\
            ,(4, "machine learning"), (4, "regression"), (4, "decision trees"), (4, "libsvm")\
            ,(5, "Python"), (5, "R"), (5, "Java"), (5, "C++"), (5, "Haskell"), (5, "programming languages")]

# Who likes Python, or R, ....
def data_scientist_who_like(target_interest):
    return [user_id for user_id, user_interest in interests if user_interest == target_interest]

like_python = data_scientist_who_like("Python")
# explanation of results
# user 2, 3 ,and 5 like Python

from collections import defaultdict
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)
    
user_ids_by_interest["Python"]

interests_by_user_id = defaultdict(list)
for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)
    