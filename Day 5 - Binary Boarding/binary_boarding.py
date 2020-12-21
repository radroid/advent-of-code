import pathlib


def decode_binary_boarding(boarding_pass: str):
    if not len(boarding_pass) == 10:
        raise ValueError('The length of the boarding pass'
                         ' entered is not equal to 10.')

    row_binary = boarding_pass[:7].replace('F', '0').replace('B', '1')
    col_binary = boarding_pass[7:].replace('L', '0').replace('R', '1')

    row_num = int(row_binary, 2)
    col_num = int(col_binary, 2)
    seat_id = row_num * 8 + col_num

    return row_num, col_num, seat_id


def highest_seat_ID(path_to_passes: pathlib.PosixPath):
    if not path_to_passes.exists():
        raise FileExistsError('No file exists at the path provided.')

    with path_to_passes.open('r') as f:
        passes = f.read().split('\n')

    highest_id = 0
    for boarding_pass in passes:
        data = decode_binary_boarding(boarding_pass)
        highest_id = max(data[-1], highest_id)
    
    print(f'The highest seat ID in the data is: {highest_id}')
    
    return highest_id


if __name__ == '__main__':
    path = pathlib.Path('boarding_passes.txt')
    highest_seat_ID(path)





