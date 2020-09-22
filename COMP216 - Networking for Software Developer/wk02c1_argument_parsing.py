'''
Written by Younga
September 22, 2020

To demonstrate argument parsing

wk02c2_argument__parsing.py
'''

import argparse
parser = argparse.ArgumentParser()
args = parser.parse_args()

print(args)