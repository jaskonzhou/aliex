import re
str = "200003482|32814609855|cn1520287680qivz"
print(re.findall(r"[|](.+?)[|]",str))
