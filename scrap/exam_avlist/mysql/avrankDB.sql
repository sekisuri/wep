CREATE TABLE IF NOT EXISTS `ddm_rank` (
  `av_id` int(11) NOT NULL AUTO_INCREMENT,
  `rank_id` tinyint(1) unsigned DEFAULT 0,
  `av_krName` varchar(50) DEFAULT '',
  `av_enName` varchar(50) DEFAULT '',
  `av_jaName` varchar(50) DEFAULT '',
  `rank_year` char(4) DEFAULT '',
  `rank_manth` char(2) DEFAULT '',
  `tmp` varchar(255) DEFAULT '',
  `tmp2` varchar(255) DEFAULT '',
  PRIMARY KEY (`av_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;


CREATE TABLE IF NOT EXISTS `mpb_rank` (
  `av_id` int(11) NOT NULL AUTO_INCREMENT,
  `rank_id` tinyint(1) unsigned DEFAULT 0,
  `av_krName` varchar(50) DEFAULT '',
  `av_enName` varchar(50) DEFAULT '',
  `av_jaName` varchar(50) DEFAULT '',
  `rank_year` char(4) DEFAULT '',
  `rank_manth` char(2) DEFAULT '',
  `tmp` varchar(255) DEFAULT '',
  `tmp2` varchar(255) DEFAULT '',
  KEY `av_name` (`av_krName`),
  PRIMARY KEY (`av_id`)
) ENGINE=MyISAM  DEFAULT CHARSET=utf8;
