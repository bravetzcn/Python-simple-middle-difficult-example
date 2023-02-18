import random
lower="qwertyuıop"
upper=lower.upper()
number="123456789"
mark="!'^+%&/()=?_"

main= lower+upper+number+mark
password=random.choices(main,k=10)
# join komutu oluşturduğumuz şifrenin birleşmesini sağlar.
password="".join(password)
print(password)

