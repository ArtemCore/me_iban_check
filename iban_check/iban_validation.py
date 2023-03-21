import string

COUNTRIES = {
    "ME": [25, "Montenegro"],
}


LETTERS = {ord(d): str(i) for i, d in enumerate(string.digits + string.ascii_uppercase)}

# Montenegro IBAN format
# MEkk bbbc cccc cccc cccc xx
# k = IBAN check digits (always = "25")
# b = Bank code
# c = Account number
# x = National check digits


def get_number_iban_version(iban: str) -> str:
    return (iban[4:] + iban[:4]).translate(LETTERS)


def check_iban(iban: str) -> bool:
    # check country
    country_code: str = iban[:2].upper()
    country_digest: str = iban[:4][2:]
    valid_country = False
    valid_national_digest = False
    if country := COUNTRIES.get(country_code):
        valid_country = True
        if country_digest.isalnum():
            valid_national_digest = (int(country_digest) == country[0])
    # An IBAN is validated by converting it into an integer and performing a basic mod-97 operation
    # (as described in ISO 7064) on it. If the IBAN is valid, the remainder equals 1
    is_valid: bool = int(get_number_iban_version(iban)) % 97 == 1
    return valid_country and is_valid and valid_national_digest

