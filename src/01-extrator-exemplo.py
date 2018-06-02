#!/usr/bin/env python3

import datapackage
import pandas

url = 'https://raw.githubusercontent.com/frictionlessdata/example-data-packages/master/cpi/datapackage.json'
storage = datapackage.push_datapackage(descriptor=url,backend='pandas')