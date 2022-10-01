import requests
import hashlib
import sys


def request_api_data(query_char):
    # Range option that implements k-Anonymity model to allow password to be searched by partial hashes (5 characters)
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the api')
    return res


def get_password_leaks_count(hashes, hash_to_check):
    # Get list of hashes and their count and split them into hashes and count
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        # Check if our password's hash matches any in the API response
        # Return the amount of times password has been leaked
        if h == hash_to_check:
            return count
    return 0


def pwned_api_check(password):
    # Check if password exists in the API response

    # Turn encoded object into hexadecimal
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()

    # Get first 5 hexadecimal characters and remaining tail
    first_5_characters = sha1password[:5]
    remaining_characters = sha1password[5:]

    # Pass the first 5 characters to the API and get all the hashes that start with the 5 characters
    response = request_api_data(first_5_characters)

    return get_password_leaks_count(response, remaining_characters)


def main():
    try:
        with open('./text.txt', mode='r') as my_file:
            password_text = my_file.read()
            count = pwned_api_check(password_text)
            if count:
                print(f'Password "{password_text}" was found {count} times.')
            else:
                print(f'Password "{password_text}" was not found in list of leaks')
    except FileNotFoundError as err:
        print('Check file path')


if __name__ == '__main__':
    main()

#
#
# Option for running program through console - less secure as input is saved in console
# Ex: 'python3 checkpassword.py hello'
# Using text file which can be deleted is more secure
#
# def main(args):
#     for password in args:
#         count = pwned_api_check(password)
#         if count:
#             print(f'Password "{password}" was found {count} times.')
#         else:
#             print(f'Password "{password}" was not found in list of leaks')
#     return 'done!'
#
#
# if __name__ == '__main__':
#     # Run the main function with console arguments
#     sys.exit(main(sys.argv[1:]))
