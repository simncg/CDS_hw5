import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

def get_requirements(requirements_path='requirements.txt'):
    with open(requirements_path) as fp:
        return [x.strip() for x in fp.read().split('\n') if not x.startswith('#')]


setuptools.setup(
    name="computingds-hw5-simncg",
    version="0.0.2",
    author="Simón Caicedo",
    author_email="simncg@gmail.com",
    description="This package solves homework 5 of CDS course",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    setup_requires = ['pytest-runner', 'wheel'],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires = get_requirements()
)