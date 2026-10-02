player_hp = 300
enemy_hp = 350
print("A wild boar appears!")

while player_hp > 0 and enemy_hp > 0:
    print(f"Your HP: {player_hp}")
    print(f"Enemy HP: {enemy_hp}")
    print("1. Attack!")
    print("2. Block!")
    print("3. Heal!")
    action = input("Choose an action (1/2/3): ")

    blocking = False
    if action == '1':
        enemy_hp -= 35
    elif action == '2':
        blocking = True
        print("Incoming attack!")
    elif action == '3':
        if player_hp + 20 > 300:
           player_hp = 300
        else:
           player_hp += 20
        

    #enemy actions
    if blocking == False:
        player_hp -= 30
    else:
        player_hp -= 15
if player_hp <= 0:
    print("You lose!")
elif enemy_hp <= 0:
    print("You win!")