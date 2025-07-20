DROP TABLE IF EXISTS authors;

CREATE TABLE authors (
    author_id TEXT PRIMARY KEY,
    first TEXT NOT NULL,
    last TEXT NOT NULL
);
