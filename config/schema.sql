CREATE TABLE `users` (
	uid INT UNSIGNED PRIMARY KEY AUTO_INCEMENT NOT NULL,
	username VARCHAR(32) NOT NULL,
	password CHAR(64) NOT NULL,
	salt BLOB(512) NOT NULL,
	email VARCHAR(64),
	admin INT(1)
);

CREATE TABLE `notes` (
    uid INT UNSIGNED PRIMARY KEY AUTO_INCREMENT NOT NULL,
	stored_as VARCHAR(64),
    file_name VARCHAR(32),
    owner INT UNSIGNED FOREIGN KEY REFERENCES users.uid,
    rating INT
);

CREATE TABLE `note_ratings` (
    noteID INT NOT NULL UNSIGNED FOREIGN KEY REFERENCES notes.uid,
	userID INT NOT NULL UNSIGNED FOREIGN KEY REFERENCES users.uid,
	rating INT,
    UNIQUE (noteID, userID)
);

CREATE TABLE `tags_to_notes` (
	tag VARCHAR(32) NOT NULL,
	noteID INT UNSIGNED NOT NULL FOREIGN KEY REFERENCES notes.uid,
    UNIQUE (noteID, tag)
)

CREATE TABLE `subscriptions` (
	userID INT NOT NULL FOREIGN KEY REFERENCES users.userID ,
	courseID INT NOT NULL FOREIGN KEY REFERENCES courses.courseID,
    UNIQUE (userID, courseID)
);

CREATE TABLE `courses` (
	courseID INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	term INT UNSIGNED FOREIGN KEY REFERENCES terms.termID,
	name VARCHAR(9),
	alt_name VARCHAR(255),
	professor INT FOREIGN KEY REFERENCES users.userID
);

CREATE TABLES `terms` (
    termID INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    termName VARCHAR(32),
    termYear INT
);

CREATE TABLE `dates` (
    eventID INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	courseID INT UNSIGNED FOREIGN KEY REFERENCES coures.courseID,
	startDate TIMESTAMP,
	endDate TIMESTAMP,
	title VARCHAR(32),
	description VARCHAR(255)
);

CREATE TABLE `todo` (
	itemID INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	userID INT UNSIGNED FOREIGN KEY REFERENCES users.uid,
	description VARCHAR(255)
);

CREATE TABLE `comments` (
	commentID UNSIGNED PRIMARY KEY AUTO_INCREMENT,
	userID INT NOT NULL UNSIGNED FOREIGN KEY REFERENCES users.uid,
	postTime NOT NULL TIMESTAMP,
    courseID INT NOT NULL UNSIGNED FOREIGN KEY REFERENCES courses.courseID
);