def atbashCipher(c):
  a = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
  n = list("0123456789")
  c = list(c.upper().replace(" ", ""))
  for i in range(len(c)):
    if(c[i] in n):
      _ = n
    else:
      _ = a
    c[i] = _[(len(_)-1)-(_.index(c[i]))]
  return "".join(c)
#END FUNCTIONS  

m = "MIRRORMYTHOUGHTS0123"

print("--Begin Encryption--")
c = atbashCipher(m)
print(c)
print("--End Encryption--\n")

print("--Begin Decryption--")
print(atbashCipher(c))
print("--End Decryption--")
