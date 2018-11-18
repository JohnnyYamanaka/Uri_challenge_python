test_case = int(input())
qty_led = {"1": 2, "2": 5, "3": 5, "4": 4, "5": 5, "6": 6, "7": 3, "8": 7, "9": 6, "0": 6,}

for case in range(test_case):
    number_desired_to_print = input()
    led_necessary = 0
    for digit in range(len(number_desired_to_print)):
        led_necessary += qty_led[number_desired_to_print[digit]]

    print("%d leds" %led_necessary)