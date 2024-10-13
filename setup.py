from setuptools import setup, find_packages
from typing import List


def get_requirements() ->List[str]:
    '''
    This function will return a list of requirements'''
    requirement_list:List[str]=[]
    try:
        with open('requirements.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                requirement = line.strip()

                if requirement != "-e .":
                    requirement_list.append(requirement)
            
    except FileNotFoundError:
        print("requirements.txt not found")
        

setup(
    name='Network Security',
    version='1.0.0',
    author='Carlos Vasconez',
    author_email='carvas91@hotmail.com',
    packages=find_packages(),
    install_requires= get_requirements()
)
