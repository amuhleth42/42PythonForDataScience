from load_csv import load
import matplotlib.pyplot as plt


def main():
    df_life = load("life_expectancy_years.csv")
    df_gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    try:
        df_life = df_life['1900']
        df_gdp = df_gdp['1900']

        plt.scatter(df_gdp, df_life)
        plt.title('1900')
        plt.xlabel('Gross domestic product')
        plt.ylabel('Life Expectancy')
        plt.xscale('log')
        plt.xticks([300, 1000, 10000], ['300', '1k', '10k'])
        plt.show()

    except Exception as err:
        print("Error:", err)


if __name__ == "__main__":
    main()
