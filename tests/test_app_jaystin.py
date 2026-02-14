from pathlib import Path

import duckdb


def run_sql(con, filepath):
    sql = Path(filepath).read_text()
    print(f"\nRunning: {filepath}")
    con.execute(sql)
    print("Success!")


def main():
    con = duckdb.connect("test_shelter.duckdb")

    # 1. Create tables
    run_sql(con, "sql/duckdb/jaystin_shelter_schema.sql")

    # 2. Show tables (proof they exist)
    print("Tables:", con.execute("SHOW TABLES").fetchall())

    # 3. Load data
    run_sql(con, "sql/duckdb/jaystin_shelter_data.sql")

    # 4. Peek at the data (proof it loaded)
    print("Adoption sample:", con.execute("SELECT * FROM adoption LIMIT 5").fetchall())
    print("Branch sample:", con.execute("SELECT * FROM branch LIMIT 5").fetchall())

    con.close()


if __name__ == "__main__":
    main()
