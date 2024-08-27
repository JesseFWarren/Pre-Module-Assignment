# Jesse Warren Pre-Module Assignment 8/25
import pandas as pd
import argparse

def filter(input, output, value, column):
    """
    Filters the input .csv file for the specified value in the specified column and creates an output csv file

    Args:
        input: The csv file to be filtered.
        output: The name of the filtered csv file.
        value: The value to be filtered for in the inputed csv file.
        column: The column to filter for the specified value.
    """
    df = pd.read_csv(input) #Read inputed csv file
    filtered = df[df[column] == value] #Filter the df
    filtered.to_csv(output, index=False) #Export filtered df to csv called output


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input') #First command line argument for input (include .csv)
    parser.add_argument('output') #Second command line argument for output (include .csv)
    parser.add_argument('value') #Third command line argument for the value to be filtered for
    parser.add_argument('column') #Final command line argument for the column to be filtered

    args = parser.parse_args()

    filter(args.input, args.output, args.value, args.column) #Run the operation using the arguments provided via the command line

if __name__ == "__main__":
    main()