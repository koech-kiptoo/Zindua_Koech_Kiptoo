# Make sure you add your code to the function below before submission
def converter(amount, original_currency, target_currency):
    # Add code here
    answer = 0
    if original_currency == "USD" and target_currency == "KSH":
        answer = amount * 112.50

    elif original_currency == "KSH" and target_currency == "USD":
        answer = amount / 112.50

    elif original_currency == "KSH" and target_currency == "EUR":
        answer = amount / 132.45

    elif original_currency == "EUR" and target_currency == "KSH":
        answer = amount * 132.45

    elif original_currency == "EUR" and target_currency == "USD":
        answer = amount * 1.20

    elif original_currency == "EUR" and target_currency == "USD":
        answer = amount / 1.20

    answer = round(answer, 2)

    return answer


def user_menu():
    while True:
        try:
            amount = float(input('Enter Amount:'))
            original_currency = str(input('Enter Original Currency:').upper())
            target_currency = str(input('Enter Original Currency:').upper())
            if original_currency not in ['KSH', 'USD', 'EUR']:
                raise Exception

            value = converter(amount, original_currency.upper(), target_currency)
            print('Your Conversion from {} to {} is {}'.format(original_currency, target_currency,
                                                               value))
            break
        except Exception as error:
            print('There was an Error, Please Try Again ', error)
            continue

