import setuptools
from google_trans_new import __version__

with open("README.md", "r", encoding='utf-8') as f:
    long_desc = f.read()


def _requires_from_file(filename):
    return open(filename, encoding="utf8").read().splitlines()


setuptools.setup(
    name="google-trans-new",
    version=__version__,
    author="lushan88a",
    description="google_trans_new",
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url="https://github.com/lushan88a/google_trans_new",
    packages=setuptools.find_packages(),
    install_requires=_requires_from_file('requirements.txt'),
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
