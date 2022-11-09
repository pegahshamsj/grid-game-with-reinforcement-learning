import random
import matplotlib.pyplot as plt

start = [1, 2]
gold = [4, 4]
w = [1, 2]
h1 = [2, 4]
h2 = [3, 1]
ACTIONS = [0, 1, 2, 3]
Q = {(i, j):[-1, -1, -1, -1] for i in range(-1, 6) for j in range(-1, 6)}
e = 1
l = 1
g = 0.9
reward_lst=[]


def move(state, action):
    i, j = state
    if action == 0:
        state = [i, j + 1]
    elif action == 1:
        state = [i, j - 1]
    elif action == 2:
        state = [i - 1, j]
    elif action == 3:
        state = [i + 1, j]
    reward = -1.0
    if i + 1 > 4 and action == 3:
        reward = -100
    if i - 1 < 0 and action == 2:
        reward = -100
    if j + 1 > 4 and action == 0:
        reward = -100
    if j - 1 < 0 and action == 1:
        reward = -100

    if state == gold:
        reward = 100
    if state == w:
        reward = -100
    if state == h1 or state == h2:
        reward = -100
    return state, reward


for i in range(1000):
    now = start
    flag = False
    episode_reward = []
    for j in range(100):
        if random.random() < e:
            ACTION = random.choice(ACTIONS)
        else:
            ACTION = Q[tuple(now)].index(max(Q[tuple(now)]))
        next_place, prize = move(now, ACTION)
        episode_reward.append(prize)
        value = max(Q[tuple(next_place)])
        Q[tuple(now)][ACTION] = l * (prize + g * value) + (1 - l) * Q[tuple(now)][ACTION]
        if prize == 100:
            l *= 0.99
            e *= 0.98
            flag = True
            break
        if prize == -100:
            break
        now = next_place
    reward_lst.append(sum(episode_reward))

now = start
print(start)
flag = False
for j in range(10):
    ACTION = Q[tuple(now)].index(max(Q[tuple(now)]))
    next_place, prize = move(now, ACTION)
    if prize == 100:
        flag = True
        break
    print(next_place)
    now = next_place
print(gold)

plt.plot(reward_lst)
plt.show()
