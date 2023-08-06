"""A setuptools based setup module.
See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://santhoshse7en.github.io/news_fetch/
https://santhoshse7en.github.io/news_fetch_doc/
"""
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

# Always prefer setuptools over distutils
import setuptools

keywords = ['Newspaper', "news_fetch", "without-api", "google_scraper", 'news_scraper', 'bs4', 'lxml',]

setuptools.setup(
    name="news_fetch",
    version="0.0.3",
    author="M Santhosh Kumar",
    author_email="santhoshse7en@gmail.com",
    description="A Python Package which helps to scrape news details",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://santhoshse7en.github.io/news_fetch/",
    keywords = keywords,
    install_requires=['beautifulsoup4', 'pandas', 'selenium', 'pattern', 'fake_useragent', 'nltk', 'chromedriver-binary==74.0.3729.6.0'],
    packages = setuptools.find_packages(),
    classifiers=['Development Status :: 4 - Beta',
              'Intended Audience :: End Users/Desktop',
              'Intended Audience :: Developers',
              'Intended Audience :: System Administrators',
              'License :: OSI Approved :: MIT License',
              'Operating System :: OS Independent',
              'Programming Language :: Python',
              'Topic :: Communications :: Email',
              'Topic :: Office/Business',
              'Topic :: Software Development :: Bug Tracking',
              ],
)
