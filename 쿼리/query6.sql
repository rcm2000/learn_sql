DROP TABLE delivery_add;
DROP TABLE category;
DROP TABLE order_refund;
DROP TABLE userorder;
DROP TABLE order_refund;
DROP TABLE board;
DROP TABLE cart;
DROP TABLE cust;
DROP TABLE item;


CREATE TABLE cust(
   id CHAR(5),
   pwd VARCHAR(10) NOT NULL,
   name VARCHAR(10) NOT NULL
);
ALTER TABLE cust ADD PRIMARY KEY (id);
# ------------------------------------------

CREATE TABLE category (
	category_code	VARCHAR(30)	NOT NULL,
	category_name	VARCHAR(30)	NULL
);

ALTER TABLE category ADD PRIMARY KEY (category_code);
# ------------------------------------------

CREATE TABLE item(
   id INT,
   name VARCHAR(20),
   price INT,
   rate FLOAT,
   regdate DATE,
   category_code	VARCHAR(30)	NOT NULL
);
ALTER TABLE item ADD PRIMARY KEY (id);
ALTER TABLE item MODIFY id INT AUTO_INCREMENT;
ALTER TABLE item AUTO_INCREMENT = 1000;
ALTER TABLE item ALTER COLUMN rate SET DEFAULT 3.3;
ALTER TABLE item ADD CONSTRAINT FOREIGN KEY (category_code) REFERENCES category(category_code);


CREATE TABLE cart(
	id VARCHAR(5),
	id2 INT,
	regdate DATE NOT NULL,
	qt INT NOT NULL
);
ALTER TABLE cart ADD PRIMARY KEY (id,id2);
ALTER TABLE cart ADD CONSTRAINT FOREIGN KEY (id) REFERENCES cust(id);
ALTER TABLE cart ADD CONSTRAINT FOREIGN KEY (id2) REFERENCES item(id);

# ------------------------------------------
CREATE TABLE board(
	board_id INT,
	id VARCHAR(10),
	title VARCHAR(200) NOT NULL,
	content VARCHAR(2000) NOT NULL,
	regdate	DATE NOT NULL,
	cnt INT	
);
ALTER TABLE board ADD PRIMARY KEY (board_id);
ALTER TABLE board MODIFY board_id INT AUTO_INCREMENT;
ALTER TABLE board AUTO_INCREMENT = 100;
ALTER TABLE board ALTER COLUMN cnt SET DEFAULT 0;
ALTER TABLE board ADD CONSTRAINT FOREIGN KEY (id) REFERENCES cust(id);

INSERT INTO board (id,title,content,regdate) VALUES('id01','test','hello world',CURDATE());
# ------------------------------------------
CREATE TABLE userorder (
	order_numbers	INT	NOT NULL,
	regdate	DATE,
	qt	INT,
	address	VARCHAR(50),
	receiver_name	VARCHAR(20),
	receiver_number	VARCHAR(20),
	item_id	INT	NOT NULL,
	user_id	VARCHAR(10)
);

ALTER TABLE userorder ADD PRIMARY KEY (order_numbers);
ALTER TABLE userorder ADD CONSTRAINT FOREIGN KEY (item_id) REFERENCES item(id);
ALTER TABLE userorder ADD CONSTRAINT FOREIGN KEY (user_id) REFERENCES cust(id);
# ------------------------------------------
CREATE TABLE order_refund (
	refund_numbers	INT	NOT NULL,
	order_numbers	INT	NOT NULL,
	refund_reason	VARCHAR(200),
	refund_img	VARCHAR(20),
	refund_email	VARCHAR(30)
);
ALTER TABLE order_refund ADD PRIMARY KEY (refund_numbers);
ALTER TABLE order_refund ADD CONSTRAINT FOREIGN KEY (order_numbers) REFERENCES userorder(order_numbers);


# ------------------------------------------

CREATE TABLE delivery_add (
	user_id	VARCHAR(10)	NOT NULL,
	zip_code	VARCHAR(20)	NULL,
	add1	VARCHAR(50)	NULL,
	add2	VARCHAR(50)	NULL
);

ALTER TABLE delivery_add ADD CONSTRAINT FOREIGN KEY (user_id) REFERENCES cust(id);


# ------------------------------------------
INSERT INTO cart VALUES('id99',2000,CURDATE(),1);
SELECT * FROM cart;

INSERT INTO cart VALUES('id01',1000,CURDATE(),1);
INSERT INTO cart VALUES('id02',1001,CURDATE(),2);
INSERT INTO cart VALUES('id03',1002,CURDATE(),2);

INSERT INTO cust VALUES('id01','pwd01','이말숙');
INSERT INTO cust VALUES('id02','pwd02','이말숙');
INSERT INTO cust VALUES('id03','pwd03','이말숙');
INSERT INTO cust VALUES('id04','pwd04','이말숙');
INSERT INTO cust VALUES('id05','pwd05','이말숙');


INSERT INTO item (NAME,PRICE,REGDATE) VALUES('pants',10000,CURDATE());
INSERT INTO item VALUES(10,'shirts',20000,3.3,'2020-01-01');

SELECT * FROM item;
SELECT * FROM cust;
