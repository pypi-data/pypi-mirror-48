[![Build Status](https://travis-ci.org/voidpp/hdd-stat.svg?branch=master)](https://travis-ci.org/voidpp/hdd-stat)
[![Coverage Status](https://coveralls.io/repos/github/voidpp/hdd-stat/badge.svg?branch=master)](https://coveralls.io/github/voidpp/hdd-stat?branch=master)

About
--
Microservice and cli tool for get info about hdds.

Install
--
```bash
pip install hdd-stat
```

Usage
--
CLI:
```bash
hdd-stat
```
uWSGI example config:
```ini
[uwsgi]
processes = 2
module = hdd_stat.app:app
http-socket = :8090
```
