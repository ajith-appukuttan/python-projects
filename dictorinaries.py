thisdict = {
  "brand": ("aa","ewwer","fool"),
  "model": "Mustang",
  "year": 1964
}
#print(thisdict["brand"].index("aa"))

thisdict1 = {
  "brand": {"aa","ewwer","fool"},
  "model": ("aa","ewwer","fool"),
}
#print(thisdict["brand"].index("fool"))

for x in thisdict1["brand"]:
  print(x)

for y in thisdict1["model"]:
  print(y)  





