CREATE TABLE `users` (
	uid INT UNSIGNED PRIMARY KEY AUTO_INCEMENT NOT NULL,
	username VARCHAR(32) NOT NULL,
	password CHAR(64) NOT NULL,
	salt BLOB(512) NOT NULL,
	email VARCHAR(64),
	admin INT(1),
	other user info (eg. name)
);

//assess how to handle copying notes
CREATE TABLE `notes` (
	uid (ie what its saved as)
file name (ie human readable name),
original author?, //is something like this important?,
owner,
ratings, //do we only want aggregate ratings, or store each rating individually
tags,
etc. figure this all out
);

//deal with permissions somehow

CREATE TABLE `note_ratings` (
	noteID,
	userID,
	rating
); primary key (noteID, userID)

CREATE TABLE `tags_to_notes` (
	tagID,
	notesID,
)

CREATE TABLE `tags` ( //how exactly to handle this
	name
)

CREATE TABLE `subscriptions` (
	userID INT FOREIGN KEY REFERENCES users.userID ,
	courseID INT FOREIGN KEY REFERENCES courses.courseID
); primary key userID, courseID

CREATE TABLE `courses` (
	courseID primary key,
	term,
	name,
	alt_name?,
	professor INT FOREIGN KEY REFERENCES users.userID
);

CREATE TABLE `dates` (
	eventID, primary key
	courseID, foreign key
	start,
	end, //this necessary?
	title,
	description
);

CREATE TABLE `todo` (
	itemID primary key,
	userID,
	description
);

CREATE TABLE `comments` (
	commentID, (primarykey)
	userID, (ie the poster)
	postTime,
	associated with, (ie a note, class, or date)
);
