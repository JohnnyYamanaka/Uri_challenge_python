choosed_product, quantity = list(input().split(" "))

menu = {"1": 4.00, "2": 4.50, "3": 5.00, "4": 2.00, "5": 1.50}

total_values = menu[choosed_product] * float(quantity)

print("Total: R$ %.2f" % total_values)