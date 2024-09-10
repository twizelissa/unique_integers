# If there is need to optimize our program more than this  
# we can go for other option like Js or use other sorting methods
import os
import time

class UniqueIntHandler:
    def __init__(self):
        self.seen = [False] * 2047 
        # to track integers from -1023 to 1023 (add 1023 to shift)

    def process_file(self, input_file_path, output_file_path):
        # try to open input and output files
        try:
            with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
                unique_integers = []

                # Go line by line and clean up spaces
                for line in infile:
                    line = line.strip()

                    # Ignore empty lines or ones that are not valid integers
                    if self.is_valid_integer(line):
                        num = int(line)
                        if not self.seen[num + 1023]:  # We adjust by 1023 to make -1023 fit
                            unique_integers.append(num)
                            self.seen[num + 1023] = True  # Now we mark that number as seen

                # Now we sort the unique integers list (implementing bubble sort manually)
                self.sort_unique_integers(unique_integers)

                # Writing results to the output file
                for num in unique_integers:
                    outfile.write(f"{num}\n")

        except FileNotFoundError:
            print(f"File not found: {input_file_path}")  # if file is missing

    def is_valid_integer(self, value):
        """Checks if a given string can be converted to an integer"""
        try:
            int(value)  # try to convert to integer
            return True  # If successful, it's valid
        except ValueError:
            return False  # If it fails, it's not an integer

    def sort_unique_integers(self, integers):
        """Sort integers using bubble sort (since we can't use the built-in sort)"""
        n = len(integers)
        for i in range(n):
            for j in range(0, n-i-1):
                if integers[j] > integers[j+1]:
                    # Swap the numbers if they are out of order
                    integers[j], integers[j+1] = integers[j+1], integers[j]

def main():
    input_dir = '../sample_inputs'  # Folder where inputs are
    output_dir = '../sample_results'  # Folder for saving the results

    # Start time to measure runtime
    start_time = time.time()

    # Process all input files from the input directory
    for input_file in os.listdir(input_dir):
        input_file_path = os.path.join(input_dir, input_file)  # get full path for input file
        output_file_path = os.path.join(output_dir, f"{input_file}_results.txt")  # create output path

        # create an instance of UniqueIntHandler and process the current file
        unique_int_handler = UniqueIntHandler()
        unique_int_handler.process_file(input_file_path, output_file_path)

    # End time to calculate how long the process took
    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # Convert seconds to milliseconds
    print(f"Time taken: {elapsed_time} ms")

if __name__ == "__main__":
    main()
