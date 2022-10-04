import os
from setuptools import setup, find_packages

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))


# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

setup(name='wotreplay',
      version='1.0.0',
      description='World of Tanks PC replay data extractor',
      author='Gabriel Oana',
      author_email='gabriel.oana91@gmail.com',
      license='MIT',
      url='https://gitlab.com/gabriel_oana/worldoftanks',
      zip_safe=False,
      long_description=README,
      long_description_content_type="text/markdown",
      packages=find_packages(),
      install_requires=[
            'sqlalchemy',
            'tqdm'
      ],
      classifiers=[
            "Development Status :: 5 - Production/Stable",
            "Programming Language :: Python :: 3",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            'Topic :: Software Development :: Libraries :: Python Modules',
            'Typing :: Typed',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
      ]
      )
