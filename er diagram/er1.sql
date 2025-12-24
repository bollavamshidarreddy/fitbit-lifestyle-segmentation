use fitbit_db;

ALTER TABLE heartrate_seconds_merged
ADD COLUMN Time_dt DATETIME;

ALTER TABLE heartrate_seconds_merged
ADD COLUMN id BIGINT AUTO_INCREMENT PRIMARY KEY;

CREATE INDEX idx_time_dt ON heartrate_seconds_merged(Time_dt);
SET SQL_SAFE_UPDATES = 0;


UPDATE heartrate_seconds_merged
SET Time_dt = STR_TO_DATE(Time, '%m/%d/%Y %h:%i:%s %p')
WHERE Time_dt IS NULL
limit 5000;

SELECT 
    COUNT(*) AS total_rows,
    SUM(Time_dt IS NOT NULL) AS converted_rows,
    SUM(Time_dt IS NULL) AS pending_rows
FROM heartrate_seconds_merged;



ALTER TABLE heartrate_seconds_merged
DROP COLUMN Time;


ALTER TABLE heartrate_seconds_merged
CHANGE Time_dt Time DATETIME;


select * from heartrate_seconds_merged limit 5; 