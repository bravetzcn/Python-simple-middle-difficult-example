import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_excel("corona1.xltx")
print(data)
plt.plot(data["haftalık_vaka"] ,data["haftalık_vefat"],'b')
plt.xlabel("haftalıik vaka")
plt.ylabel("haftalik vefat")
plt.legend()


plt.plot(data["haftalık_vaka"] ,data["haftalık_vefat"],'g',label="vaka/vefat")
plt.xlabel("haftalıik vaka")
plt.ylabel("haftalik vefat")
plt.legend()


plt.scatter(data["haftalık_vaka"] ,data["haftalık_vefat"])
plt.legend()

plt.subplot(131)
plt.plot(data["haftalık_vaka"] ,data["haftalık_vefat"],'g',label="vaka/vefat")
plt.xlabel("haftalıik vaka")
plt.ylabel("haftalik vefat")

plt.subplot(132)
plt.plot(data["haftalık_vaka"] ,data["haftalık_vefat"],'g',label="vaka/vefat")
plt.xlabel("haftalıik vaka")
plt.ylabel("haftalik vefat")

plt.subplot(133)
plt.plot(data["haftalık_vaka"] ,data["haftalık_vefat"],'g',label="vaka/vefat")
plt.xlabel("haftalıik vaka")
plt.ylabel("haftalik vefat")
plt.suptitle("corana grafikleri")

plt.legend()
plt.show()



