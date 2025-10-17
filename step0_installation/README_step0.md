# Step 0 - Python Installation and Environment Setup

## Project Path
D:\Waqas\Python\projects\scrap_analytics

## Purpose
To create and verify a clean Python environment for future data analytics work.

---

## 1. Python Installation
- Installed Python 3.11.9 from the official website: https://www.python.org/downloads/windows/  
- During setup:
  - Checked “Add Python to PATH”
  - Selected “Customize Installation”
  - Installation directory: D:\Waqas\Python

---

## 2. Version Verification
Commands used:
python --version
pip --version

Output:
Python 3.11.9
pip 24.0

---

## 3. Project Folder Structure
D:\Waqas\Python\projects\scrap_analytics
│
├───step0_installation
├───step1_data_collection
├───step2_cleaning
├───step3_analysis
├───step4_dashboard
└───step5_automation

---

## 4. Virtual Environment Setup
Commands used:
cd D:\Waqas\Python\projects\scrap_analytics
python -m venv env
env\Scripts\activate

Prompt after activation:
(env) PS D:\Waqas\Python\projects\scrap_analytics>

---

## 5. Library Installation
Commands used:
pip install --upgrade pip
pip install pandas numpy openpyxl matplotlib seaborn jupyterlab yagmail

---

## 6. Environment Verification
File created:
(env) PS D:\Waqas\Python\projects\scrap_analytics\step0_installation> notepad test_setup.py
D:\Waqas\Python\projects\scrap_analytics\step0_installation\test_setup.py

Write below code in above created file named as test_setup.py:
import sys
import pandas as pd
import numpy as np
import matplotlib
import seaborn
import yagmail

print("Setup Complete!")
print("Python version:", sys.version)
print("Pandas version:", pd.__version__)
print("NumPy version:", np.__version__)
print("Matplotlib version:", matplotlib.__version__)
print("Seaborn version:", seaborn.__version__)
Command:
python test_setup.py
Output:

yaml
Copy code
Setup Complete!
Python version: 3.11.9
Pandas version: 2.3.3
NumPy version: 2.3.4
Matplotlib version: 3.10.7
Seaborn version: 0.13.2
7. Result
The Python setup was completed successfully.
All libraries were installed and verified through a test script.
Environment is ready for Step 1 – Data Collection.

8. System Information
Date Completed: 17 October 2025

Operating System: Windows 10

Processor: Core i5

Python Version: 3.11.9

Folder Path: D:\Waqas\Python\projects\scrap_analytics