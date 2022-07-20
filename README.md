Spark UDFs
========

Often PySpark users need to create **user defined functions** (UDFs) to transform data. Implementing UDFs in PySpark can be done in either Python or Scala.

For a good discussion on performance of each approach, see [this article](https://medium.com/wbaa/using-scala-udfs-in-pyspark-b70033dd69b9).

In this repo we show how UDFs written in Python and Scala can be used in a PySpark program.

## Requirements

To run this project the following are needed:
- Python 3.8 and `venv`
- Java 8 SDK

## Basic setup

At the root the project there is the main setup script `setup.sh`. This script will:
- Setup the Python project under the `python` directory.
   - A new virtual environment will be created under `pyenv` where all Python dependencies will be installed.
- Build the Scala project artifacts under the `scala` directory.

### Manually building Scala UDF

The Scala artifacts can be manually built in a command shell, by typing the following in the `scala` directory:

```bash
$ sbt clean assembly
```

This will create the Scala artifact in `scala/target/scala-2.12/spark-udf-assembly-0.1.0.jar`. This is the artifact the PySpark project will pick up.

## Running the PySpark example in the interactive console

1. Open a command line window at the project root and go to the `python` directory using `cd python`.
2. Activate the virtual environment using `source ./pyenv/bin/activate`
3. Open an interactive Python console by typing `ipython`
4. Load files into the interactive console with the `%load` command. For example:
   ```python
   In [1]: %load main.py
   ```
   This should load the contents of the `main.py` file into the interactive console.

## The UDFs

Both Python and Scala UDFs calculate the word and character count of the supplied text. These can be found under the `python/text_stats` and under the `scala/src/` directories, respectively.
