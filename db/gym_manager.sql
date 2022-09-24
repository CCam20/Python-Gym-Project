DROP TABLE classes
Drop Table members

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    second_name VARCHAR(255),
    age INT,
    membership_type VARCHAR(255)
);

CREATE TABLE classes(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255)
);