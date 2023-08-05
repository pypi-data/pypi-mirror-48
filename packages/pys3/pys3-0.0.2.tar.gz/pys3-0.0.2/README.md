# PyS3

Minimal wrapper for S3 functionality in `boto3`.

## Installation

```python
pip install pys3
```

## Example

```python
from pys3 import PyS3

# Local file
file = PyS3('/path/to/file.txt', 'w')
file.write('Hello World!')
file.close()

# File on S3
file = PyS3('s3://bucket_name/path/to/file.txt', 'w')
file.write('Hello World!')
file.close()
```

## Prerequisites

`pys3` uses `boto3` as a back-end. Thus, credentials for AWS must be set up according to that framework. For example, place the acces key ID and secret key in the `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY`.

## How it works

Upon creation of a `PyS3` file object, it is checked whether the passed file URL refers to a location on S3. If so, a local copy of the file is downloaded (provided it exists). When the `close()` method is called, any modifications to the local file are uploaded.
