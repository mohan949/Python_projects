
import pytest

# a = 4
# b = 1
@pytest.fixture(params=["a","b"])
def sample_data(request):
    print(f"Fixture param: {request.param}")
    return request.param


def testLogOff(sample_data):
    print('logOff Succesfull')

