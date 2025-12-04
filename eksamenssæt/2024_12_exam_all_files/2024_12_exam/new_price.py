def new_price(price, discount):
    new = price - (143.5 * (discount/100))

    return (new, f"{new:.02f} DKK")

print(new_price(143.50, 40))

