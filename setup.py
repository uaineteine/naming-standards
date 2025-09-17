from setuptools import setup, find_packages

requirements = []
long_description = '# Naming Standards\n\nA validation package for database table and column names, providing standardized classes for validating and managing table names, column headers, and variable lists.\n\n## Features\n\n- **Tablename**: Validates database table identifiers according to naming conventions\n- **Colname**: Validates column/header names with lowercase enforcement  \n- **NamedList**: A list with enforced lowercase and utility methods for name management\n- **ColList**: A validated list for variable names that conform to header naming conventions\n\n## Installation\n\n```bash\npip install naming_standards.tar.gz\n```\n\n## Usage\n\n### Table Names\n\n```python\nfrom transforms_names import Tablename\n\n# Valid table names\ntable1 = Tablename("my_table")        # Standard format\ntable2 = Tablename("_private_table")  # Starting with underscore\ntable3 = Tablename("123")             # Purely numeric\ntable4 = Tablename("table123")        # Mixed alphanumeric\n```\n\n### Column Names\n\n```python\nfrom transforms_names import Colname\n\n# Valid column names (automatically lowercased)\ncol1 = Colname("customer_name")  # Valid\ncol2 = Colname("order_123")      # Valid\ncol3 = Colname("CustomerName")   # Becomes "customername"\n```\n\n### Lists\n\n```python\nfrom transforms_names import ColList, NamedList\n\n# Basic named list\nnames = NamedList(["CustomerID", "OrderNumber"])  # Becomes ["customerid", "ordernumber"]\n\n# Validated column list\ncolumns = ColList(["customerid", "ordernumber", "amount123"])\n```\n\n## Version\n\n1.0.0'

setup(
    name="naming_standards",
    version="1.0.0",
    author="",
    author_email="",
    description="A python package of a working transforms framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    packages=find_packages(include=["naming_standards", "naming_standards.*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=requirements
)
