import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pa

#plot points on a scatter plot
data = pa.read_csv("iris.csv")

rows = 150
SepalLength = []
SepalWidth = []
plt.figure(figsize=(8,6))
# Setosa = Blue, Versis = Green, Virginica = Red
# Plotting the points
for i in range(rows):
    if data.iloc[i, 4] == "Iris-setosa":
        plt.plot(data.iloc[i, 0], data.iloc[i,1], "bo")
    if data.iloc[i, 4] == "Iris-versicolor":
        plt.plot(data.iloc[i, 0], data.iloc[i,1], "g+")
    if data.iloc[i, 4] == "Iris-virginica":
        plt.plot(data.iloc[i, 0], data.iloc[i,1], "rv")

# Creating Legend
redpatch = patches.Patch(color='red', label='Iris-virginica')
bluepatch = patches.Patch(color='blue', label='Iris-setosa')
greenpatch = patches.Patch(color='green', label='Iris-versicolor')

plt.legend(handles=[redpatch, bluepatch, greenpatch])
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.suptitle("Sepal Length (cm) vs Sepal Width (cm)")

plt.savefig("graph1.png")
plt.savefig("graph1.pdf")

plt.show()

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, layout = "tight")
fig.set_figheight(6)
fig.set_figwidth(8)


# Label the axes and create legends
ax1.set_xlabel("Petal Length (cm)")
ax1.set_ylabel("Petal Width (cm)")
ax2.set_xlabel("Petal Length (cm)")
ax2.set_ylabel("Petal Width (cm)")
ax3.set_xlabel("Petal Length (cm)")
ax3.set_ylabel("Petal Width (cm)")
ax1.legend(handles=[bluepatch], loc = "upper left")
ax2.legend(handles=[greenpatch], loc = "upper left")
ax3.legend(handles=[redpatch], loc = "upper left")


# Title the graphs
ax1.set_title("Iris-setosa")
ax2.set_title("Iris-versicolor")
ax3.set_title("Iris-viriginica")

# Create the legend
fig.suptitle("Petal Length (cm) vs Petal Width (cm)")

for i in range(rows):
    if data.iloc[i, 4] == "Iris-setosa":
        ax1.plot(data.iloc[i, 2], data.iloc[i,3], "bo")
    if data.iloc[i, 4] == "Iris-versicolor":
        ax2.plot(data.iloc[i, 2], data.iloc[i,3], "g+")
    if data.iloc[i, 4] == "Iris-virginica":
        ax3.plot(data.iloc[i, 2], data.iloc[i,3], "rv")

plt.savefig("graph2.png")
plt.savefig("graph2.pdf")
plt.show()

