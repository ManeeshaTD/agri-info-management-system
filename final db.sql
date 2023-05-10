/*
SQLyog Community v13.1.5  (64 bit)
MySQL - 5.6.12-log : Database - crop prediction
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`crop prediction` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `crop prediction`;

/*Table structure for table `complaint` */

DROP TABLE IF EXISTS `complaint`;

CREATE TABLE `complaint` (
  `Complaint_id` int(11) NOT NULL AUTO_INCREMENT,
  `L_id` int(11) DEFAULT NULL,
  `prod_id` int(11) DEFAULT NULL,
  `Complaint` varchar(500) NOT NULL,
  `Reply` varchar(500) NOT NULL,
  `Date` varchar(50) NOT NULL,
  PRIMARY KEY (`Complaint_id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1;

/*Data for the table `complaint` */

insert  into `complaint`(`Complaint_id`,`L_id`,`prod_id`,`Complaint`,`Reply`,`Date`) values 
(1,3,0,'Hello','ok','2023-02-17'),
(2,3,0,'I','ko','2023-02-17'),
(3,3,0,'Hii','pending','2023-02-17'),
(4,11,2,'Asdfh','Ok','2023-02-17'),
(5,11,2,'Not Good','pending','2023-02-17'),
(6,11,2,'gg','pending','2023-02-18'),
(7,11,2,'gsgs','hb','2023-02-18'),
(8,3,0,'vvvh','pending','2023-02-18'),
(9,11,2,'bbz','pending','2023-02-18'),
(10,16,4,'Aaaaa','Ok','2023-04-13'),
(11,10,0,'Heyyy','pending','2023-04-13'),
(12,10,0,'Heyyy','pending','2023-04-13'),
(13,15,0,'Hhh','ok','2023-04-13'),
(14,15,0,'Ok','pending','2023-04-19'),
(15,15,0,'Ok','pending','2023-04-19');

/*Table structure for table `crop` */

DROP TABLE IF EXISTS `crop`;

CREATE TABLE `crop` (
  `Crop_id` int(11) NOT NULL AUTO_INCREMENT,
  `Crop_name` varchar(50) NOT NULL,
  `Description` varchar(100) NOT NULL,
  `Image` varchar(100) NOT NULL,
  PRIMARY KEY (`Crop_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `crop` */

insert  into `crop`(`Crop_id`,`Crop_name`,`Description`,`Image`) values 
(2,'okra','asdf','download.jpeg');

/*Table structure for table `disease` */

DROP TABLE IF EXISTS `disease`;

CREATE TABLE `disease` (
  `id` int(11) NOT NULL,
  `Disease` varchar(25) NOT NULL,
  `Details` varchar(100) NOT NULL,
  `precaution` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `disease` */

/*Table structure for table `expert` */

DROP TABLE IF EXISTS `expert`;

CREATE TABLE `expert` (
  `E_id` int(11) NOT NULL AUTO_INCREMENT,
  `L_id` int(11) DEFAULT NULL,
  `First_name` varchar(20) NOT NULL,
  `Last_name` varchar(10) NOT NULL,
  `place` varchar(25) NOT NULL,
  `post` varchar(25) NOT NULL,
  `pin` int(6) NOT NULL,
  `email` varchar(25) NOT NULL,
  `phone` bigint(20) NOT NULL,
  PRIMARY KEY (`E_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `expert` */

insert  into `expert`(`E_id`,`L_id`,`First_name`,`Last_name`,`place`,`post`,`pin`,`email`,`phone`) values 
(1,2,'glich','wich','kozhikode','kozhikode',630012,'gl@gmail.com',9853201254),
(2,17,'ffc','f','bbj','kannur',245633,'ss@gmail.com',9745315354);

/*Table structure for table `farmer` */

DROP TABLE IF EXISTS `farmer`;

CREATE TABLE `farmer` (
  `Farmer_id` int(11) NOT NULL AUTO_INCREMENT,
  `L_id` int(11) DEFAULT NULL,
  `First_name` varchar(20) DEFAULT NULL,
  `Last_name` varchar(10) DEFAULT NULL,
  `place` varchar(25) DEFAULT NULL,
  `post` varchar(25) DEFAULT NULL,
  `pin` int(11) DEFAULT NULL,
  `phone` bigint(20) DEFAULT NULL,
  `email` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`Farmer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1;

/*Data for the table `farmer` */

insert  into `farmer`(`Farmer_id`,`L_id`,`First_name`,`Last_name`,`place`,`post`,`pin`,`phone`,`email`) values 
(1,3,'Hali','Huk','Kannur','Kannur',987655,9658745231,'Aa@gmail.com'),
(8,10,'Wik','Vok','Kollam','Kollam',679515,9876543212,'Vv@gmail.com'),
(9,15,'Frr','Mmer','Kkd','Kkd',679567,9876543210,'Aa@gmail.com');

/*Table structure for table `fertilizer` */

DROP TABLE IF EXISTS `fertilizer`;

CREATE TABLE `fertilizer` (
  `Fertilizer_id` int(11) NOT NULL AUTO_INCREMENT,
  `E_id` int(11) DEFAULT NULL,
  `Fertilizer` varchar(50) DEFAULT NULL,
  `Description` varchar(500) DEFAULT NULL,
  `Price` int(11) DEFAULT NULL,
  PRIMARY KEY (`Fertilizer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `fertilizer` */

insert  into `fertilizer`(`Fertilizer_id`,`E_id`,`Fertilizer`,`Description`,`Price`) values 
(1,2,'Alaska Fish Emulsion','he large percentage of nitrogen is just what they need to produce large thick leaves that resist pests and disease.',260),
(5,2,'Arbico Organics Earthworm','Their thick, soil-like texture can also improve the substrate in the garden and feed loam-loving varieties of vegetables.',359);

/*Table structure for table `fertilizer_rec` */

DROP TABLE IF EXISTS `fertilizer_rec`;

CREATE TABLE `fertilizer_rec` (
  `fer_id` int(11) NOT NULL AUTO_INCREMENT,
  `reason` varchar(50) DEFAULT NULL,
  `fertilizer` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`fer_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `fertilizer_rec` */

insert  into `fertilizer_rec`(`fer_id`,`reason`,`fertilizer`) values 
(1,'Nitrogen','ammonium phosphate'),
(2,'Nitrogen','calcium ammonium nitrate'),
(3,'Nitrogen','urea'),
(4,'Phosphorus','monoammonium phosphate (MAP, 11-48- 0)'),
(5,'Phosphorus','diammonium phosphate (DAP, 18-46-0)'),
(6,'Phosphorus','polyphosphate'),
(7,'Potassium','potassium silicate'),
(8,'Potassium','sulfur- or polymer-coated potassium products');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(10) DEFAULT NULL,
  `password` varchar(10) DEFAULT NULL,
  `type` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`type`) values 
(1,'admin','admin','admin'),
(2,'ee','ee','expert'),
(3,'Ff','Ff','farmer'),
(10,'F','F','pending'),
(11,'Uu','Uu','user'),
(12,'ss','ss','user'),
(14,'Asd','Asd@gmail.','expert'),
(15,'fa','fa','farmer'),
(16,'u','u','user'),
(17,'ddfgh','ddghi','expert');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `N_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification` varchar(150) DEFAULT NULL,
  `date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`N_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`N_id`,`notification`,`date`) values 
(1,'heyy','2023-02-17'),
(3,'note','2023-02-17'),
(5,'hello','2023-04-13');

/*Table structure for table `order` */

DROP TABLE IF EXISTS `order`;

CREATE TABLE `order` (
  `Order_id` int(11) NOT NULL AUTO_INCREMENT,
  `U_id` int(11) DEFAULT NULL,
  `Date` varchar(50) DEFAULT NULL,
  `Total` varchar(50) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `order` */

insert  into `order`(`Order_id`,`U_id`,`Date`,`Total`,`status`) values 
(1,16,'2023-04-20','2400','paid');

/*Table structure for table `order details` */

DROP TABLE IF EXISTS `order details`;

CREATE TABLE `order details` (
  `Order details_id` int(11) NOT NULL AUTO_INCREMENT,
  `Product_id` int(11) DEFAULT NULL,
  `Order_id` int(11) DEFAULT NULL,
  `Quantity` double DEFAULT NULL,
  PRIMARY KEY (`Order details_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `order details` */

insert  into `order details`(`Order details_id`,`Product_id`,`Order_id`,`Quantity`) values 
(1,2,1,4),
(2,4,1,1);

/*Table structure for table `product` */

DROP TABLE IF EXISTS `product`;

CREATE TABLE `product` (
  `Product_id` int(11) NOT NULL AUTO_INCREMENT,
  `L_id` int(11) DEFAULT NULL,
  `Product` varchar(50) DEFAULT NULL,
  `Rate` double DEFAULT NULL,
  `Details` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`Product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

/*Data for the table `product` */

insert  into `product`(`Product_id`,`L_id`,`Product`,`Rate`,`Details`) values 
(2,3,'mango',500,'organic'),
(3,3,'Grape ',350,'Qwert'),
(4,3,'Coconut ',400,'Pp'),
(5,15,'Aa',123,'H');

/*Table structure for table `questions` */

DROP TABLE IF EXISTS `questions`;

CREATE TABLE `questions` (
  `Doubt_id` int(11) NOT NULL AUTO_INCREMENT,
  `E_id` int(11) DEFAULT NULL,
  `L_id` int(11) DEFAULT NULL,
  `Doubt` varchar(200) DEFAULT NULL,
  `Reply` varchar(200) DEFAULT NULL,
  `Date` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`Doubt_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `questions` */

insert  into `questions`(`Doubt_id`,`E_id`,`L_id`,`Doubt`,`Reply`,`Date`) values 
(1,2,3,'Asdgg','ok','2023-02-17'),
(2,2,3,'Hwllo','pending','2023-02-17'),
(3,2,3,'','pending','2023-02-17'),
(4,2,15,'Hyyyy','ok','2023-04-13');

/*Table structure for table `suggestions` */

DROP TABLE IF EXISTS `suggestions`;

CREATE TABLE `suggestions` (
  `Tip_id` int(11) NOT NULL AUTO_INCREMENT,
  `Tip` varchar(150) DEFAULT NULL,
  `Date` varchar(50) DEFAULT NULL,
  `E_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`Tip_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `suggestions` */

insert  into `suggestions`(`Tip_id`,`Tip`,`Date`,`E_id`) values 
(2,'use fertilizers','2023-02-17',2);

/*Table structure for table `user` */

DROP TABLE IF EXISTS `user`;

CREATE TABLE `user` (
  `U_id` int(11) NOT NULL AUTO_INCREMENT,
  `L_id` int(11) DEFAULT NULL,
  `First_name` varchar(10) DEFAULT NULL,
  `Last_name` varchar(10) DEFAULT NULL,
  `place` varchar(25) DEFAULT NULL,
  `post` varchar(25) DEFAULT NULL,
  `pin` int(6) DEFAULT NULL,
  `phone` bigint(10) DEFAULT NULL,
  `email` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`U_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;

/*Data for the table `user` */

insert  into `user`(`U_id`,`L_id`,`First_name`,`Last_name`,`place`,`post`,`pin`,`phone`,`email`) values 
(1,11,'Aswin','J','Kannur','Kannur',679876,9876567843,'Aj@gmail.com'),
(2,12,'Jinoj','P','Palakkad','Palakkad ',679854,9867453243,'jj@gmail.com'),
(4,16,'Uusr','Ssr','Pppp','Aaaa',987644,9876543212,'Aa@gmail.com');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
