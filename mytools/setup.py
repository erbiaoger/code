from setuptools import setup

setup(name="mytools",
      version='0.1',
      description='some tools made by erbiaoger',
      url='https://github.com/erbiaoger/code/mytools',
      author='erbiaoger',
      author_email='erbiaoger@gmail.com',
      packages=["mytools"],
      zip_safe=False,
      install_requires=[
          "numpy",
          "pandas"
          ],
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          ],
      )
