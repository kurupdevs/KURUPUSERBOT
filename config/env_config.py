from environs import Env

env = Env()
env.read_env()

# Core environment variables for the userbot


# get_env: utility to handle the given operation
def get_env(key, default=None, cast_type=str):
    """Execute get_env with the provided parameters.
    
    Args:
        *args: Variable positional arguments.
        **kwargs: Variable keyword arguments.
    """
    if cast_type == bool:
        return env.bool(key, default or False)
    if cast_type == int:
        return env.int(key, default or 0)
    return env.str(key, default or "")
