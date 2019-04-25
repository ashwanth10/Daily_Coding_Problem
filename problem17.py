"""
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the length of the longest absolute path to a file in the abstracted file system. If there is no file in the system, return 0.
"""

def longest_absolute_path(files):
    longest_absolute_path_file = ''
    length_of_longest_absolute_path_file = 0

    for file in files:
        length_of_file = len(file)
        if length_of_file > length_of_longest_absolute_path_file:
            longest_absolute_path_file = file
            length_of_longest_absolute_path_file = length_of_file

    return longest_absolute_path_file

def count_tabs(s):
    return s.count('\t')

def files_in_FS(string):
    items = string.split('\n')
    stack = []
    files = []
    for item in items:
        if not item.startswith('\t'):
            stack.append(item)
        else:
            number_of_tabs = count_tabs(item)
            if(not '.' in item):
                if len(stack) == number_of_tabs - 1:
                    stack.append(item.strip('\t'))
                else:
                    stack = stack[0:number_of_tabs]
                    stack.append(item.strip('\t'))
            else:
                prefix = '/'.join(stack[0: number_of_tabs])
                files.append(prefix + '/' + item.strip('\t'))
    return files

def main():
    string1 = 'dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext'
    string2 = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'

    files = files_in_FS(string1)
    print(longest_absolute_path(files))

    files = files_in_FS(string2)
    print(longest_absolute_path(files))

if __name__ == '__main__':
    main()