from setuptools import setup, find_packages
setup(
    name='cdhetero',
    version='0.1',
    packages=find_packages(include=['cdhetero*']),
    install_requires=['py3Dmol','absl-py','biopython',
                      'chex','dm-haiku','dm-tree',
                      'immutabledict','jax','ml-collections',
                      'numpy','pandas','scipy','tensorflow'],
)