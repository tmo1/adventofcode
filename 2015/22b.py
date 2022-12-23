# https://adventofcode.com/2015/day/22#part2

import sys

words = sys.stdin.readline().split()
boss_starting_hp = int(words[-1])
words = sys.stdin.readline().split()
boss_damage = int(words[-1])
least = 1000000


def fight(player_stats, boss_hp, effects, spent, player_turn):
    global least
    player_stats_new = player_stats.copy()
    if player_turn:
        player_stats_new['hp'] -= 1
        if player_stats_new['hp'] == 0:
            return
    effects_new = effects.copy()
    player_stats_new['armor'] = 0
    for effect in effects_new.keys():
        if effect == 'Shield':
            player_stats_new['armor'] = 7
        elif effect == 'Poison':
            boss_hp -= 3
            if boss_hp <= 0:
                least = min(spent, least)
                return
        else:  # it's 'Recharge'
            player_stats_new['mp'] += 101
        effects_new[effect] -= 1
    effects_new = {key: val for key, val in effects_new.items() if val > 0}
    if player_turn:
        if player_stats_new['mp'] < 53 or least - spent < 53:
            return
        for j in range(5):
            player_stats_new_new = player_stats_new.copy()
            effects_new_new = effects_new.copy()
            spent_new = spent
            boss_hp_new = boss_hp
            if j == 0:
                player_stats_new_new['mp'] -= 53
                spent_new += 53
                boss_hp_new -= 4
            elif j == 1:
                if player_stats_new['mp'] >= 73:
                    player_stats_new_new['mp'] -= 73
                    spent_new += 73
                    boss_hp_new -= 2
                    player_stats_new_new['hp'] += 2
                else:
                    continue
            elif j == 2:
                if player_stats_new['mp'] >= 113 and 'Shield' not in effects_new:
                    player_stats_new_new['mp'] -= 113
                    spent_new += 113
                    effects_new_new['Shield'] = 6
                else:
                    continue
            elif j == 3:
                if player_stats_new['mp'] >= 173 and 'Poison' not in effects_new:
                    player_stats_new_new['mp'] -= 173
                    spent_new += 173
                    effects_new_new['Poison'] = 6
                else:
                    continue
            else:
                if player_stats_new['mp'] >= 229 and 'Recharge' not in effects_new:  # it's 'Recharge'
                    player_stats_new_new['mp'] -= 229
                    spent_new += 229
                    effects_new_new['Recharge'] = 5
                else:
                    continue
            if boss_hp_new <= 0:
                # print(player_stats, boss_hp, effects, spent_new, player_turn, stack)
                least = min(spent_new, least)
                continue
            fight(player_stats_new_new, boss_hp_new, effects_new_new, spent_new, False)
    else:
        player_stats_new['hp'] -= max(boss_damage - player_stats_new['armor'], 1)
        if player_stats_new['hp'] <= 0:
            return
        fight(player_stats_new, boss_hp, effects_new, spent, True)


fight({'hp': 50, 'mp': 500}, boss_starting_hp, {}, 0, True)
print(least)
