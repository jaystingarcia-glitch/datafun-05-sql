CREATE TABLE adoption (
    adoption_id TEXT,
    shelter_id TEXT,
    animal_type TEXT,
    outcome TEXT,
    fee DOUBLE,
    adopt_date DATE
);

CREATE TABLE branch (
    branch_id TEXT,
    branch_name TEXT,
    city TEXT,
    system_name TEXT
);
