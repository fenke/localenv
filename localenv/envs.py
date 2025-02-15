"""Fill in a module description here"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_core.ipynb.

# %% auto 0
__all__ = ['find_env_path', 'get_var_from_env_file', 'update_env_file']

# %% ../nbs/00_core.ipynb 3
import os, pathlib, json



# %% ../nbs/00_core.ipynb 5
def _create_getenv(env_vars:dict, def_getenv=os.getenv):
    '''Internal function to create a getenv function using the dict specified
    environment variabels and a fallback getenv function'''

    def _getenv(V, D=None):
        '''Locally created with user dictionary'''
        assert V is not None, f"Can not have '{str(V)}' as var name"
        return env_vars.get(V, def_getenv(V,D))

    return _getenv


# %% ../nbs/00_core.ipynb 14
def find_env_path(env_filename = '.env.json'):

    current_path = pathlib.Path.cwd()
    for p in current_path.parents:
        if p.joinpath(env_filename).exists():
            return p.joinpath(env_filename)

    return pathlib.Path.home().joinpath(env_filename)



# %% ../nbs/00_core.ipynb 18
#| eval: false
with open(find_env_path()) as f:
    env_vars = json.load(f)

for k, e in env_vars.items():
    globals()[k] = _create_getenv(env_vars=e)

#globals()['__all__'] = list(set(env_vars.keys()) | set(globals().get('__all__',[])))


# %% ../nbs/00_core.ipynb 23
def get_var_from_env_file(var_name, default_getenv=os.getenv, env_filename = '.env.json'):
    env_path = find_env_path(env_filename)
    with open(env_path) as f:
        env_vars = json.load(f)
    return env_vars.get(var_name, default_getenv(var_name))

# %% ../nbs/00_core.ipynb 27
def update_env_file(section, var_name, var_value, env_filename = '.env.json'):
    env_path = find_env_path(env_filename)
    with open(env_path) as f:
        env_vars = json.load(f)

    section_vars = env_vars.get(section, {})
    section_vars[var_name] = var_value
    env_vars[section] = section_vars

    with open(env_path, 'w') as f:
        json.dump(env_vars, f, indent=3, ensure_ascii=True)
