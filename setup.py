import setuptools

with open("README.md", "r", encoding='utf-8') as f:
    long_desc = f.read()

setuptools.setup(
    name="google-trans-new",
    version="0.2",
    author="lushan88a",
    description="google_trans_new",
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url="https://github.com/lushan88a/google_trans_new",
    packages=setuptools.find_packages(),
    install_requires=["urllib3", "requests"],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
