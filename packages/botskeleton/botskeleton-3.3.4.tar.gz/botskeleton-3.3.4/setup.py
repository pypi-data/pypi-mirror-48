"""setup.py for botskeleton"""
from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

INSTALL_REQUIRES = [
    "clint>=0.5.1, <0.6.0",
    "drewtilities>=1.3.2, <2.0.0",
    "tweepy>=3.7, <4.0",
    "Mastodon.py>=1.4.2, <2.0",
]

TESTS_REQUIRE = [
    "coveralls>=1.7.0, <2.0.0",
    "pytest>=4.5.0, <5.0.0",
]

SETUP_REQUIRES = [
    "pytest-runner",
]

with open(path.join(HERE, "README.rst")) as f:
    LONG_DESCRIPTION = f.read().strip()

with open(path.join(HERE, "VERSION"), encoding="utf-8") as f:
    VERSION = f.read().strip()

setup(author="Andrew Michaud",
      author_email="bots@mail.andrewmichaud.com",

      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Environment :: Console",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: BSD License",
          "Natural Language :: English",
          "Operating System :: MacOS :: MacOS X",
          "Operating System :: POSIX :: Linux",
          "Operating System :: POSIX :: BSD :: FreeBSD",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Programming Language :: Python :: 3 :: Only",
          "Programming Language :: Python :: Implementation :: CPython",
          "Topic :: Software Development :: Libraries",
          "Typing :: Typed",
      ],

      entry_points={},

      install_requires=INSTALL_REQUIRES,
      python_requires=">=3.6",
      setup_requires=SETUP_REQUIRES,
      tests_require=TESTS_REQUIRE,

      license="BSD3",

      name="botskeleton",

      packages=find_packages(),

      description="A skeleton for content bots.",
      long_description=LONG_DESCRIPTION,

      url="https://github.com/alixnovosi/bot_skeleton",

      version=VERSION)
