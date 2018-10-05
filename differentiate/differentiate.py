from argparse import ArgumentParser


def differentiate(x, y):
    """
    Retrieve a unique of list of elements that do not exist in both x and y.
    Capable of parsing one-dimensional (flat) and two-dimensional (lists of lists) lists.

    :param x: list #1
    :param y: list #2
    :return: list of unique values
    """
    # Validate both lists, confirm either are empty
    if len(x) == 0 and len(y) > 0:
        return y  # All y values are unique if x is empty
    elif len(y) == 0 and len(x) > 0:
        return x  # All x values are unique if y is empty

    # Get the input type to convert back to before return
    try:
        input_type = type(x[0])
    except IndexError:
        input_type = type(y[0])

    # Dealing with a 2D dataset (list of lists)
    if input_type not in (str, int, float):
        # Immutable and Unique - Convert list of tuples into set of tuples
        first_set = set(map(tuple, x))
        secnd_set = set(map(tuple, y))

    # Dealing with a 1D dataset (list of items)
    else:
        # Unique values only
        first_set = set(x)
        secnd_set = set(y)

    # Determine which list is longest
    longest = first_set if len(first_set) > len(secnd_set) else secnd_set
    shortest = secnd_set if len(first_set) > len(secnd_set) else first_set

    # Generate set of non-shared values and return list of values in original type
    return [input_type(i) for i in {i for i in longest if i not in shortest}]


def main():
    # Declare argparse argument descriptions
    usage = 'Compare two files text files and retrieve unique values'
    description = 'TODO.'
    helpers = {
        'files': "Input two text file paths",
    }

    # construct the argument parse and parse the arguments
    ap = ArgumentParser(usage=usage, description=description)
    ap.add_argument(help=helpers['files'], action='append', default=[], dest='files')
    args = vars(ap.parse_args())

    # Split text files
    txt_files = args['files'][0].split(' ')  # hackish

    data = []
    # Read each text file
    for tf in txt_files:
        with open(tf, 'r') as f:
            # Remove whitespace and \n
            data.append([l.strip() for l in f.readlines()])

    # Run differentiate
    print(differentiate(data[0], data[1]))


if __name__ == '__main__':
    main()
