import os
from pathlib import Path
import paths_


def path(format=0):

    rootfolder_ = os.path.dirname(os.path.abspath(__file__))
    if format == 1:
        rootfolder = Path(rootfolder_)
    else:
        rootfolder = rootfolder_

    print(f' rootfolder= {rootfolder} ')
    return rootfolder
