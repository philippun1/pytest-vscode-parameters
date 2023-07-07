import test_example

def pytest_addoption(parser):
    parser.addoption(
        "--test_option",
        default=""
    )

def pytest_configure(config):
    test = config.getoption("--test_option")
    test_example.TEST = test
