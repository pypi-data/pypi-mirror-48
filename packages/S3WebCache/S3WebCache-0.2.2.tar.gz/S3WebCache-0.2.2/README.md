[![Build Status](https://travis-ci.org/wharton/S3WebCache.svg?branch=master)](https://travis-ci.org/wharton/S3WebCache)
[![PyPI version](https://badge.fury.io/py/S3WebCache.svg)](https://badge.fury.io/py/S3WebCache)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# S3 Web Cache

This is a simple package for archiving web pages (HTML) to S3. It acts as a cache returning the S3 version of the page if it exists. If not it gets the url through [Requests](http://docs.python-requests.org/en/master/) and archives it in s3.

Our use case: provide a reusable history of pages included in a web scrape. An archived version of a particular URL at a moment in time. Since the web is always changing, different research questions can be asked at a later date, without losing the original content. Please only use in this manner if you have obtained permission for the pages you are requesting.


## Quickstart


### Install

`pip install s3webcache`


### Usage

```
from s3webcache import S3WebCache

s3wc = S3WebCache(
    bucket_name=<BUCKET>,
    aws_access_key_id=<AWS_ACCESS_KEY_ID>,
    aws_secret_key=<AWS_SECRET_ACCESS_KEY>,
    aws_default_region=<AWS_DEFAULT_REGION>)

request = s3wc.get("https://en.wikipedia.org/wiki/Whole_Earth_Catalog")

if request.success:
    html = request.message
```

If the required AWS credentials are not given it will fallback to using environment variables.

The `.get(url)` operation returns a namedtuple Request: (success: bool, message: str).

For successful operations, `.message` contains the url data.
For unsuccessful operations, `.message` contains error information.


### Options

S3WebCache() takes the following arguments with these defaults:
 - bucket_name: str
 - path_prefix: str = None\
    Subdirectories to store URLs. `path_prefix='ht'` will start archiving at path s3://BUCKETNAME/ht/
 - aws_access_key_id: str = None 
 - aws_secret_key: str = None
 - aws_default_region: str = None 
 - trim_website: bool = False
    Trim out the hostname. Defaults to storing the hostname as dot replaced underscores. `https://github.com/wharton/S3WebCache` would be `s3://BUCKETNAME/github_com/wharton/S3WebCache`.\
    Set this to true and it will be stored as `s3://BUCKETNAME/wharton/S3WebCache`.
 - allow_forwarding: bool = True
    Will follow HTTP 300 class redirects.


## TODO

 - Add 'update s3 if file is older than...' behavior
 - Add transparent compression by default (gzip, lz4, etc)
 - Add rate limiting


## Reference

[AWS S3 API documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html) 


## License

MIT


## Tests

Through Travis-ci