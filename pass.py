import random
up_alph = "qwertyuioplkjhgfdsaxzcvbnm"
lo_alph = up_alph.upper()
symbole = "{}[]()*&^%$#@!"
num = "1234567890"
all =up_alph+lo_alph+symbole+num
length = 16
password = ".".join(random.sample(all,length))
print(password)