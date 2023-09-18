from load_csv import load
import matplotlib.pyplot as plt


def main():
    df = load("life_expectancy_years.csv")
    try:
        swiss = df.loc[df['country'] == 'Switzerland']
        years = swiss.columns[1:]
        values = swiss.values[0][1:]

        plt.plot(years, values, label="Switzerland")
        plt.title("Switzerland's Life Expectancy Projection")
        plt.xlabel("Year")
        plt.xticks(years[::40])
        plt.ylabel("Life expectancy")
        plt.show()

    except Exception as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
