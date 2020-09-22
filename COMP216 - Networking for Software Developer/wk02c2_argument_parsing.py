'''
Written by Younga
September 22, 2020

To demonstrate argument parsing

wk02c2_argument__parsing.py
'''

import argparse
DEFAULT_PORT = 12345
DEFAULT_PROTOCOL = 'tcp'

parser = argparse.ArgumentParser()
parser.add_argument(
    '-proto', 
    required=True,
    choices=['http', 'tcp', 'udp'],
    help='choices may be http, tcp or udp'
)
# python wk02c2_argument_parsing.py -proto=tcp
# python wk02c2_argument_parsing.py
# python wk02c2_argument_parsing.py -h

parser.add_argument(
    '-port',
    default=DEFAULT_PORT,
    type=int,
    help=f'prot to use for this communication, default: {DEFAULT_PORT}'
)
# python wk02c2_argument_parsing.py -proto=tcp -port=54321

parser.add_argument(
    '-u', '-user',
    help='the user name'
)
# python wk02c2_argument_parsing.py -proto=tcp -port=54321 -u=Younga

args = parser.parse_args()

print(args)