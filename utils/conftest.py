# tests/conftest.py
import sys
import os

services_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'services'))
print(f"Adding {services_path} to sys.path")
sys.path.insert(0, services_path)
