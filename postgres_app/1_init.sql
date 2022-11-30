CREATE TABLE IF NOT EXISTS Users (
    id serial PRIMARY KEY,
    name text,
    last_name text,
    time_created int,
    balance real,
    gender text,
    age int,
    city text,
    birth_day text,
    premium bool,
    ip text
    );

CREATE TABLE IF NOT EXISTS Events (
    id serial PRIMARY KEY,
    type text,
    name text,
    event_date int
);

CREATE TABLE IF NOT EXISTS Bets (
    id serial PRIMARY KEY,
    date_created int,
    userId int REFERENCES users(id) ON DELETE CASCADE,
    eventId int REFERENCES events(id) ON DELETE CASCADE
);





