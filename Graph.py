"""
Printing a graph
"""
import matplotlib.pyplot as plt

def main():
    x1 = [4.7e-5, 9.17e-5, 9.69e-5, 2.64e-4, 4.78e-4, 0.0014, 0.003, 0.006, 0.009, 0.016, 0.03, 0.05, 0.14, 0.32]
    x2 = [1.27e-4, 1.99e-4, 1.68e-4, 3.92e-4, 9.40e-4, 0.0012, 0.002, 0.005, 0.007, 0.009, 0.021, 0.06, 0.076, 0.27]
    y = []

    for i in range(1, 15):
        y.append(i)

    plt.plot(x1, y)
    plt.plot(x2, y)
    plt.legend(["DFS", "BFS"])
    plt.show()

if __name__ == "__main__":
    main()