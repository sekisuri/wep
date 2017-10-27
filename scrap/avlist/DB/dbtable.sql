

CREATE TABLE IF NOT EXISTS `av_index` (
  `av_id` int(11) NOT NULL AUTO_INCREMENT,
  `index_name` varchar(50) DEFAULT '',
  PRIMARY KEY (`av_id`),
  UNIQUE INDEX (index_name)

) ENGINE=MyISAM  DEFAULT CHARSET=utf8;


