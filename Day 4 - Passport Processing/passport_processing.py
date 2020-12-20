import pathlib
import re


class PassportProcesser:
    def __init__(self, required_fields: list = None,
                 path_to_data: str = 'passports.txt'):
        if required_fields is None:
            required_fields = ['byr', 'iyr', 'eyr', 'hgt',
                               'hcl', 'ecl', 'pid']
        self.required_fields = set(required_fields)
        self.path_to_data = pathlib.Path(path_to_data)
        if not self.path_to_data.exists():
            raise FileExistsError('No file was found at the location input.')

    def is_valid_passport(self, passport_data: dict):
        present_fields = set(passport_data.keys())
        if len(self.required_fields - present_fields) == 0:
            return True
        else:
            return False

    def get_passport_data(self):
        with self.path_to_data.open() as f:
            data = f.read()

        passports_list = data.split('\n\n')
        passports = []
        
        for passports_str in passports_list:
            passports.append(
                {data.split(':')[0]: data.split(':')[1]
                 for data in re.split(r'\s', passports_str)})
        return passports
    
    def count_valid_passports(self):
        passports_data = self.get_passport_data()
        valid_passports = 0
        for passport in passports_data:
            if self.is_valid_passport(passport):
                valid_passports += 1
        
        print(f'Number of valid passports: {valid_passports}\n'
              f'Number of passports: {len(passports_data)}')


if __name__ == '__main__':
    pp = PassportProcesser()
    pp.count_valid_passports()