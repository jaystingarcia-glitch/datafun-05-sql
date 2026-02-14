from pathlib import Path

import duckdb


def run_sql(con, filepath):
    sql = Path(filepath).read_text()
    print(f"\nRunning: {filepath}")
    con.execute(sql)
    print("Success!")


def main():
    con = duckdb.connect("test_shelter.duckdb")

    run_sql(con, "sql/duckdb/jaystin_shelter_schema.sql")


if __name__ == "__main__":
    main()
