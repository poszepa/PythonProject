import random


treasures = [
    {"typTreasure" : "green", "chance" : 0.75, "reward" : 1000},
    {"typTreasure" : "orange", "chance" : 0.20, "reward" : 4000},
    {"typTreasure" : "purple", "chance" : 0.04, "reward" : 9000},
    {"typTreasure" : "gold", "chance" : 0.01, "reward" : 16000}
]

def is_get_reward(chance_to_get_reward_int):
    return random.choices(["Get reward", "Nothing"], [chance_to_get_reward_int, 100 - chance_to_get_reward_int])[0]

def print_success_get_treasure(treasure):
    print("""
    Congratulation!!!
    You got:""",treasure["typTreasure"],"""
    In treasure you found:""",treasure["reward"])



def run_program_dungeon():
    sumReward = 0
    treasure_chance = [treasure.get("chance") for treasure in treasures]
    for i in range(4):
        get_player_reward = is_get_reward(40)
        if(get_player_reward == "Get reward"):
            player_get_treasure = random.choices(treasures, treasure_chance)[0]
            print_success_get_treasure(player_get_treasure)
            sumReward += player_get_treasure["reward"]
    print("\nPlayer got:", sumReward)
