

CREATE TABLE IF NOT EXISTS `av_model` (
  `av_id` int(11) NOT NULL AUTO_INCREMENT,
  `av_krName` varchar(50) DEFAULT '',
  `av_enName` varchar(50) DEFAULT '',
  `av_jaName` varchar(50) DEFAULT '',
  `av_height` tinyint(1) unsigned DEFAULT 0,
  `av_bust` tinyint(1) unsigned DEFAULT 0,
  `av_waist` tinyint(1) unsigned DEFAULT 0,
  `av_hip` tinyint(1) unsigned DEFAULT 0,
  `av_bustcup` char(1) DEFAULT '',
  `av_birthday` date DEFAULT '0000-00-00',
  `av_debut` date DEFAULT '0000-00-00',
  `av_sns1` varchar(255) DEFAULT '',
  `av_sns2` varchar(255) DEFAULT '',
  `av_sns3` varchar(255) DEFAULT '',
  `av_sns4` varchar(255) DEFAULT '',
  PRIMARY KEY (`av_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `av_title` (
  `title_id` int(11) NOT NULL AUTO_INCREMENT,
  `av_id` int(11) DEFAULT 0,
  `title_name` varchar(30) DEFAULT '',
  `release_date` date DEFAULT '0000-00-00',
  `komaker` varchar(100) DEFAULT '',
  `jamaker` varchar(100) DEFAULT '',
  `enmaker` varchar(100) DEFAULT '',
  `title_age`  tinyint(1) unsigned DEFAULT 0,
  `mosaic` char(1) DEFAULT '',
   KEY `idx_avid` (`av_id`),
   PRIMARY KEY (`title_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;
