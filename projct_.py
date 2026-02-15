class InvalidChaiError(Exception): pass
             # PASS can be written in single line also...

def bill(flavor,cups):
      menu = {"masala":10,"ginger":20}
      try:
            if flavor not in menu:
                  raise InvalidChaiError("unavailable chai")
            if not isinstance(cups,int):
                  raise TypeError("no. of cups must be int.")
            total = menu[flavor] * cups

            print(f"your bill for {cups} cups of {flavor} chai:rupees{total}")
      except Exception as e:
            print("Error: ",e)
      finally:
            print("thank u")

bill("mint",2)
bill("masala","four")
bill("ginger", 4)

            