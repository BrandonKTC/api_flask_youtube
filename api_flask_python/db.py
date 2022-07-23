import sqlite3
DATABASE_NAME = "youtube.db"

# Create the connection to the database with sqlite3
def get_db():
    """
    create a database if not exist with sqlite3 and return the connection
    :return: return the database connect
    """
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

# Create the different table of the database
def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS user(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username VARCHAR(45) UNIQUE NOT NULL,
                email VARCHAR(45) UNIQUE NOT NULL,
                pseudo VARCHAR(45) NULL, 
                password VARCHAR(45) NOT NULL,
                created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP);
                
        CREATE TABLE IF NOT EXISTS video( 
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR(45) NOT NULL,
                duration INT NULL,
                user_id INT NOT NULL,
                source VARCHAR(45) NOT NULL,
                created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                view INT NOT NULL,
                enabled TINYINT(1) NOT NULL,
                fk_video_user_idx user_id ASC,
                CONSTRAINT fk_video_user FOREIGN KEY (user_id) REFERENCES user);
                
        CREATE TABLE IF NOT EXISTS video_format(
                        id INT NOT NULL PRIMARY KEY,
                        code VARCHAR(45) NOT NULL,
                        uri VARCHAR(45) NOT NULL,
                        video_id INT NOT NULL,
                        fk_video_format_video1_idx video_id ASC,
                        CONSTRAINT fk_video_format_video1 FOREIGN KEY(video_id) REFERENCES video);
                        
        CREATE TABLE IF NOT EXISTS token(
                        id INT PRIMARY KEY NOT NULL,
                        code VARCHAR(45) NOT NULL UNIQUE,
                        expired_at DATETIME NOT NULL,
                        user_id INT NOT NULL ,
                        CONSTRAINT fk_token_user1 FOREIGN KEY(user_id) REFERENCES user );
                        
        CREATE TABLE IF NOT EXISTS comment( 
                        id INT PRIMARY KEY NOT NULL,
                        body LONGTEXT NULL,
                        user_id INT NOT NULL,
                        video_id INT NOT NULL,
                        CONSTRAINT fk_comment_user1 FOREIGN KEY(user_id) REFERENCES user
                        CONSTRAINT fk_comment_video1 FOREIGN KEY(video_id) REFERENCES video)
        """
    ]
    # Instantiate the database
    db = get_db()
    cursor = db.cursor()
    # Instantiate the table
    for table in tables:
        cursor.executescript(table)


create_tables()
