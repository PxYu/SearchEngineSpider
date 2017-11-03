CREATE TABLE Documents (
    d_id int NOT NULL AUTO_INCREMENT,
    idx int NOT NULL,
    query varchar(64) NOT NULL,
    title varchar(128) NOT NULL,
    url varchar(128) NOT NULL,
    snippet varchar(255) NOT NULL,
    PRIMARY KEY (d_id)
);