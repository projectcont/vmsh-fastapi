import os
from pathlib import Path
import paths_


def path(format=0):
    '''
    BASE_DIR = Path(__file__).resolve().parent
    print()
    print('project_directory=',BASE_DIR)
    print('            ', os.getcwd())
    print('            ', os.path.abspath(os.curdir))
    print('project_directory=',os.path.dirname(os.path.abspath(__file__)))
    print()

    '''
    rootfolder_ = os.path.dirname(os.path.abspath(__file__))
    if format == 1:
        rootfolder = Path(rootfolder_)
    else:
        rootfolder = rootfolder_

    print(f' rootfolder= {rootfolder} ')
    return rootfolder
