#!/usr/bin/env python
# simple2links.py

import os
import sys

def parse_bed_file(bed_file):
    """Parse a BED file into a dictionary."""
    try:
        with open(bed_file, 'r') as f:
            return {line.split("\t")[3]: line.split("\t")[0:3] for line in f}
    except FileNotFoundError:
        sys.exit(f"Error: File '{bed_file}' not found.")
    except IndexError:
        sys.exit(f"Error: Malformed line in '{bed_file}'. Ensure it is in correct BED format.")

def process_simple_file(simple_file, ref_dict, qry_dict, output_file):
    """Process the simple file and write Circos link data to output."""
    with open(simple_file, 'r') as sf, open(output_file, 'w') as fo:
        for line in sf:
            if line.startswith("#"):
                continue
            items = line.strip().split("\t")
            if len(items) < 4:
                sys.exit(f"Error: Malformed line in '{simple_file}'. Ensure it has at least 4 columns.")

            # Extract gene information
            ref_start_gene, ref_end_gene = items[0], items[1]
            qry_start_gene, qry_end_gene = items[2], items[3]

            # Get chromosome and position information
            ref_chr, ref_start = ref_dict[ref_start_gene][0:2]
            ref_end = ref_dict[ref_end_gene][2]
            qry_chr, qry_start = qry_dict[qry_start_gene][0:2]
            qry_end = qry_dict[qry_end_gene][2]

            # Format Circos input
            circos_input = [ref_chr, ref_start, ref_end, qry_chr, qry_start, qry_end]
            fo.write('\t'.join(circos_input) + '\n')

def main():
    if len(sys.argv) < 2:
        sys.exit("Usage: python simple2links.py <simple_file>")

    simple_file = sys.argv[1]

    # Derive BED file names
    try:
        ref_bed = simple_file.split(".")[0] + ".bed"
        qry_bed = simple_file.split(".")[1] + ".bed"
    except IndexError:
        sys.exit("Error: Input file name must contain at least two parts separated by '.'.")

    # Parse BED files
    ref_dict = parse_bed_file(ref_bed)
    qry_dict = parse_bed_file(qry_bed)

    # Output file
    output_file = simple_file + "_link.txt"

    # Process simple file
    process_simple_file(simple_file, ref_dict, qry_dict, output_file)

    print(f"Circos link data written to '{output_file}'.")

if __name__ == "__main__":
    main()
