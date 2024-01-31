from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."


def get_requirements(file_path: str) -> List[str]:
    with open(file_path, "r") as file:
        requirements = file.readlines()
        require_lst = [req.replace("\n", "") for req in requirements]

        if HYPEN_E_DOT in require_lst:
            require_lst.remove(HYPEN_E_DOT)
        return require_lst


setup(
    name="DiamondPricePrediction",
    version="0.0.1",
    author="Himal Mevada",
    author_email="developer.himal@gmail.com",
    install_requires=get_requirements("requirements.txt"),
    package=find_packages()
)
