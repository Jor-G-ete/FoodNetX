from setuptools import setup

version = "0.1"

with open("README.md", "r") as rmd:
      long_description = rmd.read()

setup(
      name="FoodNetX",
      packages=['FoodNetX'],
      version=version,
      license="GNU General Public License v3.0",
      description="Library to create databases using graphs from networkx. Covers the challenge of Foodvisor",
      author="Jorge Lopez Marcos",
      author_email="jlomar2005@hotmail.com",
      maintainer="Jorge Lopez Marcos",
      maintainer_email="jlomar2005@hotmail.com",
      url="https://github.com/Jor-G-ete/FoodNetX",
      download_url="https://github.com/Jor-G-ete/FoodNetX/archive/v"+version+".tar.gz",
      project_urls={
           "Documentation":"https://github.com/Jor-G-ete/FoodNetX",
           "Source Code":"https://github.com/Jor-G-ete/FoodNetX/blob/master/FoodNetX/database.py"
      },
      platforms="Windows",
      keywords=["python3.7", "NeuroSky", "Graphs", "Trees"],
      long_description=long_description,
      long_description_content_type='text/markdown',
      install_requires=[
            'networkx',
            'matplotlib'
      ],
      classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',  # Define that your audience are developers
            'Topic :: Software Development :: Build Tools',
            "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
            'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
            'Programming Language :: Python :: 3.7',
            "Natural Language :: English",
            "Natural Language :: Spanish",
            "Operating System :: Microsoft :: Windows :: Windows 10",
            "Topic :: Scientific/Engineering :: Medical Science Apps."
            ],
      python_requires=">=3.7",
      )