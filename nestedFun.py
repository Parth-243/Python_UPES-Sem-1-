def outer_fun(message):
  def inner_fun():
    print(message)
  return inner_fun  

clo = outer_fun("Hello Parth")

clo()

def fun(message):
  print(f"Ths is the {message}")


a= "hello boy"
fun(a);  