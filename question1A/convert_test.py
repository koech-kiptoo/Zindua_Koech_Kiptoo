import main
def main_test():
    assert main.converter(5, 'USD', 'KSH') == 562.50
    assert main.converter(100, 'KSH', 'EUR') == 0.76
    assert main.converter(25, 'EUR', 'USD') == 30.00

main_test()
main.user_menu()