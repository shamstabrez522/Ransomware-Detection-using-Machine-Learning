# Ransomware-Detection-using-Machine-Learning
# MLRD Machine Learning Ransomware Detection
MLRD is a machine learning based malware analyser written in Python 3 that can be used to detect ransomware.


## Features:
* Analyses and Extracts features from PE file headers to determine if a file is malicious or not.
* Features include: Debug Size, Debug RVA, Major Image Version, Major OS Version, Export Size, IAT RVA, Major Linker Version, Minor Linker Version, Number Of Sections, Size Of Stack Reserve, Dll Characteristics, and Bitcoin Addresses.
* Checks if a file contains a Bitcoin Address using YARA rules.
* Correlate results with Virus Total, Threat Crowd, and Hybrid Analysis.

## Install:
```
git clone https://

cd MLRD-Machine-Learning-Ransomware-Detection

sudo pip3 install -r requirements.txt
```
## Usage

### Train model:
```
python3 mlrd_learn.py
```

### Basic Usage:
```
python3 mlrd.py 'FILE TO ANALYSE'
```
```
### Display Extracted Features for Input File:
```
python3 mlrd.py 'FILE TO ANALYSE'
```
```
### Display Help Information:
```
python3 mlrd.py/'Test Data'
```

## Test Data:
* Malicious and Benign test files for use with the program can be found in the Test Data directory.
* In this directory you will find benign windows PE files and you can download ransomware files within a ZIP file from following website.
For MAlICIOUS FILE DOWNLOADING : https://docs.paloaltonetworks.com/wildfire/8-1/wildfire-admin/submit-files-for-wildfire-analysis/verify-wildfire-submissions/test-a-sample-malware-file

## WARNING:
* Malicious programs are contained within this directory and thus, should be handled with care.
* The ransomware distributed inside the test virual machine have been gathered for research purposes and are only for use within the scope of this project.
* Using these programs with malicious intent is strictly prohibited. 
