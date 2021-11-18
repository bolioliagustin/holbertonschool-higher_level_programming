-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT id, name FROM hbtn_0d_cities WHERE state_id = (
    SELECT id
    FROM hbtn_0d_states
    WHERE name = 'California')
    ORDER BY id ASC;