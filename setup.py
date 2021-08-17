import setuptools

with open("README.md" , "r") as f:
    long_description = f.read()

setuptools.setup(
      name="pysudo",
      version="1.1.0",
      author="Yash Indane",
      author_email="yashindane46@gmail.com",
      description="libray for solving standard Sudoku",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/YashIndane/pysudo",
      packages=setuptools.find_packages(),
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
      ],
      python_requires='>=3.6',
)
