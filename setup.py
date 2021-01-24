from setuptools import setup, find_packages


setup(
    name="underline",
    version="1.0.3",
    description="A human friendly web crawling library",
    py_module=["underline"],
    license="MIT",
    keywords="web,spider,crawler",
    packages=find_packages(),
    install_requires=[
        "bs4>=0.0.1",
        "requests>=2.24.0"
    ],
    extras_require={
        "dev": [
            "pytest>=3.7",
            "check-manifest>=0.43",
            "twine>=3.2.0"
        ]
    },

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
    ],

    url="https://github.com/anyms/underline",
    author="Jeeva",
    author_email="mytellee@gmail.com"
)


# pip install -e .
# python setup.py sdist
# twine.exe upload --repository-url=https://upload.pypi.org/legacy/ dist/*
