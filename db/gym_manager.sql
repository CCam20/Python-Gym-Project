DROP TABLE enrollments;
DROP TABLE classes;
DROP TABLE members;

CREATE TABLE members(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    age INT,
    membership_type VARCHAR(255)
);

CREATE TABLE classes(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255)
);

CREATE TABLE enrollments(
    id SERIAL PRIMARY KEY,
    member_id INT NOT NULL REFERENCES members(id) ON DELETE CASCADE,
    class_id INT NOT NULL REFERENCES classes(id) ON DELETE CASCADE
);