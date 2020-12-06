def caesarCipher(c, d=False):
  k = 3
  a = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
  c = list(c.upper().replace(" ", ""))
  for i in range(len(c)):
    if(d):
      c[i] = a[(a.index(c[i])-k)%26]
    else:
      c[i] = a[(a.index(c[i])+k)%26]
  return "".join(c)
#END FUNCTIONS  

m = "WEWILLATTACKATNOON"

print("--Begin Encryption--")
c = caesarCipher(m)
print(c)
print("--End Encryption--\n")

print("--Begin Decryption--")
print(caesarCipher(c, True))
print("--End Decryption--")
