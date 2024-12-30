COPY tweets( username, x_tweets, created_at)
FROM '/tmp/tweets_db.csv'
DELIMITER ','
CSV HEADER;

SELECT * FROM tweets LIMIT 100;