def zombie_vs_plants(zombie: list, plant: list) -> bool:
    max_soldat = len(plant) if len(plant) > len(zombie) else len(zombie)
    live_plants = 0
    live_zombie = 0
    if len(plant) < max_soldat:
        plant.extend([0] * (max_soldat - len(plant)))
    if len(zombie) < max_soldat:
        zombie.extend([0] * (max_soldat - len(zombie)))
    for soldat in range(max_soldat):
        if zombie[soldat] > plant[soldat]:
            live_zombie += 1
        if zombie[soldat] < plant[soldat]:
            live_plants += 1
        else:
            pass
    if live_zombie == live_plants:
        max_power_plant = 0
        max_power_zombie = 0
        for soldat in range(max_soldat):
            max_power_plant += plant[soldat]
            max_power_zombie += zombie[soldat]
        return True if max_power_plant >= max_power_zombie else False
    return live_plants > live_zombie


print(zombie_vs_plants([1, 3, 5, 7], [2, 4, 6, 8]))
print(zombie_vs_plants([1, 3, 5, 7], [2, 4]))
print(zombie_vs_plants([1, 3, 5, 7], [2, 4, 0, 8]))
print(zombie_vs_plants([2, 1, 1, 1], [1, 2, 1, 1]))
