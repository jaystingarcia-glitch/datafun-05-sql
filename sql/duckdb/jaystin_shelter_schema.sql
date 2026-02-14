-- Purpose: Define the structure of the shelter database tables.

DROP TABLE IF EXISTS adoption;
DROP TABLE IF EXISTS branch;

-- Create the adoption table
CREATE TABLE adoption (
    adoption_id TEXT,
    shelter_id TEXT,
    animal_type TEXT,
    outcome TEXT,
    fee DOUBLE,
    adopt_date DATE
);
