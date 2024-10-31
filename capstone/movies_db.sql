CREATE database movies_db;

USE movies_db;

CREATE TABLE Director (
    DirectorID INT PRIMARY KEY AUTO_INCREMENT,
    DirectorName VARCHAR(255)
);

CREATE TABLE Genre (
    GenreID INT PRIMARY KEY AUTO_INCREMENT,
    Genre VARCHAR(50)
);

CREATE TABLE Movie (
    MovieID INT PRIMARY KEY AUTO_INCREMENT,
    Title VARCHAR(255),
    Year INT,
    Certificate VARCHAR(10),
    Duration INT,
    Rating FLOAT,
    Metascore INT,
    DirectorID INT,
    GenreID INT,
    Description TEXT,
	ImageUrl VARCHAR(255),
    FOREIGN KEY (DirectorID) REFERENCES Director(DirectorID),
    FOREIGN KEY (GenreID) REFERENCES Genre(GenreID)
);

CREATE TABLE Cast (
    CastID INT PRIMARY KEY AUTO_INCREMENT,
    MovieID INT,
    CastMember VARCHAR(255),
    FOREIGN KEY (MovieID) REFERENCES Movie(MovieID)
);

CREATE TABLE users (
    UserID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(50) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL
);

CREATE TABLE movie_tracker (
    TrackerID INT AUTO_INCREMENT PRIMARY KEY,
    UserID INT NOT NULL,
    MovieID INT NOT NULL,
    Status VARCHAR(50) CHECK (Status IN ('not yet completed', 'in-progress', 'completed')),
    FOREIGN KEY (UserID) REFERENCES users(UserID) ON DELETE CASCADE,
    FOREIGN KEY (MovieID) REFERENCES Movie(MovieID) ON DELETE CASCADE
);

ALTER TABLE users AUTO_INCREMENT = 1;



