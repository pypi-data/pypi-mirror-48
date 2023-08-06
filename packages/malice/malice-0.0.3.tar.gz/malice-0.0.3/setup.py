import setuptools

from malice.malice import __version__, __author__, __email__, __license__

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="malice",
    version=__version__,
    author=__author__,
    author_email=__email__,
    description="My awesome little infrastructure configuration environment",
    license=__license__,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SamuelDeal/malice",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": ["malice = malice:main"]
    },
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Natural Language :: English",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        # "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Software Development",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Clustering",
        "Topic :: System :: Software Distribution",
        "Topic :: System :: Systems Administration",
    ]
)
