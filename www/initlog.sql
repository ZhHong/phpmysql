CREATE TABLE IF NOT EXISTS account_log (
	`log_index`  bigint(11) NOT NULL AUTO_INCREMENT ,
	`log_type`  int(11) NOT NULL ,
	`log_account`  int(11) NOT NULL ,
	`log_time` int(11) NOT NULL,
	PRIMARY KEY (`log_index`);
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
//

CREATE TABLE IF NOT EXISTS market_log (
	`log_index`  bigint(11) NOT NULL AUTO_INCREMENT ,
	`log_type`  int(11) NOT NULL ,
	`log_market_id` int(11) NOT NULL,
	`log_account`  int(11) NOT NULL,
	`log_time` int(11) NOT NULL,
	PRIMARY KEY (`log_index`);
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
//

CREATE TABLE IF NOT EXISTS items_log (
	`log_index`  bigint(11) NOT NULL AUTO_INCREMENT ,
	`log_type`  int(50) NOT NULL ,
	`log_item_type`  int(11) NOT NULL,
	`log_account`  int(11) NOT NULL,
	`log_time` int(11) NOT NULL,
	PRIMARY KEY (`log_index`);
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
//

CREATE TABLE IF NOT EXISTS item_info_log (
	`log_index`  bigint(11) NOT NULL AUTO_INCREMENT ,
	`log_item_id` int(11) NOT NULL,
	`log_account` int(11) NOT NULL,
	`log_time` int(11) NOT NULL,
	PRIMARY KEY (`log_index`);
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
//

CREATE TABLE IF NOT EXISTS item_detail_log (
	`log_index`  bigint(11) NOT NULL AUTO_INCREMENT ,
	`log_type`  int(11) NOT NULL,
	`log_item_id`  int(11) NOT NULL ,
	`log_account` int(11) NOT NULL,
	`log_time` int(11) NOT NULL,
	PRIMARY KEY (`log_index`);
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