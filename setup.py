from setuptools import setup, find_packages

def parse_requirements(filename):
    with open(filename, "r") as file:
        return [line.strip() for line in file if line and not line.startswith("#")]

setup(
    name="mylolcli",
    version="0.1.0",
    description="A CLI tool for interacting with the Riot API to retrieve summoner information.",
    author="Manuel Pizano",
    author_email="antarinho@proton.me",
    url="https://github.com/maniakapps/mylolcli",
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    install_requires=parse_requirements("requirements.txt"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        "console_scripts": [
            "mylolcli = api_wrapper.cli:main",
        ],
    },
)
