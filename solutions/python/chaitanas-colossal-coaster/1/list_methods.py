
# Add a person to the correct queue
def add_me_to_the_queue(express_queue, normal_queue, ticket_type, person_name):
    if ticket_type == 1:
        express_queue.append(person_name)
        return express_queue
    else:
        normal_queue.append(person_name)
        return normal_queue


# Find a friend's position in the queue
def find_my_friend(queue, friend_name):
    return queue.index(friend_name)


#  Add a person at a specific position (to join friends)
def add_me_with_my_friends(queue, index, person_name):
    queue.insert(index, person_name)
    return queue


# Remove the mean person from the queue
def remove_the_mean_person(queue, person_name):
    queue.remove(person_name)
    return queue


# Count how many people share the same name
def how_many_namefellows(queue, person_name):
    return queue.count(person_name)


#  Remove the last person and return their name
def remove_the_last_person(queue):
    return queue.pop()


#  Return a sorted copy of the queue (alphabetical order)
def sorted_names(queue):
    return sorted(queue)
