import math
def ePolybiusCipher(c, d=False):
  a = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
  g = []
  c = list(c.upper().replace(" ", ""))
  s = " "
  i = 0
  while i < len(c):
    if(d):
      _ = int("".join(c[i:i+2]))
      m = int(c[i])-1
      g.append(a[_-11-(m*10)+(m*6)])
      i += 2
    else:
      _ = a.index(c[i])
      g.append(str((_%6)+11+(10*math.floor(_/6))))
      i += 1
  if(d):
    s = ""
  return s.join(g)
#END FUNCTIONS  

m = "THE PASSWORD IS 5579"

print("--Begin Encryption--")
c = ePolybiusCipher(m)
print(c)
print("--End Encryption--\n")

print("--Begin Decryption--")
print(ePolybiusCipher(c, True))
print("--End Decryption--")
