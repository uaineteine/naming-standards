
# Naming Standards

A validation package for database table and column names, providing standardized classes for validating and managing table names, column headers, and variable lists.

## Table of Contents

- [Installation](#installation)
- [Features](#features)
- [Usage](#usage)
	- [Table Names](#table-names)
	- [Column Names](#column-names)
	- [NamedList](#namedlist)
	- [ColList](#collist)
- [Documentation Build Process](#documentation-build-process)
- [Version](#version)


## Installation

```bash
pip install naming_standards
```

## Features

- **Tablename**: Validates and standardises table names according to database naming conventions
- **Colname**: Validates column/header names with strict formatting rules (lowercase, underscores allowed)
- **NamedList**: A list with enforced lowercase and utility methods for name management
- **ColList**: A validated list for variable names that conform to header naming conventions

## Usage

### Table Names

```python
from naming_standards import Tablename

# Valid table names
valid_names = [
	Tablename("my_table"),        # Standard format
	Tablename("_private_table"),  # Starting with underscore
	Tablename("123"),             # Purely numeric
	Tablename("table123"),        # Mixed alphanumeric
	Tablename("CustomerData"),    # CamelCase
]

# Invalid table names (will raise ValueError)
try:
	Tablename("1table")          # Cannot start with digit
except ValueError as e:
	print(e)

try:
	Tablename("table-name")      # No hyphens allowed
except ValueError as e:
	print(e)

try:
	Tablename("")                # Cannot be empty
except ValueError as e:
	print(e)
```

### Column Names

```python
from naming_standards import Colname

# Valid header names
valid_headers = [
	Colname("customername"),   # All lowercase letters
	Colname("order123"),       # Letters and numbers
	Colname("customer_name"),  # Underscored column name
	Colname("CUSTOMERNAME"),   # Automatically converted to customername
	Colname("ORDER123"),       # Automatically converted to order123
]

# Invalid header names (will raise ValueError)
try:
	Colname("customer name")   # No spaces
except ValueError as e:
	print(e)

try:
	Colname("order-date")      # No hyphens
except ValueError as e:
	print(e)

try:
	Colname("")                # Cannot be empty
except ValueError as e:
	print(e)
```

### NamedList

```python
from naming_standards import NamedList

# Create a named list
var_list = NamedList(["name", "age", "city"])
print(var_list)  # NamedList(['name', 'age', 'city'])

# Properties and methods
print(f"Count: {var_list.count}")  # Count: 3
print(var_list.to_json())  # JSON representation

# Set operations
other_list = ["age", "salary", "department"]
overlap = var_list.overlap(other_list)
print(overlap)  # NamedList(['age'])

# Extend with unique values
var_list.extend_with(other_list)
print(var_list)  # NamedList(['name', 'age', 'city', 'salary', 'department'])
```

### ColList

```python
from naming_standards import ColList

# Valid variable list
valid_vars = ColList(["customerid", "ordernumber", "amount123"])
print(valid_vars)  # ColList(['customerid', 'ordernumber', 'amount123'])

# Invalid variable list (will raise ValueError)
try:
	invalid_vars = ColList(["customer id", "order-number", "amount@"])
except ValueError as e:
	print(e)  # Column names must be in correct format

# All NamedList methods are available
print(valid_vars.to_json())
other_vars = ["productid", "customerid"]
overlap = valid_vars.overlap(other_vars)
print(overlap)  # ColList(['customerid'])
```


## Documentation Build Process

See [docs/docsbuild.md](docs/docsbuild.md) for details on building the documentation with Sphinx, including pre-compilation, auto-modules, meta files, and the build process.

## Version

1.0.0