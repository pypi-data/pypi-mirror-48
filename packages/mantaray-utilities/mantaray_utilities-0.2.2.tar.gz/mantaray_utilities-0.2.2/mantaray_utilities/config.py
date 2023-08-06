import os
import logging
from pathlib import Path

CONFIG_MAP = {
    'JUPYTER_DEPLOYMENT': {
        'config_ini_name': 'config_jupyter.ini',
    },
    'JUPYTER_DEPLOYMENT_TEST': {
        'config_ini_name': 'config_local.ini',
    },
    'USE_K8S_CLUSTER': {
        'config_ini_name': 'config_k8s_deployed.ini',
    },
    'DEFAULT': {
        'config_ini_name': 'config_local.ini',
    },
}
SCRIPT_FOLDERS = ['0_notebooks_verify', '1_notebooks_blocks', '2_notebooks_use_cases', '3_notebooks_demos']

def get_deployment_type():
    if 'JUPYTER_DEPLOYMENT' in os.environ:
        return 'JUPYTER_DEPLOYMENT'
    if 'USE_K8S_CLUSTER' in os.environ:
        return 'USE_K8S_CLUSTER'
    if 'JUPYTER_DEPLOYMENT_TEST' in os.environ:
        return 'JUPYTER_DEPLOYMENT_TEST'
    else:
        return 'DEFAULT'

def name_deployment_type():
    if 'JUPYTER_DEPLOYMENT' in os.environ:
        logging.info("Environment configuration detected: JupyterHub cluster.".format())
    elif 'JUPYTER_DEPLOYMENT_TEST' in os.environ:
        logging.info("Environment configuration detected: JupyterLab local testing.".format())
    elif 'USE_K8S_CLUSTER' in os.environ:
        logging.info("Environment configuration detected: Use deployed k8s endpoints.".format())
    else:
        logging.info("Environment configuration detected: Local machine with start-ocean local components.".format())

def get_config_file_path():
    # The configuration ini file is in the root of the project
    proj_path = get_project_path() / CONFIG_MAP[get_deployment_type()]['config_ini_name']
    assert proj_path.exists(), "{} not found".format(proj_path)
    return proj_path

def get_project_path():
    if get_deployment_type() == 'JUPYTER_DEPLOYMENT':
        # Detect a jupyter notebook running within one of the allowed folders
        return Path.home() / 'mantaray_jupyter'
        # if any(folder == Path.cwd().parts[-1] for folder in SCRIPT_FOLDERS):
        #     # Go up to the parent, this is the project root
        #     return Path.cwd().parents[0]
        # else:
        #     print("JUPYTER_DEPLOYMENT is set, but can't find the correct paths!")
        #     raise EnvironmentError
    elif get_deployment_type() == 'JUPYTER_DEPLOYMENT_TEST':
        this_path =  Path.cwd() / '..' / '..'
        return this_path.resolve()
    elif get_deployment_type() == 'USE_K8S_CLUSTER':
        return Path.cwd()
    elif get_deployment_type() == 'DEFAULT':
        return Path.cwd()
    else:
        raise NameError

    # print(Path.cwd())
# if not 'PATH_PROJECT' in locals():
#     PATH_PROJECT = Path.cwd()
# print("Project root path:", PATH_PROJECT)


if 0:
    from pathlib import Path
    # Ensure paths are correct in Jupyter Hub
    # The PATH_PROJECT path variable must be the root of the project folder
    # By default the root is the current working directory
    PATH_PROJECT = Path.cwd()

    # But if run as a Jupyter Notebook, the cwd will be one of:
    SCRIPT_FOLDERS = ['0_verify', '1_blocks', '2_use_cases', '3_demos']

    if any(folder == Path.cwd().parts[-1] for folder in SCRIPT_FOLDERS):
        # Go up to the parent
        PATH_PROJECT = Path.cwd().parents[0]

    assert PATH_PROJECT.parts[-1] == 'mantaray_jupyter'