# -*- encoding:utf-8 -*-
from distutils.core import setup

setup(
    name = 'pysub',
    packages = ['pysub'],
    version = '0.2',
    description = 'Library to manipulate SubRip subtitles',
    author = 'Salvador de la Puente González',
    author_email = 'neo.salvador@gmail.com',
    url = "http://unoyunodiez.wordpress.com/pysub/",
    download_url = "https://github.com/lodr/pysub/zipball/master",
    keywords = ['subtitle', 'video', 'srt', 'synchronization'],
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Other Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU General Public License (GPL)",
	    "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Topic :: Multimedia :: Video",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    long_description = """\
This module contains the class SubtitleStream to load SubRip subtitles format.
See the class for extended documentation but basically you can load a SubRip
(.srt) file shift it backward / forward, edit the text or check for sequence
integrity.

Instances of SubtitleStream act like sequences so they are iterable and you
can get slices of it.

You can save() the stream as well.
"""
)
