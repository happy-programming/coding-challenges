def space_to_new_line(space_str):
    return '\n'.join(space_str.strip().split(" "))


if __name__ == '__main__':
    print 'Enter New Line'
    space_str = raw_input().strip()
    print space_to_new_line(space_str)
