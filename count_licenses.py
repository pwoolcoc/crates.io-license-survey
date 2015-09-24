#!/usr/bin/env python3
import csv
from collections import Counter

license_counter = Counter()

with open("license.csv") as csvfile:
    data = csv.reader(csvfile, dialect='excel')
    for crate_name, row in data:
        # some projects are multi-license, and they almos 
        # always use a '/' to join the license names
        licenses = row.split("/")
        for license in licenses:
            # we just want the general class of the license,
            # so the trailing '+' characters are unnecessary
            cleaned = license.strip().rstrip("+")
            if cleaned:
                license_counter.update([cleaned])

for x, n in license_counter.most_common():
    print("{x:30}{n}".format(x=x, n=n))

