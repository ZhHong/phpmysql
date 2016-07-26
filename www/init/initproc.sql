CREATE TABLE IF NOT EXISTS account (
	`account_id`  bigint(11) NOT NULL AUTO_INCREMENT ,
	`account_name`  varchar(50) NOT NULL ,
	`account_pwd`  varchar(50) NOT NULL ,
	`reg_time` int(11) NOT NULL,
	PRIMARY KEY (`account_id`);
) ENGINE=InnoDB AUTO_INCREMENT=30000 DEFAULT CHARSET=utf8;
//

CREATE TABLE IF NOT EXISTS market_code (
	`market_id`  bigint(11) NOT NULL AUTO_INCREMENT ,
	`market_name`  varchar(50) NOT NULL ,
	`game_name` varchar(50) NOT NULL,
	`create_account`  int(11) NOT NULL,
	`create_time` int(11) NOT NULL,
	PRIMARY KEY (`market_id`);
) ENGINE=InnoDB AUTO_INCREMENT=1000 DEFAULT CHARSET=utf8;
//

CREATE TABLE IF NOT EXISTS items_type (
	`items_type_id`  bigint(11) NOT NULL AUTO_INCREMENT ,
	`items_type_name`  varchar(50) NOT NULL ,
	`items_market_id`  int(11) NOT NULL,
	`parent_type_id`  int(11),
	`create_account` int(11) NOT NULL,
	`create_time` int(11) NOT NULL,
	PRIMARY KEY (`items_type_id`);
) ENGINE=InnoDB AUTO_INCREMENT=2000 DEFAULT CHARSET=utf8;
//

CREATE TABLE IF NOT EXISTS item_info (
	`item_id`  bigint(11) NOT NULL AUTO_INCREMENT ,
	`item_name`  varchar(50) NOT NULL ,
	`items_type_id`  int(11) NOT NULL,
	`create_account` int(11) NOT NULL,
	`create_time` int(11) NOT NULL,
	PRIMARY KEY (`item_id`);
) ENGINE=InnoDB AUTO_INCREMENT=3000 DEFAULT CHARSET=utf8;
//

CREATE TABLE IF NOT EXISTS item_detail (
	`insert_id`  bigint(11) NOT NULL AUTO_INCREMENT ,
	`item_id`  int(11) NOT NULL ,
	`current_nums`  int(11) NOT NULL,
	`min_value` int(11) NOT NULL,
	`max_value` int(11) NOT NULL,
	`insert_account` int(11) NOT NULL,
	`insert_time` int(11) NOT NULL,
	PRIMARY KEY (`insert_id`);
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
//


DROP PROCEDURE IF EXISTS server_update;
CREATE PROCEDURE server_update()
BEGIN
	DECLARE uDbName varchar(128);
	/*=================get db name==================== */
	select database() into uDbName;
	SET @result = 0;
	/* =================update BEGIN==================== */
	/* =================update END==================== */
	SET @result = 1;
END;

CALL server_update();
DROP PROCEDURE IF EXISTS server_update;
//


DROP PROCEDURE IF EXISTS load_market;
CREATE PROCEDURE load_market ()
BEGIN
  SET @result = 0;
  SELECT market_id,market_name,game_name,create_account,create_time from market_code;
  SET @result = 1;
END;
//