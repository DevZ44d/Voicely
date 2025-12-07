import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    lng_description = fh.read()

setuptools.setup(
    name="voicely",
    version="3.0.0",
    author="AhMed",
    author_email="asyncpy@proton.me",
    license="MIT",
    description="Voicely is a lightweight Python library that converts audio files → text and optionally translates the extracted text ",
    long_description=lng_description,
    long_description_content_type="text/markdown",
    python_requires=">=3.6",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
