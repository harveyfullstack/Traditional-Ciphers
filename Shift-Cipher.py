def shiftCipher(c, k, d=False):
  a = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
  c = list(c.upper().replace(" ", ""))
  for i in range(len(c)):
    if(d):
      c[i] = a[(a.index(c[i])-k)%26]
    else:
      c[i] = a[(a.index(c[i])+k)%26]
  return "".join(c)
#END FUNCTIONS  

m = "HOWMANYPOSSIBLEKEYSARETHERE"
c = shiftCipher(m, 7) #Check key 7

print("--Begin Encryption--")
for k in range(1, 26):
  print("Key %s: %s" % (k, shiftCipher(m, k)))
print("--End Encryption--\n")

print("--Begin Decryption--")
for k in range(1, 26):
  print("Key %s: %s" % (k, shiftCipher(c, k, True)))
print("--End Decryption--")
