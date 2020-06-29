import argparse
import plistlib

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('file', nargs='?')
    args = parser.parse_args()
    if args.file is not None:
        file = args.file
        with open(file, 'rb') as fp:
            plist = plistlib.loads(fp)

        print(plist)
