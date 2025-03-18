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
@article{SZEMER2025100495,
title = {Topology-informed machine learning for efficient prediction of solid oxide fuel cell electrode polarization},
journal = {Energy and AI},
pages = {100495},
year = {2025},
issn = {2666-5468},
doi = {https://doi.org/10.1016/j.egyai.2025.100495},
url = {https://www.sciencedirect.com/science/article/pii/S2666546825000278},
author = {Maksym Szemer and Szymon Buchaniec and Tomasz Prokop and Grzegorz Brus},
keywords = {Fuel cell, Microstructure, Artificial neural networks, Persistent homology, Persistent diagrams, Machine learning, Computational topology},
abstract = {Machine learning has emerged as a potent computational tool for expediting research and development in solid oxide fuel cell electrodes. The effective application of machine learning for performance prediction requires transforming electrode microstructure into a format compatible with artificial neural networks. Input data may range from a comprehensive digital material representation of the electrode to a selected set of microstructural parameters. The chosen representation significantly influences the performance and results of the network. Here, we show a novel approach utilizing persistence representation derived from computational topology. Using 500 microstructures and current–voltage characteristics obtained with three-dimensional first-principles simulations, we have prepared an artificial neural network model that can replicate current–voltage characteristics of unseen microstructures based on their persistent image representation. The artificial neural network can accurately predict the polarization curve of solid oxide fuel cell electrodes. The presented method incorporates complex microstructural information from the digital material representation while requiring substantially less computational resources (preprocessing and prediction time ≈1min) compared to our high-fidelity simulations (simulation time ≈1h) to obtain a single current-potential characteristic for one microstructure.}
}
```

## Contact
Corresponding author e-mail: brus@agh.edu.pl

## License
This project is licensed under the MIT License.


