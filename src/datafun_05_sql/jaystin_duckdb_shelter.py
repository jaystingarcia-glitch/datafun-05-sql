# === DECLARE IMPORTS ===

import logging
from pathlib import Path
from typing import Final

# External (must be listed in pyproject.toml)
from datafun_toolkit.logger import get_logger, log_header
import duckdb

# === CONFIGURE LOGGER ONCE PER MODULE (FILE) ===

LOG: logging.Logger = get_logger("P05", level="DEBUG")

# === DECLARE GLOBAL CONSTANTS ===

ROOT_DIR: Final[Path] = Path.cwd()

DATA_DIR: Final[Path] = ROOT_DIR / "data" / "shelter"
SQL_DIR: Final[Path] = ROOT_DIR / "sql" / "duckdb"
ARTIFACTS_DIR: Final[Path] = ROOT_DIR / "artifacts" / "duckdb"
DB_PATH: Final[Path] = ARTIFACTS_DIR / "shelter.duckdb"

# === DECLARE HELPER FUNCTION: READ SQL FROM PATH ===


def read_sql(sql_path: Path) -> str:
    """Read a SQL file from disk using UTF-8 encoding."""
    return sql_path.read_text(encoding="utf-8")


# === DECLARE HELPER FUNCTION: RUN SQL ACTION (NO RESULTS) ===


def run_sql_script(con: duckdb.DuckDBPyConnection, sql_path: Path) -> None:
    """Execute a SQL action script file (DDL or data load)."""
    LOG.info(f"RUN SQL script: {sql_path}")
    sql_text = read_sql(sql_path)
    con.execute(sql_text)
    LOG.info(f"DONE SQL script: {sql_path}")


# === DECLARE HELPER FUNCTION: RUN SQL QUERY (LOG RESULTS) ===


def run_sql_query(con: duckdb.DuckDBPyConnection, sql_path: Path) -> None:
    """Execute a SQL query script file and log the results."""
    LOG.info("")
    LOG.info(f"RUN SQL query: {sql_path}")

    sql_text = read_sql(sql_path)
    result = con.execute(sql_text)

    rows = result.fetchall()
    columns = [col[0] for col in result.description]

    LOG.info("====================================")
    LOG.info(sql_path.name)
    LOG.info("====================================")
    LOG.info(", ".join(columns))

    for row in rows:
        LOG.info(", ".join(str(value) for value in row))


# === DEFINE THE MAIN FUNCTION ===


def main() -> None:
    """Run the shelter pipeline."""
    log_header(LOG, "Jaystin Shelter Pipeline (DuckDB)")

    LOG.info("START main()")
    LOG.info(f"ROOT_DIR: {ROOT_DIR}")
    LOG.info(f"DATA_DIR: {DATA_DIR}")
    LOG.info(f"SQL_DIR: {SQL_DIR}")
    LOG.info(f"DB_PATH: {DB_PATH}")

    # Ensure artifacts directory exists
    ARTIFACTS_DIR.mkdir(parents=True, exist_ok=True)

    # Open DuckDB connection
    con = duckdb.connect(str(DB_PATH))

    try:
        # ----------------------------------------------------
        # STEP 1: CLEAN + CREATE TABLES
        # ----------------------------------------------------
        run_sql_script(con, SQL_DIR / "jaystin_shelter_schema.sql")

        # ----------------------------------------------------
        # STEP 2: LOAD CSV DATA
        # ----------------------------------------------------
        run_sql_script(con, SQL_DIR / "jaystin_shelter_data.sql")

        # ----------------------------------------------------
        # STEP 3: RUN ALL QUERIES
        # ----------------------------------------------------
        run_sql_query(con, SQL_DIR / "jaystin_shelter_query_total_records.sql")
        run_sql_query(con, SQL_DIR / "jaystin_shelter_query_adoptions_by_animal.sql")
        run_sql_query(con, SQL_DIR / "jaystin_shelter_query_outcomes.sql")
        run_sql_query(con, SQL_DIR / "jaystin_shelter_query_total_fees.sql")
        run_sql_query(con, SQL_DIR / "jaystin_shelter_query_adopt_date.sql")
        run_sql_query(con, SQL_DIR / "jaystin_shelter_query_average_fee.sql")
        run_sql_query(con, SQL_DIR / "jaystin_shelter_query_fees_by_animal.sql")

    finally:
        con.close()

    LOG.info("END main()")


# === CONDITIONAL EXECUTION GUARD ===

if __name__ == "__main__":
    main()
