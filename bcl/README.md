# BCL
This folder contains the main scripts used in the BCL project. Each script is essential for the conversion of battery cycling data into different formats, supporting the project's overall goal of standardizing and linking battery data. Below, you will find descriptions of the main scripts and their purposes.

Scripts
1. convertToPybamm.py
Description: This script converts JSON data following the BCL structure into a format compatible with PyBaMM (Python Battery Mathematical Modeling). PyBaMM is a battery simulation package used to model and simulate battery behaviors and characteristics.
Functionality:
Parses the input JSON data to extract relevant battery parameters and cycling instructions.
Maps these parameters and instructions into a structure that can be utilized by PyBaMM for simulations.
Usage:
See usage in the TestNotebook provided

2. convertToJsonld.py
Description: This script converts JSON data into JSON-LD (JSON for Linked Data) format. JSON-LD is a method of encoding linked data using JSON, which enhances the interoperability and discoverability of the data across different platforms.
Functionality:
Transforms BCL structured JSON into JSON-LD, embedding context and linking information to standard vocabularies such as EMMO (Elementary Multiperspective Material Ontology).
Ensures that all relevant battery parameters, cycling instructions, and metadata are accurately represented in the JSON-LD format.
Usage:
See usage in the TestNotebook provided