"""
Test goes here

"""
import polars as pl

if __name__ == "__main__":
    data = pl.read_csv("test.csv")
    assert data.height > 0
    print("Input statisfy !")