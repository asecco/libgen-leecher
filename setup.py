from setuptools import setup, find_packages

setup(
    name = "LibGen-Leecher",
    description = 'Library Genesis downloader',
    long_description = 'A script for easily downloading books from Library Genesis.',
    version = '0.1.1',
    author = "Andrew Secco",
    author_email = "<asecco99@gmail.com>",
    packages = find_packages(),
    install_requires = ['libgen-api'],
    keywords = ['python', 'downloader', 'library genesis', 'textbooks'],
)