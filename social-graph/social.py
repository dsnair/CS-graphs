import random

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}


    # Creates a bi-directional friendship
    def addFriendship(self, userID, friendID):
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)


    # Create a new user with a sequential integer ID
    def addUser(self, name):
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()


    # Takes a number of users and an average number of friendships as arguments
    # Creates that number of users and a randomly distributed friendships between those users.
    # The number of users must be greater than the average number of friendships.
    def populateGraph(self, numUsers, avgFriendships):
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}

        # Add users
        for i in range(numUsers):
            self.addUser(f"divya{i}")

        # Create friendships
        possibleFriendships = []

        for userID in self.users:
            # don't include your userID in range
            for friendID in range(userID + 1, self.lastID + 1):
                possibleFriendships.append((userID, friendID))

        random.shuffle(possibleFriendships)
       
        for i in range((numUsers * avgFriendships) // 2):
            friendship = possibleFriendships[i]
            self.addFriendship(friendship[0], friendship[1])


    # Takes a user's userID as an argument
    # Returns a dictionary containing every user in that user's
    # extended network with the shortest friendship path between them.
    # The key is the friend's ID and the value is the path.
    def getAllSocialPaths(self, userID):
        visited = {}
        
        return visited


if __name__ == '__main__':
    sg = SocialGraph()

    sg.populateGraph(10, 2)
    print("Friendships:", sg.friendships)

    connections = sg.getAllSocialPaths(1)
    print("Connections:", connections)