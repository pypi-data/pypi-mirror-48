import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='fantasy-premier-league-stats',
    version='0.0.2',
    author='Göktuğ Erce Gürel',
    author_email='goktugercegurel@gmail.com',
    description='Stats and Visualizations for FPL, Fantasy Allsvenskan and Fantasy Eliteserien',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/goktugerce/fantasy-premier-league',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=requirements
)
