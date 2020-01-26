from setuptools import find_packages, setup

setup(
    name='skool_car',
    author='Baptiste OJEANSON',
    author_email='bapo@octo.com',
    description='skool car piloting program',
    packages=find_packages(exclude=['tests.*', 'tests', 'functional_tests']),
    python_requires='~=3.6',
    entry_points={
        'console_scripts': [
            'skool_car = skool_car.application.__main__:main',
        ],
    },
    version='0.1.0'
)
