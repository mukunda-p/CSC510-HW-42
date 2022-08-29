from setuptools import setup,find_packages


setup(
    name="Math Functions",
    version="1.0",
    author="CSC510-Software Engineering HomeWork Group 42, Kalyan Karnati, Mukunda Varma Pericherla, Pranavi Sharma Sanganabhatla, Saketh Vangala, Srihitha Reddy Kaalam",
    packages=find_packages()
    description='Home work',
    author_email="mperich@ncsu.edu",
    packages=find_packages(),
    tests_require=['pytest'],
      classifiers=[
          "License :: OSI Approved :: MIT License",
          "Programming Language :: Python",
      ],
    license='MIT',
    install_requires=['python', 'pytest'],
)
