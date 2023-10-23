def fizzBuzz(limit):
    for i in range(1, limit+1):
        text = ""
        if (i % 3) == 0:
            text = "Fizz"
        if (i % 5) == 0:
            text += "Buzz"
        if not text:
            text = i
        print(text)

fizzBuzz(16)