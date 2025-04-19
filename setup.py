from setuptools import setup, find_packages

setup(
    name="pyrtk-cli",
    version="0.1.3",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "typer>=0.9.0",
        "rich>=13.0.0",
        "fastapi",
        "uvicorn",
        "python-dotenv"
    ],
    extras_require={
        "dev": [
            "pytest",
            "setuptools",
            "wheel"
        ]
    },
    entry_points={
        "console_scripts": [
            "pyrtk=pyrtk.main:main",
        ],
    },
    author="Andres Mardones",
    description="Python REST Toolkit CLI",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)