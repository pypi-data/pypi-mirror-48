# -*- encoding: utf-8 -*-

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
  name = 'yamwapi',
  packages = ['yamwapi'],
  version = '0.3',
  description = 'A simple and modern library for interacting with the MediaWiki API. Use me to talk to Wikipedia.',
  author = 'Guilherme Gonçalves',
  author_email = 'guilherme.p.gonc@gmail.com',
  url = 'https://github.com/eggpi/yamwapi', # use the URL to the github repo
  download_url = 'https://github.com/eggpi/yamwapi/archive/0.3.tar.gz',
  keywords = 'wikipedia mediawiki',
  classifiers = [],
)
