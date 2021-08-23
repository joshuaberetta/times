#!/usr/bin/env python3

import pytz
from datetime import datetime


ZONES = {
    'Cape Town, South Africa': 'Africa/Johannesburg',
    'London, England': 'Europe/London',
    'Squamish, Canada': 'Canada/Pacific',
    'Toronto, Canada': 'Canada/Eastern',
    'Kathmandu, Nepal': 'Asia/Kathmandu',
    'Nairobi, Kenya': 'Africa/Nairobi',
}
FORMAT = '%d-%m-%y %H:%M:%S'


def main():
    longest_label = max(len(label) for label in ZONES.keys())
    div = '-' * (longest_label + len(FORMAT) + 2)
    print(div)
    for label, tz in ZONES.items():
        dt = datetime.now(pytz.timezone(tz))
        dt_str = dt.strftime(FORMAT)
        space = ' ' * (longest_label - len(label) + 1)
        print(f'{label}:{space}{dt_str}')
    print(div)


if __name__ == '__main__':
    main()
