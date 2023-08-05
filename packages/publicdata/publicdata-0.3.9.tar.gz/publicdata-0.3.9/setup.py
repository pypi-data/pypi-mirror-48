from setuptools import  find_packages, setup
import sys
import os

if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

setup(
    name='publicdata',
    version='0.3.9',
    url='https://github.com/CivicKnowledge/publicdata',
    license='MIT',
    author='Eric Busboom',
    author_email='eric@busboom.org',
    description='Metatab support code for working with public datasets',
    packages=find_packages(),
    zip_safe=True,
    install_requires=[
        'fs >= 2',
        'rowgenerators',
        'pandas',
        'requests',
        'geoid',
        'tqdm',
        'fuzzy', # For NLSY
        'nltk', # for NLSY
        'stringdist' # For NLSY
        ],
    entry_points={
        'appurl.urls': [
            "censusreporter: = publicdata.census.censusreporter:CensusReporterURL",
            "censusreportergeo: = publicdata.census.censusreporter:CensusReporterShapeURL",
            "census: = publicdata.census.files.appurl:CensusFile",
            "censusgeo: = publicdata.census.files.appurl:CensusGeoUrl",
            "nlsy+ = publicdata.nlsy.appurl:NlsyUrl"
        ],
        'rowgenerators': [
            "CRJSON+ = publicdata.census.censusreporter:CensusReporterSource",
            "census: = publicdata.census.files.generators:CensusSource",
            "censusgeo: = publicdata.census.files.generators:CensusGeoSource"
        ],
        'console_scripts': [
            'nlsy = publicdata.nlsy.__main__:main'
        ]
    },
)

