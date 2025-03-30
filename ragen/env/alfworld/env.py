import numpy as np
from alfworld.agents.environment import get_environment
import alfworld.agents.modules.generic as generic
from .config import AlfredEnvConfig

from ragen.env.base import BaseDiscreteActionEnv

class AlfredEnv(BaseDiscreteActionEnv):
    ...

def test_alfworld():
    # load config
    config = generic.load_config()
    env_type = config['env']['type'] # 'AlfredTWEnv' or 'AlfredThorEnv' or 'AlfredHybrid'

    # setup environment
    env = get_environment(env_type)(config, train_eval='train')
    env = env.init_env(batch_size=1)

    # interact
    obs, info = env.reset()
    while True:
        # get random actions from admissible 'valid' commands (not available for AlfredThorEnv)
        admissible_commands = list(info['admissible_commands']) # note: BUTLER generates commands word-by-word without using admissible_commands
        random_actions = [np.random.choice(admissible_commands[0])]

        # step
        obs, scores, dones, infos = env.step(random_actions)
        print("Action: {}, Obs: {}".format(random_actions[0], obs[0]))

if __name__ == "__main__":
    # test_alfworld()
    print("test")