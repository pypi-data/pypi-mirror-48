from setuptools import setup, find_packages
import os

f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
readme = f.read()
f.close()

setup(
    name='py-roku',
    version='1.1',
    description='Client for the Roku media player',
    long_description=readme,
    author='Villhellm',
    author_email='will@villhellm.com',
    url='https://github.com/villhellm/python-roku',
    packages=find_packages(),
    install_requires=[
        'lxml>=3.6,<3.7',
        'requests>=2.10,<2.11',
        'six'
    ],
    license='BSD License',
    platforms=["any"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
)
