from setuptools import setup

setup(name="gitterpy",
      version="0.1",
      description="A Gitter client API in Python",
      long_description=open("README.md").read(),
      author="Alex Hiam",
      author_email="alex@graycat.io",
      license="MIT License",
      url="https://github.com/graycatlabs/gitterpy",
      keywords=["gitter"],
      packages=["gitterpy"],
      install_requires=["requests"],
      )