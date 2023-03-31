import sys
import os
import setuptools
from distutils import sysconfig

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


README = "README.rst"
CHANGELOG = "CHANGELOG.rst"
LICENSE = "LICENSE.rst"


def version():
    with open(os.path.join(__location__, CHANGELOG), encoding="utf_8") as changelog_file:
        for line in changelog_file.readlines():
            if line.startswith("Version "):
                return line[len("Version "):]
    raise Exception("no valid version in " + CHANGELOG)


def long_description():
    with open(os.path.join(__location__, README), encoding="utf_8") as readme_file:
        readme_str = readme_file.read()
    with open(os.path.join(__location__, CHANGELOG), encoding="utf_8") as changelog_file:
        changelog_str = changelog_file.read()
    return readme_str + "\nHistory\n=======\n\n" + changelog_str


cxx = sysconfig.get_config_var('CXX')
if cxx and 'g++' in cxx:
    # Avoid warning about invalid flag for C++
    for varname in ('CFLAGS', 'OPT'):
        value = sysconfig.get_config_var(varname)
        if value and '-Wstrict-prototypes' in value:
            value = value.replace('-Wstrict-prototypes', '')
            sysconfig.get_config_vars()[varname] = value


if __name__ == "__main__":
    setuptools.setup(
        name="memoize",
        version=version(),
        description="A python library for automatic fonctions caching.",
        long_description=long_description(),
        # "text/markdown " si la long_description est au format markdown et pas restructuredText
        long_description_content_type="text/x-rst",
        url="https://github.com/SmartAudioTools/memoize",
        download_url="https://github.com/SmartAudioTools/memoize/tarball/master",
        license="Prosperity Public License 3.0.0 and Patron License 1.0.0",
        keywords="fonctions caching memoization",
        packages=setuptools.find_packages(exclude=("tests",)),
        python_requires=">=3",
        install_requires=[
        ],
        extras_require={
            "dev": [
                "pytest"
            ],
            "test": [
                "pytest"
            ],
        },
        include_package_data=True,
        project_urls={
            "Documentation": "https://smartaudiotools.github.io/memoize",
            "Funding": "https://github.com/sponsors/SmartAudioTools",
            "Source": "https://github.com/SmartAudioTools/memoize",
            "Tracker": "https://github.com/SmartAudioTools/memoize/issues",
        },
        classifiers=[
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Developers",
            "License :: Free for non-commercial use",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: 3.9",
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
        ],
        zip_safe=False,
        data_files=[("", [LICENSE, CHANGELOG, "pyproject.toml"])]
    )
