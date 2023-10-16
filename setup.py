from setuptools import find_packages,setup
from typing import List
# find_package will automatically find out all the packages in the directory we have created


HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements


# We can consider setup as a metadata information for the project
setup (
    name='ml_Project',
    version='0.0.1',
    author='Jahid Hasan',
    author_email='jmhasan17@gmail.com',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')
)