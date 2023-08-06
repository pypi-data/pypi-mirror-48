from distutils.core import setup

from setuptools import find_packages

with open("README.md", "rt", encoding="utf8") as f:
    long_description = f.read()

version = ".".join(map(str, __import__("lj").__VERSION__))

setup(name="LocalJudge",
      version=version,
      description="LocalJudge",
      long_description=long_description,
      long_description_content_type="text/markdown",
      author="NoCLin",
      author_email="engineelin@gmail.com",
      url="https://github.com/NoCLin/LocalJudge",
      license="MIT Licence",
      install_requires=[
          'colorful>=0.5.0',
      ],
      packages=find_packages(),
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'lj = lj.lj:main',
              'ljc = lj.ljc:main',
          ]},
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      )
