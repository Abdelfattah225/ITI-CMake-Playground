#!/usr/bin/env python3
import argparse
from datetime import datetime

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate build info header')
    parser.add_argument('--output', required=True, help='Output file path')
    parser.add_argument('--generator', required=True, help='CMake generator name')
    args = parser.parse_args()

    # Get current timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # Generate header content
    content = f'''// Auto-generated file - DO NOT EDIT
#ifndef BUILD_INFO_H
#define BUILD_INFO_H

#define BUILD_TIMESTAMP "{timestamp}"
#define BUILD_GENERATOR "{args.generator}"

#endif
'''

    # Write to output file
    with open(args.output, 'w') as f:
        f.write(content)

    print(f"Generated: {args.output}")

if __name__ == '__main__':
    main()