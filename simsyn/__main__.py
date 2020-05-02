from simsyn import Synonymizer
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('word')
args = parser.parse_args()

print(*Synonymizer().predict(args.word))
