from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="void-miner",
    version="0.1.0",
    author="The Void Miner Team",
    description="The Void Miner - A space mining adventure game",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hartensteindominic/The-Void-Miner",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Games/Entertainment",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pygame>=2.5.0",
    ],
    entry_points={
        "console_scripts": [
            "void-miner=void_miner.__main__:main",
        ],
    },
)
