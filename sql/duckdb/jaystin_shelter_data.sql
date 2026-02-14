-- Purpose: Load shelter data into DuckDB

-- Load adoption data from CSV into the adoption table
INSERT INTO adoption
SELECT * FROM read_csv_auto('data/shelter/adoption.csv');

-- Load branch data from CSV into the branch table
INSERT INTO branch
SELECT * FROM read_csv_auto('data/shelter/branch.csv');
