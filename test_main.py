from main import csvfile


def test_csvfile():
    main_data = "titanic_main_data.csv"
    result = csvfile(main_data)


if __name__ == "__main__":
    test_csvfile()