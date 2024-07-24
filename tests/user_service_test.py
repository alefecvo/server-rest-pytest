import sys
import os
import pytest

services_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'services'))
print(f"Adding {services_path} to sys.path")
sys.path.insert(0, services_path)

from user_service import generate_fake_user, send_create_user_request, validate_user_creation

@pytest.fixture(scope="session")
def base_url():
    return "https://serverest.dev"

def test_create_user(base_url):
    new_user = generate_fake_user()
    response = send_create_user_request(base_url, new_user)
    validate_user_creation(response)