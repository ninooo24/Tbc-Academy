FINISH_KEYWORD = "finish!"


friends = {}

while True:
    user_input = input("Enter names or finish:")
    if user_input.lower() == FINISH_KEYWORD:
        break

    friend, other_friend = user_input.split(" ")
    if friend in friends:
        friends[friend] += str(other_friend)
    else:
        friends[friend] = str(other_friend)

for friend, other_friend in friends.items():
    print(friend, "-", other_friend, friends[other_friend])
