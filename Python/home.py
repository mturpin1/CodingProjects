store = {
    'bedroom': ['shirt','shoes','pants','book'],
    'bathroom': ['toilet paper','soap','shampoo','mouthwash'],
    'living room': ['remote','blanket','controller','charger'],
    'garage': ['car','bike pump','tools','junk'],
    'kitchen': ['silverware','plates','spoons','forks'],
    'office': ['paper','charger','keyboard','speakers']
}
num = 0
room = input('What room are you in? ')
for item in store.keys():
    print(f'The {store[room][num]} should be stored in the {room}.')
    num += 1
