# -*- encoding:utf-8 -*-
from distutils.core import setup

setup(
    name = 'pyraphrase',
    packages = ['pyraphrase'],
    version = '0.1',
    description = 'Linguistics-related library',
    author = 'Salvador de la Puente González',
    author_email = 'neo.salvador@gmail.com',
    url = "http://unoyunodiez.wordpress.com/pyraphrase/",
    download_url = "https://github.com/lodr/pyraphrase/zipball/master",
    keywords = ['linguistics', 'paraphrases', 'diff', 'ratcliff', 'obershelp'],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License (GPL)",
	    "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
	    "Topic :: Text Processing :: Linguistic",
    ],
    long_description = """\
pyraphrase is the result of an academic project to extract paraphrases from a subtitle corpus by using some statistical metrics. This library only contains one method get_paraphrases() but it is intended to be completed with more linguistics-related functionallity.
"""
)
