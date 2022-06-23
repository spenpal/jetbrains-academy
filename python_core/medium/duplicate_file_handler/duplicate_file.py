# IMPORTS #
from collections import defaultdict
import hashlib
import os
import sys


# FUNCTIONS #
def delete_files(files):
    total_file_size = 0
    for file in files:
        total_file_size += os.path.getsize(file)
        os.remove(file)
    return total_file_size


def valid_file_numbers(file_nums_to_delete, valid_file_nums):
    files = file_nums_to_delete.split()
    while not ''.join(files).isnumeric():
        print('\nWrong format\n')
        return False
    while not all(int(file) in range(1, valid_file_nums + 1) for file in files):
        print('\nWrong format\n')
        return False

    return True


def print_duplicate_files(hashed_files_by_size, sorting_option, file_format):
    reverse = sorting_option == '1'
    sorted_hash_files_by_size = dict(sorted(hashed_files_by_size.items(), key=lambda item: item[0], reverse=reverse))
    file_num = 0
    dup_files = {}

    for size, hashed_files in sorted_hash_files_by_size.items():
        print_hashes = [f'{size} bytes']

        for h, files in hashed_files.items():
            file_formats = [file for file in files if file.endswith(file_format)]
            if not len(file_formats) > 1: continue

            print_hashes.append(f'Hash: {h}')
            for i, file in enumerate(files):
                file_num += 1
                dup_files[file_num] = file
                print_hashes.append(f'{file_num}. {file}')

        if len(print_hashes) > 1:
            print('\n'.join(print_hashes))

    return file_num, dup_files


def print_same_size_files(file_sizes, sorting_option, file_format):
    reverse = sorting_option == '1'
    sorted_file_sizes = dict(sorted(file_sizes.items(), key=lambda item: item[0], reverse=reverse))

    for size, files in sorted_file_sizes.items():
        file_formats = [file for file in files if file.endswith(file_format)]
        if not len(file_formats) > 1: continue

        print(f'{size} bytes')
        print('\n'.join(file_formats))
        print()


# MAIN #
def main():
    # Check if root directory was passed in
    if not len(sys.argv) > 1:
        print('Directory is not specified')
        sys.exit()
    root = sys.argv[1]

    # Get file format
    file_format = input('Enter file format:\n')
    any_format = len(file_format) == 0
    print()

    # Get sorting option
    size_options = """Size sorting options:
    1. Descending
    2. Ascending

    Enter a sorting option:
    """
    sorting_option = input(size_options)
    while not sorting_option.isnumeric() or sorting_option not in ['1', '2']:
        print('\nWrong option\n')
        sorting_option = input('Enter a sorting option:\n')
    print()

    # Create map of sizes and filenames
    file_sizes = defaultdict(list)
    for root, _, files in os.walk(root):
        for name in files:
            path = os.path.join(root, name)
            file_size = os.path.getsize(path)
            file_sizes[file_size].append(path)

    print_same_size_files(file_sizes, sorting_option, file_format)

    # Ask to check for duplicates in file system
    duplicate_check = input('Check for duplicates?\n')
    while duplicate_check not in ['yes', 'no']:
        print('\nWrong option\n')
        duplicate_check = input('Check for duplicates?\n')
    print()
    if duplicate_check == 'no':
        sys.exit()

    # Create hashmap of hashes and files by file size
    hashed_files_by_size = defaultdict(lambda: defaultdict(list))
    for size, files in file_sizes.items():
        for file in files:
            with open(file, 'rb') as f:
                file_hash = hashlib.md5(f.read()).hexdigest()
            hashed_files_by_size[size][file_hash].append(file)

    file_nums, dup_files = print_duplicate_files(hashed_files_by_size, sorting_option, file_format)

    # Ask user if they want to delete files
    delete = input('Delete files?\n')
    while delete not in ['yes', 'no']:
        print('\nWrong option\n')
        delete = input('Check for duplicates?\n')
    print()
    if delete == 'no':
        sys.exit()

    # Delete files
    file_nums_to_delete = input('Enter file numbers to delete:\n')
    while not valid_file_numbers(file_nums_to_delete, file_nums):
        file_nums_to_delete = input('Enter file numbers to delete:\n')
    print()

    file_nums_to_delete = [int(file_no) for file_no in file_nums_to_delete.split()]
    files_to_delete = [dup_files[file_no] for file_no in file_nums_to_delete]
    freed_storage_size = delete_files(files_to_delete)

    print(f'Total freed up space: {freed_storage_size} bytes')


if __name__ == '__main__':
    main()