from setuptools import setup, find_packages

setup(
    name="CVEhunter",
    version="1.0.0",
    description="A tool to hunt for CVEs in domains and IP addresses.",
    author="huntersh7",
    author_email="cs6267231@gmail.com",
    packages=find_packages(),
    install_requires=[
        "requests>=2.31.0",
        "rich>=13.4.2",
        "beautifulsoup4>=4.12.0",
    ],
    entry_points={
        "console_scripts": [
            "cvehunter=cvehunter.cvehunter:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)