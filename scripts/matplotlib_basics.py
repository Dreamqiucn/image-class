import matplotlib.pyplot as plt
labels=["a","b","c"]
counts=[5,3,7]
value=[1,42,41,65,43,2,7,52]
fig,ax=plt.subplots()
ax.bar(labels,counts)#柱状图bar
ax.set_title("samples per class")
ax.set_xlabel("class")
ax.set_ylabel("count")

plt.show()