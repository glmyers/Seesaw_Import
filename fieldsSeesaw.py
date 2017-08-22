#!/usr/bin/env python3
'''Field lists for Seesaw CSV upload files and must be
in the same folder as uploadSeesaw.py for it to function.
Running this alone prints a list of all fields to the terminal.
'''
def seesawFields():
    #Required: 'location_id', 'location_name'
    fields = ['Teacher Email', 'Teacher First Name', 'Teacher Last Name',
                'Class Name', 'Grade Level', 'Sign In Mode', 'Student Name',
                'Student ID', 'Student Email', 'Student Password',
                'Co-Teacher 1 Email', 'Co-Teacher 1 First Name', 'Co-Teacher 1 Last Name',
                'Co-Teacher 2 Email', 'Co-Teacher 2 First Name', 'Co-Teacher 2 Last Name',
                'Co-Teacher 3 Email', 'Co-Teacher 3 First Name', 'Co-Teacher 3 Last Name',
                'Co-Teacher 4 Email', 'Co-Teacher 4 First Name', 'Co-Teacher 4 Last Name',
                'Co-Teacher 5 Email', 'Co-Teacher 5 First Name', 'Co-Teacher 5 Last Name']
    return fields


def main():
    #Prints the fiels list to the terminal window one per line.
    print()
    print('Seesaw Fields')
    for field in seesawFields():
        print(field)
    print()
    return

if __name__ == '__main__': main()
