현재 서비스 데이터베이스 CREATE 쿼리

-- 사용자 테이블
CREATE TABLE user (
    id VARCHAR(36) PRIMARY KEY,
    country VARCHAR(255),
    name VARCHAR(255)
);

-- 매장 테이블
CREATE TABLE store (
    id VARCHAR(36) PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    phone_number VARCHAR(255),
    store_type ENUM('food', 'cafe', 'drink'),
    bln VARCHAR(255),
    owner_name VARCHAR(255)
);

-- 쿠폰 테이블
CREATE TABLE coupon (
    id VARCHAR(36) PRIMARY KEY,
    store_id VARCHAR(36),
    status ENUM('available', 'unavailable'),
    name VARCHAR(255),
    validity_period INT,
    FOREIGN KEY (store_id) REFERENCES store(id)
);

-- 쿠폰 사용 이력 테이블
CREATE TABLE coupon_history (
    user_id VARCHAR(36),
    coupon_id VARCHAR(36),
    expiration DATE,
    status ENUM('used', 'notUsed'),
    PRIMARY KEY (user_id, coupon_id),
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (coupon_id) REFERENCES coupon(id)
);

-- 매장 점유 이력 테이블
CREATE TABLE occupy_history (
    store_id VARCHAR(36),
    date DATE,
    user_id VARCHAR(36),
    country VARCHAR(255),
    PRIMARY KEY (store_id, date, user_id),
    FOREIGN KEY (store_id) REFERENCES store(id),
    FOREIGN KEY (user_id) REFERENCES user(id)
);

-- 운영시간 테이블
CREATE TABLE operating_hour (
    yoil VARCHAR(255),
    store_id VARCHAR(36),
    open_time TIME,
    close_time TIME,
    PRIMARY KEY (yoil, store_id),
    FOREIGN KEY (store_id) REFERENCES store(id)
);

-- 메뉴 테이블
CREATE TABLE menu (
    id VARCHAR(36) PRIMARY KEY,
    store_id VARCHAR(36),
    name VARCHAR(255),
    price INT,
    image MEDIUMTEXT,
    FOREIGN KEY (store_id) REFERENCES store(id)
);

-- 사진 테이블
CREATE TABLE picture (
    id VARCHAR(36) PRIMARY KEY,
    store_id VARCHAR(36),
    image MEDIUMTEXT,
    FOREIGN KEY (store_id) REFERENCES store(id)
);