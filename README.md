# Topology-Informed Machine Learning for Efficient Prediction of Solid Oxide Fuel Cell Electrode Polarization

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/Python-3.10+-brightgreen.svg)

## Overview
This repository contains the code accompanying the paper **[Topology-Informed Machine Learning for Efficient Prediction of Solid Oxide Fuel Cell Electrode Polarization](https://arxiv.org/abs/2410.05307)** by Maksym Szemer, Szymon Buchaniec, Marcin Prokop and Grzegorz Brus.

## Table of Contents

- [Installation](#Installation)
- [Structure](#Structure)
- [Data](#Data)
- [Usage](#Usage)
- [Results](#Results)
- [Citations](#Citations)
- [License](#License)

## Structure
The project is organized into the following directories and files:
```bash
├── README.md                                   	# Project description and usage instructions
├── LICENSE                                     	# License information
├── computing                                   	# Support code for generating Persistence Images accelerated with numba
│   ├── __init__.py                             	# Initializes the package and manages imports
│   ├── core.py                                 	# Calculating Persistence Surfaces and discretizing
│   ├── integrate.py                            	# Transforming (birth, death) pairs 
│   └── transformations.py                      	# Integration using Gauss-Legendre quadrature
├── data                                        	# Folder containing the data needed to reproduce the main results
│   ├── 3d_neumann                              	# Overpotential values ​​obtained from the numerical model
│   ├── pi                                      	# Main Persistence Image frames needed to generate figures
│   └── results                                 	# Results from research published in article
├── data preprocessing                          	# Scripts for cleaning, transforming, and preparing data
│   ├── making_frames.py                        	# Code for generating pandas frames
│   ├── pd                                      	# Code for generating Persistence Diagrams
│   └── pi                                      	# Code for generating Persistence Images
├── latex_utils                                 	# Scripts to generate latex fragments
├── notebooks                                   	# Jupyter notebooks for training models
│   └── train-models.ipynb                      	# Notebook for model testing and analysis (during research different variations of this notebook were used)
├── plotting                                    	# Scripts to generate figures published in article
└── requirements.txt                            	# List of required Python packages
```

## Installation
To get started, clone this repository and install the required dependencies.

### Clone the Repository
```bash
git clone https://github.com/MaksymSz/Computational-Materials-publication.git
cd Computational-Materials-publication
```
### Dependencies
Install the required packages using pip:
```bash
pip install -r requirements.txt
```

## Data
Data can be obtained from public [repository](https://zenodo.org/records/13731825?preview=1&token=eyJhbGciOiJIUzUxMiJ9.eyJpZCI6IjgwMjQyN2FhLWU4YzAtNDk1NC1hNWE2LTg5MDZkNjdhNDNlMyIsImRhdGEiOnt9LCJyYW5kb20iOiJiZDJjMzUzODVhZDk4YjY2MDBjZjVjZDc1MjY2MjhkMiJ9.vEgZumvoNH0xjqzOqMXGlsusDVk6ykHAnw8Va9lksPHJJUHa6CDh3v-fryuZZohYoO5Ku8AWiXcGfmn13MJ7xg).


## Citations
If you use this code in your research, please cite our paper as follows:
```bib
@article{Name2024,
  title={Topology-Informed Machine Learning for Efficient Prediction of Solid Oxide Fuel Cell Electrode Polarization},
  author={Szemer, Maksym and Buchaniec, Szymon and Prokop, Tomasz and Brus, Grzegorz},
  journal={Journal name},
  volume={XX},
  number={X},
  pages={XX-XX},
  year={2024},
  publisher={Publisher Name}
}
```

## Contact
Corresponding author e-mail: brus@agh.edu.pl

## License
This project is licensed under the MIT License.


