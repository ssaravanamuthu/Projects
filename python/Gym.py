import gym
env = gym.make('FrozenLake-v0')
# env.render()
env.reset()

score = 0
for x in range(10000):
    env.reset()
    for _ in range(100):
        obs, rew, done, info=env.step(1)

        if done:
            if rew != 0:
                score = score + rew

            break

print(score)