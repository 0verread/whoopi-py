from setuptools import setup
from os.path import abspath, dirname, join

README = open(join(dirname(abspath(__file__)), "README.md")).read()

setup(
  name="whoopi",
  version="1.0.0",
  description="Whoopi python SDK",
  long_description=README,
  long_description_content_type="text/markdown",
  packages=["whoopi"],
  url="https://github.com/0verread/whoopi-py",
  author="Subhajit Das",
  author_email="iamsubhajit.d@gmail.com",
  license="MIT",
  python_requires='>=3.6',
  install_requires=["requests"],

)
