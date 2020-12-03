import pathlib
import re


def password_checker(data: dict, password_policy: str = 'sled_rental'):
    """The function takes a a password and it's password policy and returns if the password is valid.

    Args:
        data (dict): password to be checked for validity in string format.
        password_policy (str): corresponding password policy when creating the password. Format: 'min-max char'.
                           'min' is the minimum number of 'char' to be present in the password.
                           'max' is the maximum number of 'char' to be presnet in the passwrod.
                           'char' is the character value for which the above limits are set.

    Raise:
        ValueError: if the password policy is not four characters long.

    Returns:
        bool: True if password is valid.
    """
    if not len(data) == 4:
        raise ValueError('The password policy is not in the right format. Please ensure you input the right '
                         'a total of four characters')

    if password_policy == 'sled_rental':
        num_char = data['password'].count(data['char'])
        if int(data['min']) <= num_char <= int(data['max']):
            return True
        else:
            return False
    elif password_policy == 'toboggan_corporate':
        if len(data['password']) < int(data['loc2']):
            location_2 = False
        else:
            location_2 = data['password'][int(data['loc2'])-1] == data['char']
        
        location_1 = data['password'][int(data['loc1'])-1] == data['char']
        valid = not location_1 == location_2
        return valid

    else:
        raise ValueError('Password policy entered does not exist.')



def part_one_solution(relative_path: str = 'passwords.txt'):
    """The function determines the number of valid passwords and provides the solution to part one
    of the second day's problem.

    Args:
        relative_path (str, optional): Path to the file relative to current files parent directory.
        Defaults to 'passwords.txt'.
    """
    path = pathlib.Path(__file__).parent.absolute() / relative_path
    valid_passwords = []

    with path.open('r') as f:
        for line in f.readlines():
            match = re.search(
                r'^(?P<min>\d+)-(?P<max>\d+)\s+(?P<char>[a-z]):\s+(?P<password>[a-z]+)',
                line)
            valid_passwords.append(
                password_checker(match.groupdict())
            )
    
    print(f'Total Number of passwords: {len(valid_passwords)}\n'
          f'Number of valid passwords: {valid_passwords.count(True)}')



def part_two_solution(relative_path: str = 'passwords.txt'):
    """The function determines the number of valid passwords and provides the solution to part two
    of the second day's problem.

    Args:
        relative_path (str, optional): Path to the file relative to current files parent directory.
        Defaults to 'passwords.txt'.
    """
    path = pathlib.Path(__file__).parent.absolute() / relative_path
    valid_passwords = []

    with path.open('r') as f:
        for line in f.readlines():
            match = re.search(
                r'^(?P<loc1>\d+)-(?P<loc2>\d+)\s+(?P<char>[a-z]):\s+(?P<password>[a-z]+)',
                line)
            valid_passwords.append(
                password_checker(match.groupdict(),
                                 password_policy='toboggan_corporate')
            )
    
    print(f'Total Number of passwords: {len(valid_passwords)}\n'
          f'Number of valid passwords: {valid_passwords.count(True)}')

if __name__ == '__main__':
    part_two_solution()
            

            
        
