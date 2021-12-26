from setuptools import setup

with open('README.md', 'r', encoding="utf-8") as file:
    long_description = file.read()

VERSION = '1.1'
AUTHOR = 'Manuel Cabral'
EMAIL = 'cabral.manuel@yandex.com'
DESCRIPTION = 'Obtención e información de datos sobre el COVID-19 en Argentina'
LICENSE = 'apache-2.0'

setup(
  name = 'codavi',
  packages = ['codavi'],
  version = VERSION,
  license = LICENSE,
  description = DESCRIPTION,
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  author = AUTHOR,
  author_email = EMAIL,
  url = 'https://github.com/manucabral/Codavi',
  keywords = ['python', 'covid', 'covid-19', 'covid19-data', 'covid19-argentina'],
  install_requires = ['requests', 'pandas'],
  python_requires = '>= 3.9',
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache Software License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.9',
    'Operating System :: Unix',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
  ],
)