def test_function():
    return
    def inner_function():
      print("Я в области видимости функции test_function")
      return

test_function()
inner_function()