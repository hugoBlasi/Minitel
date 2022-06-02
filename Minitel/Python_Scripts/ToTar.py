import tarfile
import os
import datetime
from pathlib import Path

def CreateTar() :

    
    file_name = Path(os.path.expanduser('~'),datetime.datetime.now().isoformat()+' Data.tar')

       
    file_to_add = Path('user.json')
       
    file_to_add2 = Path('network.json')
      
     

    tarfile_obj = tarfile.open(file_name,'w')

    tarfile_obj.add(file_to_add)
    tarfile_obj.add(file_to_add2)

    tarfile_obj.close()
    os.remove('user.json')
    os.remove('network.json')

