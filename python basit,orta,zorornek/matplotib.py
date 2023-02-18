import matplotlib.pyplot as plt
grublar=["a","b","c"]
veriler=[15,10,45]
plt.figure(figsize=(9,3))
plt.subplot(131)
plt.bar(grublar,veriler)
plt.subplot(132)
plt.scatter(grublar,veriler)
plt.subplot(133)
plt.plot(grublar,veriler)
plt.suptitle("KATEGORİLER")
plt.show()


