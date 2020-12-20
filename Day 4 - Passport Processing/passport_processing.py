import pathlib
import re


class PassportProcesser:
    def __init__(self, required_fields: list = None, path_to_data: str = 'passports.txt',
                 byr_lims: dict = None, iyr_lims: dict = None, eyr_lims: dict = None,
                 hgt_lims: dict = None, ecl: list = None):
        if required_fields is None:
            required_fields = ['byr', 'iyr', 'eyr', 'hgt',
                               'hcl', 'ecl', 'pid']
        
        self.required_fields = set(required_fields)
        self.path_to_data = pathlib.Path(path_to_data)
        if not self.path_to_data.exists():
            raise FileExistsError('No file was found at the location input.')

        if byr_lims is None:
            byr_lims = {
                'min': 1920,
                'max': 2002
            }
        self.byr_lims = byr_lims
        
        if iyr_lims is None:
            iyr_lims = {
                'min': 2010,
                'max': 2020
            }
        self.iyr_lims = iyr_lims
        
        if eyr_lims is None:
            eyr_lims = {
                'min': 2020,
                'max': 2030
            }
        self.eyr_lims = eyr_lims
        
        if hgt_lims is None:
            hgt_lims = {
                'cm_min': 150,
                'cm_max': 193,
                'in_min': 59,
                'in_max': 76
                }
        self.hgt_lims = hgt_lims
        
        if ecl is None:
            ecl = [
                'amb',
                'blu',
                'brn',
                'gry',
                'grn',
                'hzl',
                'oth'
            ]
        self.ecl = ecl
    
    def is_required_present(self, passport_data: dict):
        present_fields = set(passport_data.keys())
        if len(self.required_fields - present_fields) == 0:
            return True
        else:
            return False
    
    def is_valid_passport(self, passport_data: dict):
        if not self.is_required_present(passport_data):
            return False

        byr = re.findall(r'^\d{4}$', passport_data['byr'])
        if byr:
            if not self.byr_lims['min'] <= int(byr[0]) <= self.byr_lims['max']:
                return False
        else:
            return False

        iyr = re.findall(r'^\d{4}$', passport_data['iyr'])
        if iyr:
            if not (self.iyr_lims['min'] <= int(iyr[0]) <= self.iyr_lims['max']):
                return False
        else:
            return False

        eyr = re.findall(r'^\d{4}$', passport_data['eyr'])
        if eyr:
            if not self.eyr_lims['min'] <= int(eyr[0]) <= self.eyr_lims['max']:
                return False
        else:
            return False
        
        hgt_cm = re.findall(r'^(\d+)cm$', passport_data['hgt'])
        hgt_in = re.findall(r'^(\d+)in$', passport_data['hgt'])

        if hgt_cm:
            if not self.hgt_lims['cm_min'] <= int(hgt_cm[0]) <= self.hgt_lims['cm_max']:
                return False
        elif hgt_in:
            if not self.hgt_lims['in_min'] <= int(hgt_in[0]) <= self.hgt_lims['in_max']:
                return False
        else:
            return False
        
        hcl = re.findall(r'^#[0-9a-f]{6}$', passport_data['hcl'])
        if not hcl:
            return False

        if not (len(passport_data['ecl']) == 3 and passport_data['ecl'] in self.ecl):
            return False
        
        pid = re.findall(r'^[0-9]{9}$', passport_data['pid'])
        if not pid:
            return False

        return True

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