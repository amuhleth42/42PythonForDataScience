from load_csv import load
import matplotlib.pyplot as plt


def parse_as_float(s: str) -> str:
    if s.endswith('M'):
        return float(s[:-1]) * 1e6
    elif s.endswith('k'):
        return float(s[:-1]) * 1e3
    else:
        return float(s)


def main():
    df = load("population_total.csv")
    try:
        swiss = df.loc[df['country'] == 'Switzerland'].values[0, 1:]
        swiss = [parse_as_float(x) for x in swiss]
        nigeria = df.loc[df['country'] == 'Nigeria'].values[0, 1:]
        nigeria = [parse_as_float(x) for x in nigeria]
        years = df.columns[1:]

        yticks = list(range(100, 801, 100))
        yticks_values = [x * 1000000 for x in yticks]
        plt.plot(years, swiss, label="Switzerland")
        plt.plot(years, nigeria, label="Nigeria")
        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.ylabel("Population")
        plt.xticks(years[::40])
        plt.yticks(yticks_values, [f"{x}M" for x in yticks])

        plt.legend()
        plt.show()

    except Exception as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
