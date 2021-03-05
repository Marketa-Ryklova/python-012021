phone_number = input("Zadejte telefonní číslo: ")
phone_number = phone_number.replace(" ", "")

def control_phone_number(phone_number):
  if len(phone_number) == 9 :
    return True
  elif len(phone_number) == 13:
    return True
  else:
    print("Vámi zadané číslo není platné")

result1 = control_phone_number(phone_number)
if result1 :
  message_text = input("Zadej text zprávy: ")
else:
  print("Vámi zadané číslo není platné")


paid_text = ((len(message_text) // 180) +1 )
#print(paid_text)


def total_price(paid_text):
  price = paid_text * 3
  return price


if result1:
  message_price = total_price(paid_text)
  print(f"Výsledná cena je {message_price}Kč.")