import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='SnakeDir-v0',
    entry_point='snake_gymDirected.envs:SnakeEnvDir',
    # timestep_limit=1000,
    # reward_threshold=1.0,
    # nondeterministic = True,
)

