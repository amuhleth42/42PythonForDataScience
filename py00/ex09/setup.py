from setuptools import setup, find_packages


with open("./README.md") as readme_file:
    long_description = readme_file.read()

setup(
    name='ft_package',
    version='0.0.1',
    description='A package exemple',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='amuhleth',
    license="MIT",
    author_email='amuhleth@student.42lausanne.ch',
    url='yo that is my url',
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    entry_points={
        'console_scripts': [],
    },
)
