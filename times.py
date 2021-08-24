#!/usr/bin/env python3

import pytz
from datetime import datetime
from random import choice

from tabulate import tabulate


ZONES = {
    'Cape Town': 'Africa/Johannesburg',
    'London': 'Europe/London',
    'Toronto': 'Canada/Eastern',
    'Kathmandu': 'Asia/Kathmandu',
    'Nairobi': 'Africa/Nairobi',
}
DATE_FORMAT = '%d-%m-%y %H:%M:%S'
HEADER = ['Location', 'Date', 'Time']
TABLE_FORMAT = 'pretty'
TABLE_FORMATS = [
    'plain',
    'simple',
    'github',
    'grid',
    'fancy_grid',
    'pipe',
    'orgtbl',
    'jira',
    'presto',
    'pretty',
    'psql',
]


def main(fmt=None, header=[]):
    table = []
    for label, tz in ZONES.items():
        dt_str = datetime.now(pytz.timezone(tz)).strftime(DATE_FORMAT)
        table.append([label] + dt_str.split())

    fmt = fmt or TABLE_FORMAT
    print(tabulate(table, headers=header, tablefmt=fmt))


if __name__ == '__main__':
    main()
