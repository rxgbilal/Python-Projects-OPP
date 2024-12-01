class Order:
    def order_pizza(self):
        input_question_pizza = input("What kind of pizza would you like to order? Pepperoni or cheese: ")
        if input_question_pizza == "pepproni":
            ingredient = input("spicy or nomal?: ")
            if ingredient == "spicy":
                print("here is your spicy pepperoni pizza")
            else:
                print("here is your normal pepperoni pizza")
        elif input_question_pizza == "cheese":
            ingredient = input("less cheese or more cheese?: ")
            if ingredient == "less cheese":
                print("here is your less cheese pizza")
            else:
                print("here is you more cheese pizza")
        else:
            print("please choose the pizza")

    def order_burger(self):
        input_question_burger = input("What kind of burger would you like to order? Single cheese burger or double cheese burger: ")
        if input_question_burger == "cheese burger":
            print("here is your cheese burger")
        elif input_question_burger == "double cheese burger":
            print("here is your double cheese burger")
        else:
            print("please choost the burger")

input_question = input("Would you like to order a pizza? Please answer with 'yes' or 'no': ")

order_instance = Order()

if input_question == "yes":
    order_instance.order_pizza()
elif input_question == "no":
    input_question_nextitem = input("Would you like to order a burger? Please answer with 'yes' or 'no': ")
    if input_question_nextitem == "yes":
        order_instance.order_burger()
    else:
        print("Thanks for visiting.")
else:
    print("Thanks for visiting.")


