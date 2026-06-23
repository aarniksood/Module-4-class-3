country_codec = {'India' : '0091',
                 'Aus' : '0025',
                 'Nep': ' 00977',
                 'Japan' : '0067'}

print("Countery code for india -")
print(country_codec.get('India', 'Not Found'))
print("Country code for japan -")
print(country_codec.get('Japan', 'Not Found'))
