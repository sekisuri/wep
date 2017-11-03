

CREATE TABLE IF NOT EXISTS `av_index` (
  `av_id` int(11) NOT NULL AUTO_INCREMENT,
  `index_name` varchar(50) DEFAULT '',
  PRIMARY KEY (`av_id`),
  UNIQUE INDEX (index_name)

) ENGINE=MyISAM  DEFAULT CHARSET=utf8;

CREATE TABLE IF NOT EXISTS `av_profile` (
  `av_id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `rank_id` int(11) unsigned DEFAULT '0',
  `hentaku_id` int(11) unsigned DEFAULT '0',
  `hentaku_name` varchar(50) DEFAULT '',
  `av_krName` varchar(50) DEFAULT '',
  `av_enName` varchar(50) DEFAULT '',
  `av_jaName` varchar(50) DEFAULT '',
  `av_height` tinyint(1) unsigned DEFAULT '0',
  `av_bust` tinyint(1) unsigned DEFAULT '0',
  `av_waist` tinyint(1) unsigned DEFAULT '0',
  `av_hip` tinyint(1) unsigned DEFAULT '0',
  `av_bustcup` char(1) DEFAULT '',
  `av_birthday` date DEFAULT '0000-00-00',
  `av_debut` varchar(100) DEFAULT '',
  `av_graph` varchar(255) DEFAULT '',
  `av_board` varchar(255) DEFAULT '',
  `av_pic1` varchar(255) DEFAULT '',
  `av_pic2` varchar(255) DEFAULT '',
  `av_pic3` varchar(255) DEFAULT '',
  `av_pic4` varchar(255) DEFAULT '',
  `av_pic5` varchar(255) DEFAULT '',
  `av_sns1` varchar(255) DEFAULT '',
  `av_sns2` varchar(255) DEFAULT '',
  `av_sns3` varchar(255) DEFAULT '',
  `av_sns4` varchar(255) DEFAULT '',
  PRIMARY KEY (`av_id`),
  UNIQUE KEY `av_krName` (`av_krName`),
  KEY `av_name` (`hentaku_name`)
) ENGINE=MyISAM DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;