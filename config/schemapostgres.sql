CREATE TABLE users (
        uid serial PRIMARY KEY NOT NULL,
        username VARCHAR(32) NOT NULL,
        password CHAR(64) NOT NULL,
        salt bit(512) NOT NULL,
        email VARCHAR(64),
        admin boolean
);

CREATE TABLE notes (
        uid serial PRIMARY KEY NOT NULL,
        stored_as VARCHAR(64),
        file_name VARCHAR(32),
        owner integer REFERENCES users(uid),
        rating integer
);

CREATE TABLE note_ratings (
        noteID integer NOT NULL REFERENCES notes(uid),
        userID integer NOT NULL REFERENCES users(uid),
        rating integer,
        UNIQUE (noteID, userID)
);

CREATE TABLE tags_to_notes (
        tag VARCHAR(32) NOT NULL,
        noteID integer NOT NULL REFERENCES notes(uid),
        UNIQUE (noteID, tag)
);

CREATE TABLE terms (
        termID serial PRIMARY KEY,
        termName VARCHAR(32),
        termYear integer
);

CREATE TABLE courses (
        courseID serial PRIMARY KEY,
        term integer REFERENCES terms(termID),
        name VARCHAR(9),
        alt_name VARCHAR(255),
        professor integer REFERENCES users(uid)
);

CREATE TABLE subscriptions (
        userID integer NOT NULL REFERENCES users(uid),
        courseID integer NOT NULL REFERENCES courses(courseID),
        UNIQUE (userID, courseID)
);

CREATE TABLE dates (
        eventID serial PRIMARY KEY,
        courseID integer REFERENCES courses(courseID),
        startDate TIMESTAMP,
        endDate TIMESTAMP,
        title VARCHAR(32),
        description VARCHAR(255)
);

CREATE TABLE todo (
        itemID serial PRIMARY KEY,
        userID integer REFERENCES users(uid),
        description VARCHAR(255)
);

CREATE TABLE comments (
        commentID serial PRIMARY KEY,
        userID integer NOT NULL REFERENCES users(uid),
        postTime TIMESTAMP NOT NULL,
        courseID integer NOT NULL REFERENCES courses(courseID)
);