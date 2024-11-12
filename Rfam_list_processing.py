import re
import argparse


# Author: oddguyeee
# Description: This script processes an Rfam list to adapt the ncRNA annotation.
# Usage: python script_name.py -i input.txt -o output.txt

def process_file(input_file, output_file):
    """
    Reads the input file, processes each line to extract specific columns,
    and writes the processed lines to the output file.

    Parameters:
    input_file (str): Path to the input text file containing raw data.
    output_file (str): Path to the output text file for storing processed data.
    """
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            line = line.strip()  # Remove leading and trailing whitespace

            # Split line into components and retain only the first three columns
            words = line.split(maxsplit=2)

            # Assign the first and second components to col1 and col2
            col1 = words[0]
            col2 = words[1]

            # Search for specific patterns in the third component
            match = re.search(r'^([^;]+)(; .+)?(?:; )?(.*)$', words[2])

            if match:
                rest = match.group().split()
                col3 = []
                col4 = []

                # Loop through `rest` and separate elements based on `;` presence
                for i, element in enumerate(rest):
                    if ";" in element:
                        col3.append(element)
                    else:
                        # Add the current element to col3 and the remaining elements to col4
                        col3.append(element)
                        col4.extend(rest[i + 1:])
                        break

                # Join lists to form final string outputs for col3 and col4
                col3 = " ".join(col3)
                col4 = " ".join(col4)

            else:
                # If no match, assign the third component entirely to col3
                col3 = words[2]
                col4 = ""

            # Write the formatted output to the output file
            outfile.write(f"{col1}\t{col2}\t{col3}\t{col4}\n")


def main():
    # Set up argument parsing for command-line interface
    parser = argparse.ArgumentParser(description="Process input file and format output with specified columns.")
    parser.add_argument("-i", "--input", required=True, help="Path to the input file.")
    parser.add_argument("-o", "--output", required=True, help="Path to the output file.")

    # Parse the arguments provided by the user
    args = parser.parse_args()

    # Call the process_file function with the user-specified input and output files
    process_file(args.input, args.output)


# Entry point for the script
if __name__ == "__main__":
    main()
