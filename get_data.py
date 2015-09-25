#!/usr/bin/env python3
import csv
import os
import time

import requests

CRATE_URL = "https://crates.io/api/v1/crates/{crate_name}"
INDEX_PATH = PATH HERE  # change this to
                        # INDEX_PATH = "/path/to/crates.io-index"

def walk_index(path):
    for _, _, fnames in os.walk(path):
        for fname in fnames:
            if not fname == "config.json":
                yield fname

def get_license(crate_name):
    req = requests.get(CRATE_URL.format(crate_name=crate_name))
    if req.status_code == requests.codes.ok:
        try:
            j = req.json()
            crate = j['crate']
            license = crate['license']
            if license is not None:
                license = license.lower()
            return license
        except KeyError:
            return None
        except ValueError:
            return None
    return None

with open("license.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile, dialect='excel')
    for crate_name in walk_index(INDEX_PATH):
        license = get_license(crate_name)
        writer.writerow([crate_name, license])
        # The crates.io API will cut you off if you
        # don't throttle your requests a bit
        time.sleep(0.5)
