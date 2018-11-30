import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="salesforce_id",
    version="0.0.1",
    author="James Sullivan",
    author_email="bobx11@gmail.com",
    description="Simplify working with Salesforce.com IDs",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jsullivanlive/salesforce_id",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL3 License",
        "Operating System :: OS Independent",
    ],
)