from csv import reader, writer
from sys import argv
from typing import List, Tuple

"""
Small utility script for formatting raw IoT-23 dataset files. 
It performs following preprocessing steps:

1. feature selection (only specified attributes are kept)
2. replaces missing values (`-`) with actual null values  

This script takes as input (in order):

[1]: a path to a IoT-23 file
[2]: output filename, where to write the CSV result. 

Example:

```
python iot-23/transform.py conn.log.labelled my_data.csv 
```

NOTE: Light manual editing is required prior to calling this script.
By default IoT-23 conn.log.labelled file has following structure:

```
#separator \x09
#set_separator	,
#empty_field	(empty)
#unset_field	-
#path	conn
#open	2019-01-01-01-01-01
#fields	uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	proto ...
#types	time	string	addr	port
```

These headers need to be manually removed such that only header labels

```
uid	id.orig_h	id.orig_p	id.resp_h	id.resp_p	proto ...
```

remain (on line 1), followed by the data rows. After this modification
this transformation script can be applied to convert to CSV.
"""

SEP, COMMENT = '   ', '#'

ATTRS = "proto,duration,orig_bytes,resp_bytes,conn_state," \
        "missed_bytes,history,orig_pkts,orig_ip_bytes,resp_pkts," \
        "resp_ip_bytes,label".split(",")


def read_csv(path: str, delimiter=',') -> Tuple[list, list]:
    """read some CSV file and split into headers and rows

    Arguments:
        path: file path to a CSV file
        delimiter: optional delimiter

    Returns:
        Tuple where first item is data headers (list)
        and second is row of data
    """
    with open(path, 'r') as read_obj:
        csv_reader = reader(read_obj, delimiter=delimiter)
        all_rows = [row for row in csv_reader]
        header = all_rows[0]
        rows = all_rows[1:]

    return header, rows


def save_csv(filename: str, rows: List[List], headers: List = None):
    """saves CSV file

    Arguments:
        filename: where to save file (with path and extension)
        rows: list of data rows
        headers: csv file headers (optional)
    """
    with open(filename, 'w') as fp:
        w = writer(fp)

        if headers:
            w.writerow(headers)

        for row in rows:
            w.writerow(row)


def split_spaces(row: list):
    """some values are space delimited, apply custom split."""
    return [j for sub in
            [item.split(SEP) if SEP in item else [item]
             for item in row] for j in sub]


def replace_missing(row: list):
    """Replace - with None value."""
    return [None if c == '-' else c for c in row]


def keep(row, index_list):
    """remove attributes not in attrs."""
    return [row[x] for x in index_list]


def convert(file_in, file_out):
    """Convert labelled IoT-23 to CSV file."""
    head, rows = read_csv(file_in, delimiter='\t')
    all_headers = split_spaces(head)
    indices = [all_headers.index(attr) for attr in ATTRS]
    csv_headers = keep(all_headers, indices)
    csv_rows = [keep(replace_missing(split_spaces(row)), indices)
                for row in rows[:-1]]

    save_csv(file_out, csv_rows, csv_headers)
    print(f'read {len(rows)} rows')
    print(f'wrote {len(csv_headers)} headers and {len(csv_rows)} rows')


if __name__ == '__main__':
    convert(argv[1], argv[2])
