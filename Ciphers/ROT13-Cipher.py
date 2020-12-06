def ROT13Cipher(c, d=False):
  k = 13
  a = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
  c = list(c.upper().replace(" ", ""))
  for i in range(len(c)):
    if(d):
      c[i] = a[(a.index(c[i])-k)%26]
    else:
      c[i] = a[(a.index(c[i])+k)%26]
  return "".join(c)
#END FUNCTIONS  

m = "SECRETSPOILERALERT"

print("--Begin Encryption--")
c = ROT13Cipher(m)
print(c)
print("--End Encryption--\n")

print("--Begin Decryption--")
print(ROT13Cipher(c, True))
print("--End Decryption--")
