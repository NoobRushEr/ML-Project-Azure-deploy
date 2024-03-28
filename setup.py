from setuptools import find_packages,setup
from typing import List

HYPEn_E_DOT = '-e .'
def get_requiremets(file_path:str)->List[str]:
    '''
    This Function will return the list of requiremts
    '''
    requirements= []
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace('\n', '') for req in requirements]

        if HYPEn_E_DOT in requirements:
            requirements.remove(HYPEn_E_DOT)

    return requirements

setup(
    name='ML-Project',
    version='0.0.1',
    author='NoobRushEr',
    author_email='dipeshghag1234@gmail',
    packages=find_packages(),
    install_requires=get_requiremets('requirements.txt'),

)