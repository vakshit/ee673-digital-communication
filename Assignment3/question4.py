import matplotlib.pyplot as plt


def main():
    points = [(1, 2), (3, 1), (1, 0), (0, 0), (1, 2)]

    x, y = zip(*points)

    plt.fill(x, y, "g", alpha=0.2, label="Capacity Region")

    plt.xlabel("R1 (pkt/s)")
    plt.ylabel("R2 (pkt/s)")
    plt.xlim(0, 4)
    plt.ylim(0, 3)

    plt.plot(x, y, "k")

    for i, txt in enumerate(points):
        plt.annotate(
            txt, (x[i], y[i]), textcoords="offset points", xytext=(0, 10), ha="center"
        )

    plt.legend()
    plt.grid()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
