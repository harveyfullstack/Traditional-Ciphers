def railFenceCipher(c, k, d=False):
  g = [[] for i in range(k)]
  c = list(c.upper().replace(" ", ""))
  x = 0
  l = 1
  if(d):
    m = ""
    l = k+1
  for r in range(l):
    cr = 0
    dn = True
    for i in range(len(c)):
      if(not d):
        g[cr].append(c[i])
      else:
        if(r < k):
          if(cr == r):
            g[cr].append(c[x])
            x += 1
        else:
          m += g[cr].pop(0)
      if(dn):
        cr += 1
      else:
        cr -= 1
      if(cr == 0 or cr == k-1):
        dn = not dn
  if(d):
    return m
  else:
    return "".join(sum(g,[]))
#END FUNCTIONS  

m = "CHECKUNDERTHEFLOORBOARD"
c = railFenceCipher(m, 2) #Choose a key

print("--Begin Encryption--")
for k in range(2, 11):
  print("Key %s: %s" % (k, railFenceCipher(m, k)))
print("--End Encryption--\n")

print("--Begin Decryption--")
for k in range(2, 11):
  print("Key %s: %s" % (k, railFenceCipher(c, k, True)))
print("--End Decryption--")
