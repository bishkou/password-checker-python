import requests
import hashlib
import getpass


def checkPass(pwd):
    pwd = pwd.strip()
    hashedPass = hashlib.sha1(pwd.encode('utf-8')).hexdigest()
    print(hashedPass)
    firstFive = hashedPass[:5]
    rest = hashedPass[5:].upper()
    url = 'https://api.pwnedpasswords.com/range/' + firstFive
    res = requests.get(url)
    if not res.ok:
        raise RuntimeError('Error fetching "{}": {}'.format(
            url, res.status_code))

    for line in res.text.splitlines():
        # hashes[0] : The rest of the hash
        # hashes[1] : The number of occurrence
        hashes = line.split(':')
        if hashes[0] == rest:
            return hashes[1]


    return 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # pwd = getpass.getpass()
    pwd = 'password'
    try:
        count = checkPass(pwd)
    except:
        print('Something broke, please try again')

    if count:
        print(f'Your Password was found with {count} occurrences')
    else:
        print('Your Password wasn\'t found.'
              ' That doesn\'t necessarily mean it\'s a good password,'
              ' merely that it\'s not indexed on this site')

    # print(res.text)
