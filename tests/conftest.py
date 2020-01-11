import sys
from time import sleep
from uuid import uuid4

import pytest

import mhs5200


def pytest_addoption(parser):
    parser.addoption(
        "--port", action="store", default="", help="Serial port of MHS-5200 device.",
    )


@pytest.fixture(scope="session")
def port(request):
    cfg_port = request.config.getoption("--port")
    if len(cfg_port) == 0:
        if sys.platform == "win32":
            cfg_port = "COM12"
        else:
            cfg_port = "/dev/ttyUSB0"
    return cfg_port


@pytest.fixture(scope="session")
def uuid():
    return uuid4()


@pytest.fixture(scope="session")
def signal_generator(port):
    sg = mhs5200.MHS5200(port)
    sg.on()
    yield sg
    sg.off()
    # Close the serial port.
    sg.serial.close()
    sleep(0.5)

@pytest.fixture(scope="function")
def chan1(signal_generator):
    yield signal_generator.channels[0]
    
@pytest.fixture(scope="function")
def chan2(signal_generator):
    yield signal_generator.channels[1]
