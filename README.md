# Pre-Module-Assignment - Jesse Warren

Steps to run my assignment

1. Create conda environment
    conda create -n csv_filter python=3.11
2. Activate Environment
    conda activate csv_filter
3. Download Dependencies
    pip install -r requirements.txt
4. Install the csv_filter package for command line ussage
    pip install --editable .
5. Run the command line tool (Using the provided input.csv to test)
    csv-filter input.csv output.csv "Student" "occupation"
6. Run the Unit Tests
    pytest