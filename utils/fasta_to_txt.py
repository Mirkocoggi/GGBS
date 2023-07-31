import sys
import os

def process(lines=None):
    if len(lines) == 2:
        ks = ['name', 'sequence']
    else:
        ks = ['name', 'sequence', 'optional', 'quality']
    return {k: v for k, v in zip(ks, lines)}

try:
    fn = sys.argv[1]
except IndexError as ie:
    raise SystemError("Error: Specify file name\n")

if not os.path.exists(fn):
    raise SystemError("Error: File does not exist\n")

if fn.endswith('a'): 
    n = 2
elif fn.endswith('q'):
    n = 4
else:
    raise SystemError("Error: Unsupported file format\n")

records = []
with open(fn, 'r') as fh:
    lines = []
    for line in fh:
        lines.append(line.rstrip())
        if len(lines) == n:
            record = process(lines)
            records.append(record)
            lines = []

fn_txt = fn.split('.')[:-1]
fn_txt = '.'.join(fn_txt) + '.txt'
with open(fn_txt, 'w') as ft:
    for record in records:
        ft.write(record['sequence']+'\n')
