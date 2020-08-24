/*
SQLyog Ultimate v8.82 
MySQL - 5.5.16 : Database - school_management
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`school_management` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `school_management`;

/*Table structure for table `attendance_table` */

DROP TABLE IF EXISTS `attendance_table`;

CREATE TABLE `attendance_table` (
  `Enroll_no` bigint(20) DEFAULT NULL,
  `Roll_no` bigint(20) DEFAULT NULL,
  `Class_code` bigint(20) DEFAULT NULL,
  `Sub1_attendance` bigint(20) DEFAULT NULL,
  `Sub2_attendance` bigint(20) DEFAULT NULL,
  `Sub3_attendance` bigint(20) DEFAULT NULL,
  `Sub4_attendance` bigint(20) DEFAULT NULL,
  `Sub5_attendance` bigint(20) DEFAULT NULL,
  `Sub6_attendance` bigint(20) DEFAULT NULL,
  `Lab1_attendance` bigint(20) DEFAULT NULL,
  `Lab2_attendance` bigint(20) DEFAULT NULL,
  KEY `Class_code` (`Class_code`),
  KEY `Enroll_no` (`Enroll_no`),
  CONSTRAINT `attendance_table_ibfk_1` FOREIGN KEY (`Class_code`) REFERENCES `class_subjects` (`Class_code`),
  CONSTRAINT `attendance_table_ibfk_2` FOREIGN KEY (`Enroll_no`) REFERENCES `student_info` (`Enroll_no`),
  CONSTRAINT `attendance_table_ibfk_3` FOREIGN KEY (`Enroll_no`) REFERENCES `student_info` (`Enroll_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `attendance_table` */

insert  into `attendance_table`(`Enroll_no`,`Roll_no`,`Class_code`,`Sub1_attendance`,`Sub2_attendance`,`Sub3_attendance`,`Sub4_attendance`,`Sub5_attendance`,`Sub6_attendance`,`Lab1_attendance`,`Lab2_attendance`) values (121,1,1,17,27,28,25,19,22,4,5),(122,2,2,16,19,29,22,25,21,6,5);

/*Table structure for table `class_subjects` */

DROP TABLE IF EXISTS `class_subjects`;

CREATE TABLE `class_subjects` (
  `Class_code` bigint(20) NOT NULL AUTO_INCREMENT,
  `Class_name` char(10) DEFAULT NULL,
  `Sub1` char(30) DEFAULT NULL,
  `Sub2` char(30) DEFAULT NULL,
  `Sub3` char(30) DEFAULT NULL,
  `Sub4` char(30) DEFAULT NULL,
  `Sub5` char(30) DEFAULT NULL,
  `Sub6` char(30) DEFAULT NULL,
  `Lab1` char(30) DEFAULT NULL,
  `Lab2` char(30) DEFAULT NULL,
  PRIMARY KEY (`Class_code`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `class_subjects` */

insert  into `class_subjects`(`Class_code`,`Class_name`,`Sub1`,`Sub2`,`Sub3`,`Sub4`,`Sub5`,`Sub6`,`Lab1`,`Lab2`) values (1,'CS','Automata','Computer Network','Computer Graphics','Data Structure','Discrete Mathematics','Database Management System','Web Technology Lab','Computer Graphics Lab'),(2,'IT','Automata','Cyber Security','Computer Graphics','Data Structure','Discrete Mathematics','Database Management System','Object Oriented Lab','Computer Graphics Lab'),(3,'fddh','shivani','kanchu','asgda','gcjgz','zgcj','jzhdca','vHxvh','GXH'),(4,'fddh','shivani',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(5,'hjas','Gxh',NULL,NULL,NULL,NULL,NULL,NULL,NULL),(6,'hasgd','jadsh','HJDKH','JWHD','AHGDK','AGFKA','AFAFD','','');

/*Table structure for table `student_info` */

DROP TABLE IF EXISTS `student_info`;

CREATE TABLE `student_info` (
  `Enroll_no` bigint(20) NOT NULL AUTO_INCREMENT,
  `Stu_name` char(30) DEFAULT NULL,
  `Father_name` char(30) DEFAULT NULL,
  `Mother_name` char(30) DEFAULT NULL,
  `DOB` date DEFAULT NULL,
  `Address` char(50) DEFAULT NULL,
  `Phone` bigint(20) DEFAULT NULL,
  `Class_code` bigint(20) DEFAULT NULL,
  `pass` char(6) NOT NULL,
  PRIMARY KEY (`Enroll_no`),
  UNIQUE KEY `Enroll_no` (`Enroll_no`),
  KEY `Class_code` (`Class_code`),
  CONSTRAINT `student_info_ibfk_1` FOREIGN KEY (`Class_code`) REFERENCES `class_subjects` (`Class_code`)
) ENGINE=InnoDB AUTO_INCREMENT=135 DEFAULT CHARSET=latin1;

/*Data for the table `student_info` */

insert  into `student_info`(`Enroll_no`,`Stu_name`,`Father_name`,`Mother_name`,`DOB`,`Address`,`Phone`,`Class_code`,`pass`) values (121,'Shivani Pal','Sharat Chand Pal','Sandhya Pal','0000-00-00','Gorakhpur',786237,1,'pal'),(122,'Rakhi',NULL,NULL,NULL,NULL,NULL,2,'rakhi'),(124,'Shivam',NULL,NULL,NULL,NULL,NULL,NULL,''),(126,'Ashwani','Ria','pta nhi',NULL,NULL,NULL,NULL,''),(127,NULL,NULL,NULL,NULL,NULL,NULL,NULL,''),(128,'gffhf','fjfjh','ddhd',NULL,'ruafd',NULL,NULL,'sharma'),(129,'gffhf','fjfjh','ddhd',NULL,'ruafd',NULL,NULL,'sharma'),(130,'fdgd','fghf','cchc','2019-05-14','gfgf',4665,2,'hj'),(131,'hgjg','fgj','vh','2019-05-06','bm,n',3453453456,2,'fghjkl'),(132,'garima','jhas','sdg','2019-05-19','cbvcv',4564564567,1,'fghfgh'),(133,'divvva','ghcga','Sdhg','2020-05-14','agsxga',2435363789,1,'ghjasd'),(134,'divvva','ghcga','Sdhg','2020-05-14','agsxga',2435363789,1,'ghjasd');

/*Table structure for table `teachers_info` */

DROP TABLE IF EXISTS `teachers_info`;

CREATE TABLE `teachers_info` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `name` char(20) DEFAULT NULL,
  `age` bigint(2) DEFAULT NULL,
  `salary` bigint(20) DEFAULT NULL,
  `address` char(20) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `class_code` bigint(20) DEFAULT NULL,
  `pass` char(6) NOT NULL,
  `subject` char(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=205 DEFAULT CHARSET=latin1;

/*Data for the table `teachers_info` */

insert  into `teachers_info`(`id`,`name`,`age`,`salary`,`address`,`phone`,`class_code`,`pass`,`subject`) values (201,'Sandhya',45,25000,'Rustampur',5474,1,'pal','English'),(202,'Shiv',24,9000,'hghg',7676,2,'faltu',NULL),(203,'gfjf',56,5687,'fffff',773,2,'aggga',NULL),(204,'vnv',54,657,'gf',6545678923,2,'4gh780',NULL);

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
