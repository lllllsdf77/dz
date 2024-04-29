class Queries:
    CREATE_SURVEY_TABLE = '''CREATE TABLE IF NOT EXISTS survey (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        rate INTEGER NOT NULL CHECK (rate > 0 AND rate < 6),
        capt TEXT
    )'''
    CREATE_GENRE_TABLE = '''CREATE TABLE IF NOT EXISTS genre (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )'''
    CREATE_FOOD_TABLE = '''CREATE TABLE IF NOT EXISTS food(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price INTEGER,    
        picture TEXT,
        capt TEXT,
        genre_id INTEGER,
        FOREIGN KEY (genre_id) REFERENCES genres(id)
    )'''
    ADD_GENRE = '''
        INSERT INTO genre (name) VALUES ('сеты'),
        ('суши'),('рамен'),('пицца'),('добавки'),('салаты')
    '''
    ADD_FOOD = '''
    INSERT INTO food (name, price, picture, capt, genre_id) VALUES 
    ('Суши', 1000, 'image/image4.jpg', 'Суши с фирменной начинкой.', 2),
    ('Пицца', 600, 'image/image6.jpg', 'Пицца с хрустящим сыром.', 4),
    ('Сеты', 1000, 'image/image5.jpg', 'Сеты которые оправдают себя.', 1),
    ('Рамен', 200, 'image/image2.jpg', 'Рамен прямиком из вселенной Наруто.', 3),
    ('Добавки', 60, 'image/image7.jpg', 'Добавки к блюдам.', 5),
    ('Салат', 140, 'image/image1.jpg', 'Свежие салаты.', 6)
    '''



    DROP_GENRE_TABLE = 'DROP TABLE IF EXISTS genre'
    DROP_FOOD_TABLE = 'DROP TABLE IF EXISTS food'