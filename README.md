# Bert Simple


Introduction to `bert-etl` with the least amount of code possible

## Install

```
$ git clone git@github.com:jbcurtin/bert-simple.git
$ cd bert-simple
$ virtualenv -p $(which python3) env
$ source env/bin/activate
$ pip install bert-etl
```

## Overview

`staging` contains all the codes meant to be run in this example. If you'd like to only deploy one function to AWS lambda, you can use `bert-runner.py` to test the code locally and then use `bert-deploy.py` to run the code in AWS lambda

```
# Run code locally
$ bert-runner.py -m staging

# Build code to run in AWS lambda
$ bert-deploy.py -m staging

# Run code in AWS Lambda
$ bert-deploy.py -m staging -i
```

## Helper Images

To run `bert-etl` locally using `bert-runner.py`, you'll need a redis connection listening on 6379 of your host. Here is a docker command that'll do that for you

```
docker run -p 6379:6379 -d redis
```

## How to install docker

Please reference the following gist for a complete install script, https://gist.github.com/jbcurtin/ea10d25475de401360fd9d44b5d392ac

## Bert ETL Documentation

https://bert-etl.readthedocs.io/en/latest/

