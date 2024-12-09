# parquet_tools

## Overview
`parquet_tools` is a command-line utility for working with Apache Parquet files.
This tool simplifies data inspection and conversion for Parquet files.

## Features
`parquet_tools` offers three main commands:
1. **show**: Displays Parquet file contents in a human-readable format.
2. **csv**: Outputs data in CSV format.
3. **inspect**: Provides a summary inspection of the Parquet file's structure and metadata.


## Installation
To use `parquet_tools`, I recommend creating a dedicated conda or mamba environment for easier dependency management. Follow these steps:

### Step 1: Create and Activate the Environment
Using `conda`:
```bash
conda create -n parquet_env pip
conda activate parquet_env
```

Or, using `mamba` (recommended for faster environment setup):
```bash
mamba create -n parquet_env pip
mamba activate parquet_env
```

### Step 2: Install Packages
With the environment activated, install `parquet_tools` and `csvq`:
```bash
conda install parquet-tools csvq
```

### Step 3: Verify Installation
After activation, verify that parquet_tools and csvq are installed correctly:
```bash
parquet-tools --help
csvq --help
```

## Useful Links
- [parquet_tools](https://github.com/ktrueda/parquet-tools): CLI tools for working with Parquet files.
- [Apache Arrow](https://github.com/apache/arrow): CLI tools for columnar data processing.
- [csvq](https://github.com/mithrandie/csvq): SQL-like query language for CSV files.
