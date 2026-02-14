# Purpose: Test Jaystin's shelter SQL pipeline (schema → data → sample queries)

from pathlib import Path

import duckdb


def run_sql(con, filepath):
    """Read and execute a SQL file."""
    sql = Path(filepath).read_text()
    print(f"\nRunning: {filepath}")
    con.execute(sql)
    print("Success!")


def main():
    # Connect to (or create) the test database
    con = duckdb.connect("test_shelter.duckdb")

    # ---------------------------------------------------------
    # 1. Run schema file (creates empty tables)
    # ---------------------------------------------------------
    run_sql(con, "sql/duckdb/jaystin_shelter_schema.sql")

    # Show tables to confirm schema worked
    print("\n=== Tables in Database ===")
    print(con.execute("SHOW TABLES").fetchdf())

    # ---------------------------------------------------------
    # 2. Load CSV data into the tables
    # ---------------------------------------------------------
    run_sql(con, "sql/duckdb/jaystin_shelter_data.sql")

    # ---------------------------------------------------------
    # 3. Peek at the data
    # ---------------------------------------------------------
    print("\n=== Adoption Sample (first 5 rows) ===")
    print(con.execute("SELECT * FROM adoption LIMIT 5").fetchdf())

    # ---------------------------------------------------------
    # 4. Total record count
    # ---------------------------------------------------------
    print("\n=== Total Records ===")
    print(
        con.execute("""
        SELECT COUNT(*) AS total_records
        FROM adoption
    """).fetchdf()
    )

    # ---------------------------------------------------------
    # 5. Adoptions by animal type
    # ---------------------------------------------------------
    print("\n=== Adoptions by Animal Type ===")
    print(
        con.execute("""
        SELECT animal_type, COUNT(*) AS adoption_count
        FROM adoption
        GROUP BY animal_type
        ORDER BY adoption_count DESC
    """).fetchdf()
    )

    # ---------------------------------------------------------
    # 6. Outcomes by type
    # ---------------------------------------------------------
    print("\n=== Outcomes by Type ===")
    print(
        con.execute("""
        SELECT outcome, COUNT(*) AS outcome_count
        FROM adoption
        GROUP BY outcome
        ORDER BY outcome_count DESC
    """).fetchdf()
    )

    # ---------------------------------------------------------
    # 7. Total fees collected
    # ---------------------------------------------------------
    print("\n=== Total Fees Collected ===")
    print(
        con.execute("""
        SELECT SUM(fee) AS total_fees_collected
        FROM adoption
    """).fetchdf()
    )

    # ---------------------------------------------------------
    # 8. Average adoption fee
    # ---------------------------------------------------------
    print("\n=== Average Adoption Fee ===")
    print(
        con.execute("""
        SELECT AVG(fee) AS average_adoption_fee
        FROM adoption
    """).fetchdf()
    )

    # ---------------------------------------------------------
    # 9. Adoptions by date
    # ---------------------------------------------------------
    print("\n=== Adoptions by Date ===")
    print(
        con.execute("""
        SELECT adopt_date, COUNT(*) AS adoption_count
        FROM adoption
        GROUP BY adopt_date
        ORDER BY adopt_date
    """).fetchdf()
    )

    # ---------------------------------------------------------
    # 10. Average fee by animal type
    # ---------------------------------------------------------
    print("\n=== Average Fee by Animal Type ===")
    print(
        con.execute("""
        SELECT animal_type, AVG(fee) AS average_fee
        FROM adoption
        GROUP BY animal_type
        ORDER BY average_fee DESC
    """).fetchdf()
    )

    # Close the connection
    con.close()


if __name__ == "__main__":
    main()
