from setuptools import setup

setup(name='idyalog',
      version='0.1.0',
      description='A Dyalog APL kernel for Jupyter',
      author='TomaSajt',
      license='MIT',
      url="https://github.com/TomaSajt/idyalog",
      install_requires=['notebook >= 4.0'],
      packages=['dyalog_kernel'],
)
