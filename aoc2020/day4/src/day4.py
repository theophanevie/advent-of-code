import re
import sys
from typing import Dict

def isvalid(passport : Dict) -> bool:
    try:
        if not ((len(passport) == 7 and 'cid' not in passport) \
            or len(passport) == 8):
            return False
        
        if not ('byr' in passport and int(passport['byr']) >= 1920 \
            and int(passport['byr']) <= 2002):
            return False
          
        if not ('iyr' in passport and int(passport['iyr']) >= 2010 \
            and int(passport['iyr']) <= 2020):
            return False
        
        if not ('eyr' in passport and int(passport['eyr']) >= 2020 \
            and int(passport['eyr']) <= 2030):
            return False
        
        if not ('hgt' in passport and ((passport['hgt'][-2:] == 'cm' and int(passport['hgt'][:3]) >= 150 and int(passport['hgt'][:3]) <= 193) or (passport['hgt'][-2:] == 'in' and int(passport['hgt'][:2]) >= 59 and int(passport['hgt'][:2]) <= 76))):
            return False
        
        if not ('hcl' in passport and \
            re.match("#[0-9a-f]{6}", passport['hcl'])):
            return False
        
        if not ('ecl' in passport and \
            re.match("amb|blu|brn|gry|grn|hzl|oth", passport['ecl'])):
            return False
        
        if not ('pid' in passport and re.match("[0-9]{9}", passport['pid'])):
            return False

        return True

    except:
        return False


with open(sys.argv[1],'r') as inputfile:
    validpassport = 0
    passport = {}

    for line in inputfile:
        line = line.strip()

        if line == "":
            validpassport += isvalid(passport)
            passport = {}
            
        else:
            line = re.split(' |:', line)
            for i in range(0, len(line), 2):
                passport[line[i]] = line[i + 1]

validpassport += isvalid(passport)
print(validpassport)
