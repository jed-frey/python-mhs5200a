from setuptools import setup

import versioneer

setup(
    name="mhs5200",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    description="Python module for controlling inexpensive MHS-5200 signal generators.",
    url="https://github.com/jed-frey/python_mhs5200",
    author="Frey, Jed",
    license="BSD",
    packages=["mhs5200"],
    install_requires=["pyserial", "cached_property"],
    tests_require=["pytest", "pytest-html", "pytest-csv"],
    zip_safe=False,
    python_requires=">=3.6",
)
