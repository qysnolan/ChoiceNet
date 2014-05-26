-- MySQL dump 10.13  Distrib 5.6.11, for osx10.7 (x86_64)
--
-- Host: localhost    Database: test
-- ------------------------------------------------------
-- Server version	5.6.11

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accounts_user`
--

DROP TABLE IF EXISTS `accounts_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(70) NOT NULL,
  `first_name` varchar(40) NOT NULL,
  `last_name` varchar(40) NOT NULL,
  `isSuper` tinyint(1) NOT NULL,
  `accountType` varchar(255) DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user`
--

LOCK TABLES `accounts_user` WRITE;
/*!40000 ALTER TABLE `accounts_user` DISABLE KEYS */;
INSERT INTO `accounts_user` VALUES (2,'pbkdf2_sha256$12000$EdSA7xNqfrsh$B+tk3qP6S5sssb3Mft4p8O/thQWG/47PJyOHC9d8T4I=','2014-05-26 17:46:20',1,'admin@admin.com','admin','admin',1,'super',1,'2013-09-18 18:19:08',1),(4,'pbkdf2_sha256$10000$hIl3QpINv5vm$LPSpuCVWti9p8iZtGeWgXrgDeSXPVAFNqeymOtfR7yQ=','2013-09-23 20:07:49',0,'user@user.com','user','user',0,'user',1,'2013-09-18 19:55:18',0),(22,'pbkdf2_sha256$10000$WqMywSQmJsWA$qYhU5Bhjrd9/9viUQXXG1B1fa+cwjSOPYsRo7SXEp/0=','2013-09-21 02:40:02',0,'test@test.com','test','test',0,'user',1,'2013-09-20 21:23:46',0),(24,'pbkdf2_sha256$12000$ZhD2Xw3oQ53o$d0z5SRIG0yMbUI7/GhH4qVvCtR1qppgTpWdUcxdoaD8=','2014-05-12 22:30:47',0,'yunsheng@umass.edu','Yunsheng','Qi',0,'user',1,'2013-09-21 02:45:47',0),(25,'pbkdf2_sha256$10000$p5dp2hsEI8ZT$B2LdT1tdxRLtNiX0aE12GAxpSs5T4toozH9SQVhhXi8=','2013-09-21 03:00:34',0,'test2@test.com','test2','test',0,'user',1,'2013-09-21 03:00:34',0),(26,'pbkdf2_sha256$10000$xXTRe8ahvZ2a$56Nn2o0b3ylU6DG6CiyChMFpLHDTy6Es8BtxY/6hI+o=','2013-09-21 03:05:15',0,'test3@test.com','test3','test',0,'user',1,'2013-09-21 03:05:15',0),(27,'pbkdf2_sha256$10000$lpsZuCP7aH99$33GO9sEr4dgHXy+vjt2+95mqKT+uTwobOZESbSzGfP8=','2013-09-21 03:06:12',0,'test4@test.com','test4','test',0,'user',1,'2013-09-21 03:06:12',0),(29,'pbkdf2_sha256$10000$xc6oMrOzaNMi$2RUE6HKt0NoDZxuovEbk/TrL+dO3HBMvan3P3RkXilU=','2013-11-23 18:25:20',0,'test50@test.com','test50','test',0,'user',1,'2013-11-23 18:25:04',0),(31,'staff002','2013-11-23 18:55:06',0,'staff002@staff.com','staff002','staff',0,'',1,'2013-11-23 19:55:04',0),(32,'staff003','2013-11-23 18:56:35',0,'staff003@staff.com','staff003','staff',0,'',1,'2013-11-23 19:56:33',0),(33,'pbkdf2_sha256$10000$QdulBuBqRL9l$cfIW+MDSTbMrGQYQhRH/mNbg5gIni7lBKVeuAWQgVi4=','2013-11-23 18:57:58',0,'staff004@staff.com','staff004','staff',0,'',1,'2013-11-23 19:57:27',1),(34,'pbkdf2_sha256$12000$hB7kS1qwhiRO$OT1L3L6BA4U/e1vTEh2/P3TTRy74qj/n2k9OWHa1M4Q=','2014-04-28 21:06:28',0,'test6@test.com','test6','test',0,'user',1,'2014-04-28 20:55:35',0),(35,'pbkdf2_sha256$12000$QPkglSb2XrlW$lTJQi73O0KsTFfe6B1Xfn/l/rzQ0p8gGmO8Dls6GP4s=','2014-04-28 20:57:16',0,'test7@test.com','test7','test',0,'user',1,'2014-04-28 20:57:16',0),(36,'pbkdf2_sha256$12000$IKBt7jrUU5hY$1eqjDb56mhENujkg0NTd+FpfzK31nejysQPFBVAexrM=','2014-05-26 17:39:16',0,'provider@provider.com','Provider','Provider',0,'user',1,'2014-05-06 20:08:37',1);
/*!40000 ALTER TABLE `accounts_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_user_groups`
--

DROP TABLE IF EXISTS `accounts_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_user_groups_user_id_65e962a221168f14_uniq` (`user_id`,`group_id`),
  KEY `accounts_user_groups_6340c63c` (`user_id`),
  KEY `accounts_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_bd41e159b623616` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_5438e50cfea41873` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user_groups`
--

LOCK TABLES `accounts_user_groups` WRITE;
/*!40000 ALTER TABLE `accounts_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `accounts_user_user_permissions`
--

DROP TABLE IF EXISTS `accounts_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accounts_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `accounts_user_user_permissions_user_id_efbc882bce1aa55_uniq` (`user_id`,`permission_id`),
  KEY `accounts_user_user_permissions_6340c63c` (`user_id`),
  KEY `accounts_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_490b8e9508fc4f6f` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_641017aa580f103d` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accounts_user_user_permissions`
--

LOCK TABLES `accounts_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `accounts_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `accounts_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=55 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add permission',1,'add_permission'),(2,'Can change permission',1,'change_permission'),(3,'Can delete permission',1,'delete_permission'),(4,'Can add group',2,'add_group'),(5,'Can change group',2,'change_group'),(6,'Can delete group',2,'delete_group'),(10,'Can add content type',4,'add_contenttype'),(11,'Can change content type',4,'change_contenttype'),(12,'Can delete content type',4,'delete_contenttype'),(13,'Can add session',5,'add_session'),(14,'Can change session',5,'change_session'),(15,'Can delete session',5,'delete_session'),(16,'Can add site',6,'add_site'),(17,'Can change site',6,'change_site'),(18,'Can delete site',6,'delete_site'),(19,'Can add PayPal IPN',7,'add_paypalipn'),(20,'Can change PayPal IPN',7,'change_paypalipn'),(21,'Can delete PayPal IPN',7,'delete_paypalipn'),(22,'Can add log entry',8,'add_logentry'),(23,'Can change log entry',8,'change_logentry'),(24,'Can delete log entry',8,'delete_logentry'),(25,'Can add migration history',9,'add_migrationhistory'),(26,'Can change migration history',9,'change_migrationhistory'),(27,'Can delete migration history',9,'delete_migrationhistory'),(28,'Can add user',10,'add_user'),(29,'Can change user',10,'change_user'),(30,'Can delete user',10,'delete_user'),(31,'Can add service',11,'add_service'),(32,'Can change service',11,'change_service'),(33,'Can delete service',11,'delete_service'),(34,'Can add service type',12,'add_servicetype'),(35,'Can change service type',12,'change_servicetype'),(36,'Can delete service type',12,'delete_servicetype'),(37,'Can add invoice',13,'add_invoice'),(38,'Can change invoice',13,'change_invoice'),(39,'Can delete invoice',13,'delete_invoice'),(40,'Can add balance',14,'add_balance'),(41,'Can change balance',14,'change_balance'),(42,'Can delete balance',14,'delete_balance'),(43,'Can add session',15,'add_session'),(44,'Can change session',15,'change_session'),(45,'Can delete session',15,'delete_session'),(46,'Can add comment',16,'add_comment'),(47,'Can change comment',16,'change_comment'),(48,'Can delete comment',16,'delete_comment'),(49,'Can add income',17,'add_income'),(50,'Can change income',17,'change_income'),(51,'Can delete income',17,'delete_income'),(52,'Can add service owner',18,'add_serviceowner'),(53,'Can change service owner',18,'change_serviceowner'),(54,'Can delete service owner',18,'delete_serviceowner');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$10000$pOzOKqmyNavf$1P8a72SgVIWwvNxBJcHH1u1hkXtVY4mPK2kEMVH+j64=','2013-09-11 20:58:01',1,'yunsheng','','','qysnolan@gmail.com',1,1,'2013-09-11 20:58:01'),(2,'pbkdf2_sha256$10000$jJV8QI2upIKh$/NCd04c5HZE/b16HOk6agbi0IRhUNRnMjwGKYmV88as=','2013-09-18 15:06:04',1,'admin','','','qysnolan@126.com',1,1,'2013-09-17 14:10:57'),(3,'pbkdf2_sha256$10000$Qzb0os5CLAkU$n2M50uvfr3/yd7WB20u0x20GquerZ2GPmE8wzSNB5dA=','2013-09-18 15:04:31',0,'user@user.com','User','Testing','user@user.com',0,1,'2013-09-17 15:46:48');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`),
  CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`),
  CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `choiceNet_balance`
--

DROP TABLE IF EXISTS `choiceNet_balance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `choiceNet_balance` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `balance` decimal(64,12),
  PRIMARY KEY (`id`),
  KEY `choiceNet_balance_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_4693a5ca` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `choiceNet_balance`
--

LOCK TABLES `choiceNet_balance` WRITE;
/*!40000 ALTER TABLE `choiceNet_balance` DISABLE KEYS */;
INSERT INTO `choiceNet_balance` VALUES (1,24,1136.850195312500),(2,2,0.000000000000),(3,36,1448.218359375000);
/*!40000 ALTER TABLE `choiceNet_balance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `choiceNet_comment`
--

DROP TABLE IF EXISTS `choiceNet_comment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `choiceNet_comment` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `service_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `rate` int(11) NOT NULL,
  `comment` varchar(4096) DEFAULT NULL,
  `created_date` datetime NOT NULL,
  `is_provider` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `choiceNet_comment_91a0ac17` (`service_id`),
  KEY `choiceNet_comment_6340c63c` (`user_id`),
  CONSTRAINT `service_id_refs_id_0513f6fc` FOREIGN KEY (`service_id`) REFERENCES `service_service` (`id`),
  CONSTRAINT `user_id_refs_id_dc685cf4` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `choiceNet_comment`
--

LOCK TABLES `choiceNet_comment` WRITE;
/*!40000 ALTER TABLE `choiceNet_comment` DISABLE KEYS */;
INSERT INTO `choiceNet_comment` VALUES (1,58,24,3,'good service','2014-05-07 12:47:41',0),(2,60,24,5,'Good service','2014-05-07 13:16:37',0),(3,68,2,3,'Good service','2014-05-07 13:28:14',1),(4,64,36,3,'This is a good service','2014-05-07 13:29:06',1),(5,58,36,3,'hjgjlkjl;kl;','2014-05-07 13:42:39',1),(6,58,24,5,'dsagah','2014-05-07 15:07:39',0),(7,58,24,5,'asdgerh','2014-05-07 15:08:28',0);
/*!40000 ALTER TABLE `choiceNet_comment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `choiceNet_income`
--

DROP TABLE IF EXISTS `choiceNet_income`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `choiceNet_income` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `provider_id` int(11) NOT NULL,
  `income` decimal(64,12) DEFAULT NULL,
  `updated_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `choiceNet_income_3f126c2d` (`provider_id`),
  CONSTRAINT `provider_id_refs_id_ce531fed` FOREIGN KEY (`provider_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `choiceNet_income`
--

LOCK TABLES `choiceNet_income` WRITE;
/*!40000 ALTER TABLE `choiceNet_income` DISABLE KEYS */;
INSERT INTO `choiceNet_income` VALUES (1,36,0.000000000000,'2014-05-12 22:31:27');
/*!40000 ALTER TABLE `choiceNet_income` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `choiceNet_invoice`
--

DROP TABLE IF EXISTS `choiceNet_invoice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `choiceNet_invoice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date_created` datetime NOT NULL,
  `buyer_id` int(11) NOT NULL,
  `service_id` int(11) NOT NULL,
  `number` varchar(255) NOT NULL,
  `amount` int(11) DEFAULT NULL,
  `is_paid` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `refund_status` varchar(255),
  PRIMARY KEY (`id`),
  UNIQUE KEY `number` (`number`),
  KEY `choiceNet_invoice_f56062d8` (`buyer_id`),
  KEY `choiceNet_invoice_91a0ac17` (`service_id`),
  CONSTRAINT `buyer_id_refs_id_0b4f3d31` FOREIGN KEY (`buyer_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `service_id_refs_id_88833919` FOREIGN KEY (`service_id`) REFERENCES `service_service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=97 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `choiceNet_invoice`
--

LOCK TABLES `choiceNet_invoice` WRITE;
/*!40000 ALTER TABLE `choiceNet_invoice` DISABLE KEYS */;
INSERT INTO `choiceNet_invoice` VALUES (1,'2013-11-24 04:11:52',2,6,'1385266312359-service-6-2',964,0,1,NULL),(2,'2013-11-24 04:34:37',2,4,'1385267677651-service-4-2',269,1,1,NULL),(4,'2013-11-24 04:34:59',2,4,'1385267699074-service-4-2',269,0,1,NULL),(5,'2013-11-24 04:50:01',2,4,'1385268601978-service-4-2',269,1,1,NULL),(6,'1970-01-17 00:47:49',2,4,'1385269870.61-service-4-2',269,0,0,NULL),(7,'1970-01-17 00:47:50',2,4,'1385270414.56-service-4-2',269,1,1,NULL),(8,'2013-11-24 05:20:19',2,4,'1385270419748-service-4-2',269,0,1,NULL),(9,'1970-01-17 00:47:50',2,4,'1385270426.87-service-4-2',269,1,1,NULL),(10,'2013-11-24 05:32:04',2,4,'1385271124315-service-4-2',269,0,1,NULL),(11,'2013-11-24 05:38:02',2,18,'1385271482056-service-18-2',510,1,1,NULL),(12,'2013-11-24 05:50:05',2,4,'1385272205778-service-4-2',269,1,1,NULL),(13,'2013-11-24 06:04:53',2,6,'1385273093195-service-6-2',964,0,1,NULL),(14,'2013-11-24 07:33:54',24,10,'1385278434479-service-10-24',1,1,1,NULL),(15,'2013-11-24 07:34:21',24,18,'1385278461932-service-18-24',1,1,1,NULL),(16,'2013-11-25 04:14:52',2,3,'1385352892536-service-3-2',1,1,1,NULL),(17,'2013-11-26 03:55:55',24,20,'1385438155326-service-20-24',1,1,1,NULL),(18,'2014-01-07 18:43:36',24,6,'1389120216567-service-6-24',1,1,1,NULL),(19,'2014-01-07 19:51:23',2,3,'1389124283054-service-3-2',1,0,1,NULL),(20,'2014-03-30 20:31:45',24,51,'1396211505016-service-51-24',1,1,1,NULL),(21,'2014-03-31 23:50:43',24,2,'1396309843232-service-2-24',1,0,1,NULL),(22,'2014-04-01 17:29:30',24,6,'1396373370039-service-6-24',1,1,1,NULL),(23,'2014-04-11 15:10:49',24,4,'1397229049759-service-4-24',1,0,1,NULL),(24,'2014-04-29 20:04:12',24,3,'1398801852754-service-3-24',1,0,0,NULL),(25,'2014-04-29 20:11:11',24,6,'1398802271270-service-6-24',1,0,1,NULL),(26,'2014-04-29 20:11:26',24,6,'1398802286386-service-6-24',1,0,1,NULL),(27,'2014-04-29 20:14:47',24,56,'1398802487866-service-56-24',1,0,1,NULL),(28,'2014-04-29 20:18:49',24,56,'1398802729571-service-56-24',1,0,1,NULL),(29,'2014-04-29 20:20:02',24,56,'1398802802815-service-56-24',1,0,1,NULL),(30,'2014-04-29 20:20:53',24,56,'1398802853189-service-56-24',1,1,1,NULL),(31,'2014-04-29 20:34:03',24,56,'1398803643496-service-56-24',1,1,1,NULL),(32,'2014-04-29 20:45:38',24,3,'1398804338833-service-3-24',1,0,1,NULL),(33,'2014-04-29 23:22:35',24,6,'1398813755238-service-6-24',1,0,1,NULL),(34,'2014-04-29 23:25:08',24,6,'1398813908801-service-6-24',1,0,1,NULL),(35,'2014-04-29 23:26:03',24,6,'1398813963521-service-6-24',1,0,1,NULL),(36,'2014-04-29 23:26:35',24,6,'1398813995075-service-6-24',1,0,1,NULL),(37,'2014-04-29 23:27:39',24,3,'1398814059405-service-3-24',1,1,1,NULL),(38,'2014-04-29 23:28:52',24,56,'1398814132399-service-56-24',1,1,1,NULL),(39,'2014-04-30 20:51:17',2,3,'1398891077794-service-3-2',1,0,1,NULL),(40,'2014-04-30 20:51:36',2,3,'1398891096347-service-3-2',1,0,1,NULL),(41,'2014-05-01 14:36:43',24,56,'1398955003116-service-56-24',1,1,1,NULL),(42,'2014-05-01 14:38:18',24,56,'1398955098221-service-56-24',1,1,1,NULL),(43,'2014-05-01 14:39:45',24,56,'1398955185348-service-56-24',1,1,1,NULL),(44,'2014-05-01 14:40:12',24,56,'1398955212399-service-56-24',100000,0,1,NULL),(45,'2014-05-01 15:02:52',24,56,'1398956572692-service-56-24',1,1,1,NULL),(46,'2014-05-01 15:03:33',24,56,'1398956613793-service-56-24',1,1,1,NULL),(47,'2014-05-01 15:15:01',24,56,'1398957301264-service-56-24',1,1,1,NULL),(48,'2014-05-01 15:18:38',24,56,'1398957518510-service-56-24',1,1,1,NULL),(49,'2014-05-01 15:19:46',24,56,'1398957586155-service-56-24',1,1,1,NULL),(50,'2014-05-01 15:20:12',24,56,'1398957612586-service-56-24',1,1,1,NULL),(51,'2014-05-01 15:22:21',24,56,'1398957741935-service-56-24',1,1,1,NULL),(52,'2014-05-01 15:23:33',24,56,'1398957813460-service-56-24',1,1,1,NULL),(53,'2014-05-01 15:24:20',24,56,'1398957860992-service-56-24',1,1,1,NULL),(54,'2014-05-01 15:25:03',24,56,'1398957903483-service-56-24',1,0,0,NULL),(55,'2014-05-06 15:50:11',2,3,'1399391411738-service-3-2',1,0,1,NULL),(56,'2014-05-06 15:51:57',2,3,'1399391517682-service-3-2',1,0,1,NULL),(57,'2014-05-06 15:54:21',2,3,'1399391661762-service-3-2',1,0,1,NULL),(58,'2014-05-06 19:39:59',24,56,'1399405199331-service-56-24',1,1,1,NULL),(59,'2014-05-06 19:45:47',24,64,'1399405547619-service-64-24',1,1,1,NULL),(60,'2014-05-06 19:50:55',24,56,'1399405855278-service-56-24',1,0,0,NULL),(61,'2014-05-06 20:36:24',36,56,'1399408584579-service-56-36',1,1,1,NULL),(62,'2014-05-06 20:36:42',36,58,'1399408602047-service-58-36',1,1,1,NULL),(63,'2014-05-06 20:38:09',36,59,'1399408689837-service-59-36',1,1,1,NULL),(64,'2014-05-07 12:32:59',24,60,'1399465979260-service-60-24',1,1,1,NULL),(65,'2014-05-07 14:21:24',24,3,'1399472484095-service-3-24',1,0,1,NULL),(66,'2014-05-07 15:05:45',24,58,'1399475145618-service-58-24',1,1,1,NULL),(67,'2014-05-08 19:45:43',24,56,'1399578343805-service-56-24',1,1,1,NULL),(68,'2014-05-12 22:30:55',24,61,'1399933855357-service-61-24',1,1,1,NULL),(69,'2014-05-15 20:05:08',24,56,'1400184308148-service-56-24',1,0,0,NULL),(70,'2014-05-15 20:05:30',24,56,'1400184330453-service-56-24',1,0,0,NULL),(71,'2014-05-22 18:30:49',36,3,'1400783449865-service-3-36',1,0,1,NULL),(72,'2014-05-22 18:31:02',36,56,'1400783462146-service-56-36',1,0,1,NULL),(73,'2014-05-22 18:33:07',36,56,'1400783587302-service-56-36',1,0,1,NULL),(74,'2014-05-22 18:40:19',36,56,'1400784019615-service-56-36',1,1,1,NULL),(84,'2014-05-23 15:55:05',24,56,'1400860505968-service-56-24',1,0,1,NULL),(85,'2014-05-23 15:55:28',24,56,'1400860528868-service-56-24',1,0,1,NULL),(86,'2014-05-23 15:56:05',24,56,'1400860565664-service-56-24',1,0,1,NULL),(87,'2014-05-23 17:30:47',24,56,'1400866247485-service-56-24',1,1,1,NULL),(88,'2014-05-23 18:01:22',24,56,'1400868082846-service-56-24',1,0,1,NULL),(89,'2014-05-23 18:02:16',24,56,'1400868136345-service-56-24',1,0,1,NULL),(90,'2014-05-23 18:12:23',24,56,'1400868743046-service-56-24',1,0,1,NULL),(91,'2014-05-23 18:12:42',24,56,'1400868762445-service-56-24',1,1,1,NULL),(92,'2014-05-25 21:09:18',24,64,'1401052158755-service-64-24',1,0,1,NULL),(93,'2014-05-25 21:16:16',24,64,'1401052576006-service-64-24',1,1,1,NULL),(94,'2014-05-25 21:18:22',24,64,'1401052702206-service-64-24',1,1,1,'approved'),(95,'2014-05-26 18:23:03',24,64,'1401128583212-service-64-24',1,1,1,'request'),(96,'1970-01-01 00:00:00',36,64,'24-service-64-36',1,0,1,NULL);
/*!40000 ALTER TABLE `choiceNet_invoice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `choiceNet_session`
--

DROP TABLE IF EXISTS `choiceNet_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `choiceNet_session` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `session` int(11) NOT NULL,
  `user_id` int(11),
  `start_time` datetime NOT NULL,
  `end_time` datetime NOT NULL,
  `is_login` tinyint(1) NOT NULL,
  `a` int(11) NOT NULL,
  `q` int(11) NOT NULL,
  `key` varchar(128),
  PRIMARY KEY (`id`),
  KEY `choiceNet_session_6340c63c` (`user_id`),
  CONSTRAINT `user_id_refs_id_f3254fba` FOREIGN KEY (`user_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=166 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `choiceNet_session`
--

LOCK TABLES `choiceNet_session` WRITE;
/*!40000 ALTER TABLE `choiceNet_session` DISABLE KEYS */;
INSERT INTO `choiceNet_session` VALUES (1,0,24,'2014-04-30 17:38:36','2014-04-30 17:38:38',0,13,9,'0'),(88,98558682,24,'2014-05-01 03:22:54','2014-05-01 03:23:54',1,0,0,'37e84129692965ad730550d41020c9fb008301d6488f9596d1b6922740fd322b'),(89,64058967,24,'2014-05-01 03:23:44','2014-05-01 03:24:44',1,0,0,'db86ce46cdfa2264f9d622284b545ca151825142775136244f1793f1c9abddaa'),(90,97000628,24,'2014-05-01 03:24:01','2014-05-01 03:25:01',1,0,0,'3586c0ce5f880b1c67e1f1c8bce96860011676a1d2bad6bf9ede092ab6050a8f'),(91,259768,24,'2014-05-01 03:26:22','2014-05-01 03:27:22',1,0,0,'9f616cfee593b0c7c3cbfb340b6671813e8e5d8e7217ded0f4ada6668ea1325b'),(92,94930843,24,'2014-05-01 03:26:56','2014-05-01 03:27:56',1,0,0,'2f907e8a5d10eed9f977b92e607bea07d8ca99b76d9c219b28c6d13bce4ba53d'),(93,99042634,24,'2014-05-01 03:28:19','2014-05-01 03:29:19',1,0,0,'59f97b95ab152ef4b3b70eeeaea53ebb1c40881500f348a37080cc4639ee7002'),(94,0,NULL,'2014-05-01 03:30:22','2014-05-01 03:31:22',0,0,0,'e7d73f579f1e303be72b82356e3689a3a16b4056edc59d33454d5b978d17064b'),(95,40897624,24,'2014-05-01 03:30:40','2014-05-01 03:31:40',1,0,0,'e23fd82b13be81b92bc20c37b4aaa23afc0a50aa549569101bacc6c7f7e91093'),(96,63942634,24,'2014-05-01 03:30:58','2014-05-01 03:31:58',1,0,0,'8387f41e1b0682e08a96be25d5b8ba6e813dfd87563efb47581c17428b990db7'),(97,0,NULL,'2014-05-01 03:34:25','2014-05-01 03:35:25',0,0,0,'f3d3ec1bf99e87fa5d7a37c9b879798dc0003a992a9f84682db1f0603e3c6ac3'),(98,16558959,24,'2014-05-01 03:34:31','2014-05-01 03:35:31',1,0,0,'aab18970b0906a3f41058d81f6362a5098199135f167ca8a2c2b1d25ed994a6a'),(99,20336355,24,'2014-05-01 03:36:38','2014-05-01 03:37:38',1,0,0,'83b2d41d1da8ab9fff86a30f798c1b4a47c29f919a1bbc8654f55a8211690452'),(100,19134108,24,'2014-05-01 03:37:17','2014-05-01 03:38:17',1,0,0,'c5ac7ddca15f3ae04b9eb906ef3b15b739e76241a6a41c8ef969d2cf911d45c4'),(101,59301340,24,'2014-05-01 03:39:17','2014-05-01 03:40:17',1,0,0,'29c1501d42a8ea4a97f1ab1fe040e9667978367f49b39ffc1a02384bb64d5728'),(102,1698463,24,'2014-05-01 03:40:27','2014-05-01 03:40:27',1,0,0,'189f6900dfe570edcdd3a8cfb7feaf93326cb56b00c283e3325643bcfb805f73'),(103,0,NULL,'2014-05-01 12:49:00','2014-05-01 12:50:00',0,0,0,'0a29379c6c0f197e5caae0eca9e83a247f7ec8413e902270b8a22fbadc89914e'),(104,0,NULL,'2014-05-01 12:51:25','2014-05-01 12:52:25',0,0,0,'0b819a8bcb182dc5deba73416483678bc0376be30c1dfd4904388a1cf4613f5f'),(105,0,NULL,'2014-05-01 12:51:32','2014-05-01 12:52:32',0,0,0,'c3f031ca02b1875209e23758fcc8cbcf0a86a2b8e74ab13cf959b841d5792af6'),(106,60277103,24,'2014-05-01 12:52:32','2014-05-01 12:53:32',1,0,0,'fd811691aaa2ded7c5c8893bf3541df2a017e5b20c76c6c4b1a8c1976e4a91ac'),(107,87825661,24,'2014-05-01 13:15:54','2014-05-01 13:16:54',1,0,0,'f28848734b36a3cfc4e719c97b96c3e34c4325cbfd6e17760d099344396a487c'),(108,0,NULL,'2014-05-01 13:16:17','2014-05-01 13:17:17',0,0,0,'0deefc9af54ad923b5d2ee47b89dbe965970d166d2b0ae781f7390e612432aaa'),(109,0,NULL,'2014-05-01 13:18:38','2014-05-01 13:19:38',0,0,0,'ba7dbd9a60e26b967e284eef41412c788f8d97ac1a7aea6cd322febf6d9a1a88'),(110,0,NULL,'2014-05-01 13:19:42','2014-05-01 13:20:42',0,0,0,'7215ebd3d7ef23ea345b14299c4a40d9749d9ea84f93bcbcd9557d47c8eb839f'),(111,96565080,24,'2014-05-01 14:27:48','2014-05-01 14:28:48',1,0,0,'fd8f8e696449c80d5db31c5309744fee454660eb128e9805c1d2f902a29f565d'),(112,0,NULL,'2014-05-01 14:30:26','2014-05-01 14:31:26',0,0,0,'71687f727fe4eb542ae10c1d455fb794ce1e2e71046059c25ca6db3a917ec68d'),(113,22799320,24,'2014-05-01 14:31:04','2014-05-01 14:32:04',1,0,0,'009766dfc02f28b7b22ce6ad11a9d331a864794b4a8ecb6a2aea3331072e1a3a'),(114,98386100,24,'2014-05-01 14:32:45','2014-05-01 14:33:45',1,0,0,'74d6e7bb4e10738b51100b631006123e5608882167457b12cdbef8298aa72f59'),(115,16479233,24,'2014-05-01 14:33:56','2014-05-01 14:34:56',1,0,0,'dbea857bb23c5dbb90be7e4fac46521f09cc15afb349061b922dcc591804f078'),(116,59732877,24,'2014-05-01 14:36:41','2014-05-01 14:37:41',1,0,0,'453e6ca0ee62b38becb1ed83c13ce9a256c9fd1a39a1d8bc413e5958c5c8277d'),(117,62009816,24,'2014-05-01 14:38:16','2014-05-01 14:39:16',1,0,0,'d54cd35ce29150dc7bb0ef155e1b1a5ce47e7791eb2080b0f3fb5f3482f2eabe'),(118,63541323,24,'2014-05-01 14:39:44','2014-05-01 14:40:44',1,0,0,'9ec121eaad73263cb20a7809b2de805c45bef5e895a7df8946e2b61d72662c5c'),(119,18827662,24,'2014-05-01 14:40:11','2014-05-01 14:41:11',1,0,0,'1289c4df7966d29a31b8e2f3450d98ef391abbd33d2b057c4fd852fe34ce4dd9'),(120,67535592,24,'2014-05-01 15:02:51','2014-05-01 15:03:51',1,0,0,'88276d589fd8485393a8fef072598faa04317d3b66228804ea85444283276a0e'),(121,88687741,24,'2014-05-01 15:03:32','2014-05-01 15:04:32',1,0,0,'5e49f887069f12996c1a00a087c121edd84f6d30bbd7a142f8bdeb7b8ab3ea1d'),(122,93145193,24,'2014-05-01 15:14:59','2014-05-01 15:15:59',1,0,0,'e26a632391c4bcab8444153479f5bc64aba492ed83368004974b55cf24b8fbea'),(123,29136119,24,'2014-05-01 15:18:37','2014-05-01 15:19:37',1,0,0,'559fb67889c2b2e662cfb4031903dfbec6a782f9bdfccb52f25f1677c2e88b88'),(124,22343164,24,'2014-05-01 15:19:44','2014-05-01 15:20:44',1,0,0,'4c2007ef3d24574c170248a283b565cf4f5f24ce9418d3c65e7b2f049aa3c86e'),(125,30249044,24,'2014-05-01 15:20:11','2014-05-01 15:21:11',1,0,0,'43c37fdbd1fe8d24d469149316b611a5deda2752e0674f24a95a676519f91069'),(126,61386724,24,'2014-05-01 15:22:20','2014-05-01 15:23:20',1,0,0,'e4493e07ea442ae235f18ba4649fc7e2d5cd07294d6a665415aa798c003e1bcc'),(127,11368866,24,'2014-05-01 15:23:32','2014-05-01 15:24:32',1,0,0,'7491a4bcff0f5ca2f342a3e5341af1ead638b876db10bd584447915fe0662472'),(128,74113618,24,'2014-05-01 15:24:19','2014-05-01 15:25:19',1,0,0,'0d0c7b367e3b4a22fe6532e84313c4b232b83c0b842ba988de1bc56504906fe0'),(129,87072990,24,'2014-05-01 15:25:02','2014-05-01 15:26:02',1,0,0,'0cfbf75a2f32917e5cc7606f30941524ecd6074b8159e3ed29d54b406425f438'),(130,2707037,24,'2014-05-06 19:50:53','2014-05-06 19:51:53',1,0,0,'5f1d0e2c94a48b7417abee2dad6b3583b379e3253ab7ec6d6ca27fcff49faf7d'),(131,0,NULL,'2014-05-15 20:01:47','2014-05-15 20:07:47',0,0,0,'a97f13c4b35ee4866049c0b4d01fe825d5a2e22ec9bcb758a2481d451f69b01c'),(132,0,NULL,'2014-05-15 20:02:22','2014-05-15 20:08:22',0,0,0,'e6ac14e77bb3f633bdfac647422bea1cb87c09b67014fdd4cd98f1f26d1f3409'),(133,0,NULL,'2014-05-15 20:02:38','2014-05-15 20:08:38',0,0,0,'cd64577bb3545f6caf61d9ab37f3a7a5d2c5e7b7d7773f684e77ac34246ea64f'),(134,20161024,24,'2014-05-15 20:03:51','2014-05-15 20:09:51',1,0,0,'b169971ca41881019f05248f4ac5e5da137e52510fbdd9c1ecc848053cea93dc'),(135,43688999,24,'2014-05-15 20:05:06','2014-05-15 20:11:06',1,0,0,'534dee01255f3afe885cd903a44e71a975cd6a4223733529be2bb36894b96947'),(136,94614787,24,'2014-05-15 20:05:29','2014-05-15 20:11:29',1,0,0,'c7cb8acd623e83bbcae0b4108880ae3a16fa3c8e34e5b56b6eff3f3d49b3f11d'),(137,0,NULL,'2014-05-23 15:12:13','2014-05-23 15:18:13',0,0,0,'76bb31feaf64fd5b256093effac623b9b1284599322e4272b143be0a488579f0'),(138,76712193,24,'2014-05-23 15:13:14','2014-05-23 15:19:14',1,0,0,'0351781c523ba19ce3b427dad63c5f69bb0563da98cb6b1aa96611c3d63e012b'),(139,27081126,24,'2014-05-23 15:31:12','2014-05-23 15:37:12',1,0,0,'eec3c6bd4562ca0de654ff4e7caebdc365256a51db804819bbf7ce5f2d0e4520'),(140,96856235,24,'2014-05-23 15:32:10','2014-05-23 15:38:10',1,0,0,'9f2157f7e2681e07059309471dacd10407e1f5e1e2e56126979f91cb54716ad8'),(141,11215784,24,'2014-05-23 15:34:44','2014-05-23 15:40:44',1,0,0,'a3f060b87f73fd6d1f96a2e61a5e70e9a58202dd7f1c4271278cca5f432358db'),(142,19146046,24,'2014-05-23 15:36:20','2014-05-23 15:42:20',1,0,0,'40f9896cf312e4db38a0870078b283e237d042ac69e9e438adb4e8b7d8dc4b9f'),(143,94609456,24,'2014-05-23 15:38:18','2014-05-23 15:44:18',1,0,0,'a3a86279a6a577094bb744fa00f888b6860111c8eabf124a7e7ecbef1d2c9a47'),(144,31915079,24,'2014-05-23 15:40:34','2014-05-23 15:46:34',1,0,0,'15250f41953b32527e0a835a9e43b3020bb75f2dcccbca61bb40274595b760ce'),(145,6217143,24,'2014-05-23 15:41:09','2014-05-23 15:47:09',1,0,0,'3b8756112b483f5d2bf8b065b5d40714cd67049fbec5bab6a3bf771e3f78879f'),(146,47715843,24,'2014-05-23 15:42:12','2014-05-23 15:48:12',1,0,0,'5bd6fd638255477eb2cfc501e9cacda633e62fc6ac3cea9f05ff1c216da4ba0c'),(147,85515139,24,'2014-05-23 15:42:41','2014-05-23 15:48:41',1,0,0,'6bb03fa6419b5429019e55aa673097b1aa4fd2b92b08c71ecb2d4c0867a067f2'),(148,61263211,24,'2014-05-23 15:43:29','2014-05-23 15:49:29',1,0,0,'328484406b5a807723e0679a3eebad373ac54727414b3b7d3bbfe0c37946a5e9'),(149,24686868,24,'2014-05-23 15:45:06','2014-05-23 15:51:06',1,0,0,'d8e8a6f08ae500d3a15007f343e41c5ed92ad32330ad68c8e412abb86180f7a5'),(150,56351759,24,'2014-05-23 15:46:51','2014-05-23 15:52:51',1,0,0,'783c7a8a7496fafc990a7714c97d83fb7a01da3506d481b85068c9547629f997'),(151,11319569,24,'2014-05-23 15:47:21','2014-05-23 15:53:21',1,0,0,'835f6e7e5ce42d292e21d3ec5a480da1de5f2710071a91961ae8e23851809eb8'),(152,40375126,24,'2014-05-23 15:49:50','2014-05-23 15:55:50',1,0,0,'96cfa155437fd9205ef8062c070ac5e822ecde086997d0661642258956315c06'),(153,49881121,24,'2014-05-23 15:55:04','2014-05-23 16:01:04',1,0,0,'3c56947b597c9aff398e5cbdb1128b2dbb77a03a4f3ac922fe0ebc6970b93eea'),(154,17718603,24,'2014-05-23 15:55:27','2014-05-23 16:01:27',1,0,0,'a15b9bd390827f0f9b53984e29075b13e272058ce36852251c75d7eed83a8618'),(155,40275323,24,'2014-05-23 15:56:04','2014-05-23 16:02:04',1,0,0,'c9af58f23034e8c3da5a8328ef5c1818611cf1022fab36d227797b0e13ca0fd1'),(156,0,NULL,'2014-05-23 17:30:33','2014-05-23 17:36:33',0,0,0,'97ef51a75d28e4e6231a48b8af73f5e9b42ca77d8b6655d99f54ffe1ffdb64a1'),(157,89261012,24,'2014-05-23 17:30:46','2014-05-23 17:36:46',1,0,0,'e2dd150b99524704500aa8e4a95b02fd5d4cf68d7dc7c8ce386c57f67b4e73a4'),(158,76193937,24,'2014-05-23 18:01:21','2014-05-23 18:07:21',1,0,0,'c918a4324efddc6b026ec1efd7a67dd2e121e4875e56710c5d0c6cd0c56268d0'),(159,22502117,24,'2014-05-23 18:02:14','2014-05-23 18:08:14',1,0,0,'f08b672cd6fed38a32de656bd8a328daba1c65f4dbc4167fe70e2e0b61374635'),(160,21790941,24,'2014-05-23 18:12:21','2014-05-23 18:18:21',1,0,0,'ce90b0ea89e7ffd93cd8b3fe9b0e0cd32b85c83bd4dc0356011a8deb37dfa91d'),(161,29209883,24,'2014-05-23 18:12:41','2014-05-23 18:18:41',1,0,0,'240f7750cfe63cc3b105ef3c3524858c30f09481d7769d1e92c61e3c3fd30a87'),(162,34152322,24,'2014-05-25 21:09:17','2014-05-25 21:15:17',1,0,0,'969784260a5f26e8ffa737ea45ad5f0e955662d04d46f01976c16e2c0b07b128'),(163,28843840,24,'2014-05-25 21:16:14','2014-05-25 21:22:14',1,0,0,'afb87e6b4ac1b296da4b39a00ff448cbb54fd799fc495bcf046da1a505328ed3'),(164,31687896,24,'2014-05-25 21:18:20','2014-05-25 21:24:20',1,0,0,'8a89e062e8bfabc174dbb5e8b250829658a5827af07ba0d1db82ee7599c31524'),(165,27177386,24,'2014-05-26 18:23:01','2014-05-26 18:29:01',1,0,0,'7a7803f9884cc4dfcff4a9dd19a31623bb5f26d763521c1ff77dac56c8abb9ef');
/*!40000 ALTER TABLE `choiceNet_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=283 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (3,'2013-09-18 21:05:07',2,10,'9','test, test1',3,''),(4,'2013-09-18 21:05:07',2,10,'11','test, test2',3,''),(5,'2013-09-18 21:05:07',2,10,'12','test, test3',3,''),(6,'2013-09-18 21:05:07',2,10,'13','test, test4',3,''),(7,'2013-09-18 21:05:07',2,10,'6','test, test',3,''),(8,'2013-09-18 21:05:07',2,10,'14','test, test5',3,''),(9,'2013-09-20 20:45:40',2,10,'15','test, test',2,'Changed first_name and last_name.'),(10,'2013-09-20 21:01:48',2,10,'15','test, test',3,''),(11,'2013-09-20 21:06:37',2,10,'19','test, test',3,''),(12,'2013-09-20 21:18:29',2,10,'20','test, test',3,''),(13,'2013-09-20 21:23:28',2,10,'21','test, test',3,''),(14,'2013-09-21 02:08:32',2,10,'16','test, test2`',3,''),(15,'2013-09-21 02:08:32',2,10,'17','test, test3',3,''),(16,'2013-09-21 02:08:32',2,10,'18','test, test4',3,''),(17,'2013-09-21 02:08:32',2,10,'23','test, test5',3,''),(18,'2013-10-31 22:03:21',2,11,'1','Service object',1,''),(19,'2013-10-31 22:04:11',2,12,'1','ServiceType object',1,''),(20,'2013-10-31 22:04:31',2,12,'2','ServiceType object',1,''),(21,'2013-10-31 22:04:44',2,12,'3','ServiceType object',1,''),(22,'2013-10-31 22:04:57',2,12,'4','ServiceType object',1,''),(23,'2013-10-31 22:05:07',2,12,'5','ServiceType object',1,''),(24,'2013-10-31 22:05:22',2,12,'6','ServiceType object',1,''),(25,'2013-10-31 22:05:33',2,12,'7','ServiceType object',1,''),(26,'2013-10-31 22:05:44',2,12,'8','ServiceType object',1,''),(27,'2013-10-31 22:06:38',2,11,'1','Service object',2,'Changed service_type.'),(28,'2013-11-01 15:12:50',2,11,'2','Service object',1,''),(29,'2013-11-01 15:16:51',2,11,'3','Service object',1,''),(30,'2013-11-20 01:06:36',2,11,'4','Service object',1,''),(31,'2013-11-20 01:07:42',2,11,'5','Service object',1,''),(32,'2013-11-20 01:09:02',2,11,'6','Service object',1,''),(33,'2013-11-20 01:10:30',2,11,'7','Service object',1,''),(34,'2013-11-20 15:24:32',2,11,'8','Service object',1,''),(35,'2013-11-20 15:26:09',2,11,'9','Service object',1,''),(36,'2013-11-20 15:26:46',2,11,'10','Service object',1,''),(37,'2013-11-20 15:29:21',2,11,'11','Service object',1,''),(38,'2013-11-20 15:30:02',2,11,'12','Service object',1,''),(39,'2013-11-20 15:30:40',2,11,'13','Service object',1,''),(40,'2013-11-20 15:31:21',2,11,'14','Service object',1,''),(41,'2013-11-20 15:33:10',2,11,'15','Service object',1,''),(42,'2013-11-20 15:33:45',2,11,'16','Service object',1,''),(43,'2013-11-20 15:34:31',2,11,'17','Service object',1,''),(44,'2013-11-20 15:35:18',2,11,'18','Service object',1,''),(45,'2013-11-20 15:36:03',2,11,'19','Service object',1,''),(46,'2013-11-20 15:36:49',2,11,'20','Service object',1,''),(47,'2013-11-20 15:37:33',2,11,'21','Service object',1,''),(48,'2013-11-20 15:38:15',2,11,'22','Service object',1,''),(49,'2013-11-20 15:38:56',2,11,'23','Service object',1,''),(50,'2013-11-20 15:39:35',2,11,'24','Service object',1,''),(51,'2013-11-20 15:40:11',2,11,'25','Service object',1,''),(52,'2013-11-20 15:40:49',2,11,'26','Service object',1,''),(53,'2013-11-20 15:41:32',2,11,'27','Service object',1,''),(54,'2013-11-20 15:42:09',2,11,'28','Service object',1,''),(55,'2013-11-20 21:21:16',2,11,'29','Service object',1,''),(56,'2013-11-20 21:21:52',2,11,'30','Service object',1,''),(57,'2013-11-20 21:22:33',2,11,'31','Service object',1,''),(58,'2013-11-20 21:23:12',2,11,'32','Service object',1,''),(59,'2013-11-20 21:23:48',2,11,'33','Service object',1,''),(60,'2013-11-20 21:24:24',2,11,'34','Service object',1,''),(61,'2013-11-20 21:25:04',2,11,'35','Service object',1,''),(62,'2013-11-20 21:30:58',2,11,'36','Service object',1,''),(63,'2013-11-20 21:31:33',2,11,'37','Service object',1,''),(64,'2013-11-20 21:32:58',2,11,'38','Service object',1,''),(65,'2013-11-20 21:33:37',2,11,'39','Service object',1,''),(66,'2013-11-20 21:34:22',2,11,'40','Service object',1,''),(67,'2013-11-20 21:34:59',2,11,'41','Service object',1,''),(68,'2013-11-20 21:35:30',2,11,'42','Service object',1,''),(69,'2013-11-20 21:36:01',2,11,'43','Service object',1,''),(70,'2013-11-20 21:36:30',2,11,'44','Service object',1,''),(71,'2013-11-20 21:37:02',2,11,'45','Service object',1,''),(72,'2013-11-20 21:37:29',2,11,'46','Service object',1,''),(73,'2013-11-20 21:38:08',2,11,'47','Service object',1,''),(74,'2013-11-20 21:38:45',2,11,'48','Service object',1,''),(75,'2013-11-20 21:39:19',2,11,'49','Service object',1,''),(76,'2013-11-20 21:39:47',2,11,'50','Service object',1,''),(77,'2013-11-20 21:40:17',2,11,'51','Service object',1,''),(78,'2013-11-20 21:40:49',2,11,'52','Service object',1,''),(79,'2013-11-23 16:17:46',2,11,'53','Long name service long long long long long long long long',1,''),(80,'2013-11-23 16:51:42',2,11,'54','This is for testing null field',1,''),(81,'2013-11-23 17:18:22',2,11,'6','Compressing Service',2,'Changed picture.'),(82,'2013-11-23 17:31:20',2,11,'6','Compressing Service',2,'Changed picture.'),(83,'2013-11-23 17:32:25',2,11,'6','Compressing Service',2,'Changed picture.'),(84,'2013-11-23 17:50:30',2,11,'6','Compressing Service',2,'Changed picture.'),(85,'2013-11-23 18:08:07',2,10,'28','staff, staff',1,''),(86,'2013-11-23 18:29:53',2,10,'30','test, test51',1,''),(87,'2013-11-23 18:32:51',2,10,'28','staff, staff',3,''),(88,'2013-11-23 18:32:51',2,10,'30','test, test51',3,''),(89,'2013-11-23 18:55:06',2,10,'31','staff, staff002',1,''),(90,'2013-11-23 18:56:35',2,10,'32','staff, staff003',1,''),(91,'2013-11-23 18:57:28',2,10,'33','staff, staff004',1,''),(92,'2013-11-23 19:05:44',2,11,'3','Cheaper',2,'Changed owner.'),(93,'2013-11-23 19:05:52',2,11,'20','Test Service 12',2,'Changed owner.'),(94,'2013-11-23 20:01:38',2,11,'53','Long name service long long long long long long long long',2,'Changed description.'),(95,'2013-11-23 20:11:16',2,11,'8','Test Service 1',2,'Changed picture.'),(96,'2013-11-24 04:33:23',2,13,'1','1385266312359-service-6-2',2,'Changed number.'),(97,'2014-04-29 18:57:45',2,11,'56','Balance',1,''),(98,'2014-04-29 20:28:04',2,14,'1','Qi, Yunsheng',1,''),(99,'2014-04-29 23:30:01',2,11,'56','Add Balance',2,'Changed name.'),(100,'2014-04-30 17:38:47',2,15,'1','Qi, Yunsheng',1,''),(101,'2014-04-30 19:33:48',2,15,'2','None',1,''),(102,'2014-05-01 03:39:52',2,15,'2','None',3,''),(103,'2014-05-01 03:39:52',2,15,'3','None',3,''),(104,'2014-05-01 03:39:52',2,15,'4','None',3,''),(105,'2014-05-01 03:39:52',2,15,'5','None',3,''),(106,'2014-05-01 03:39:52',2,15,'6','None',3,''),(107,'2014-05-01 03:39:52',2,15,'7','None',3,''),(108,'2014-05-01 03:39:52',2,15,'8','None',3,''),(109,'2014-05-01 03:39:52',2,15,'9','None',3,''),(110,'2014-05-01 03:39:52',2,15,'10','None',3,''),(111,'2014-05-01 03:39:52',2,15,'11','None',3,''),(112,'2014-05-01 03:39:52',2,15,'12','None',3,''),(113,'2014-05-01 03:39:52',2,15,'13','None',3,''),(114,'2014-05-01 03:39:52',2,15,'14','None',3,''),(115,'2014-05-01 03:39:52',2,15,'15','None',3,''),(116,'2014-05-01 03:39:52',2,15,'16','None',3,''),(117,'2014-05-01 03:39:52',2,15,'17','None',3,''),(118,'2014-05-01 03:39:52',2,15,'18','None',3,''),(119,'2014-05-01 03:39:52',2,15,'19','None',3,''),(120,'2014-05-01 03:39:52',2,15,'20','None',3,''),(121,'2014-05-01 03:39:52',2,15,'21','None',3,''),(122,'2014-05-01 03:39:52',2,15,'22','None',3,''),(123,'2014-05-01 03:39:52',2,15,'23','None',3,''),(124,'2014-05-01 03:39:52',2,15,'24','None',3,''),(125,'2014-05-01 03:39:52',2,15,'25','None',3,''),(126,'2014-05-01 03:39:52',2,15,'26','None',3,''),(127,'2014-05-01 03:39:52',2,15,'27','None',3,''),(128,'2014-05-01 03:39:52',2,15,'28','None',3,''),(129,'2014-05-01 03:39:52',2,15,'29','None',3,''),(130,'2014-05-01 03:39:52',2,15,'30','None',3,''),(131,'2014-05-01 03:39:52',2,15,'31','None',3,''),(132,'2014-05-01 03:39:52',2,15,'32','None',3,''),(133,'2014-05-01 03:39:52',2,15,'33','None',3,''),(134,'2014-05-01 03:39:52',2,15,'34','None',3,''),(135,'2014-05-01 03:39:52',2,15,'35','None',3,''),(136,'2014-05-01 03:39:52',2,15,'36','None',3,''),(137,'2014-05-01 03:39:52',2,15,'37','None',3,''),(138,'2014-05-01 03:39:52',2,15,'38','None',3,''),(139,'2014-05-01 03:39:52',2,15,'39','None',3,''),(140,'2014-05-01 03:39:52',2,15,'40','None',3,''),(141,'2014-05-01 03:39:52',2,15,'41','None',3,''),(142,'2014-05-01 03:39:52',2,15,'42','None',3,''),(143,'2014-05-01 03:39:52',2,15,'43','None',3,''),(144,'2014-05-01 03:39:52',2,15,'44','None',3,''),(145,'2014-05-01 03:39:52',2,15,'45','None',3,''),(146,'2014-05-01 03:39:52',2,15,'46','None',3,''),(147,'2014-05-01 03:39:52',2,15,'47','None',3,''),(148,'2014-05-01 03:39:52',2,15,'48','None',3,''),(149,'2014-05-01 03:39:52',2,15,'49','None',3,''),(150,'2014-05-01 03:39:52',2,15,'50','None',3,''),(151,'2014-05-01 03:39:52',2,15,'51','None',3,''),(152,'2014-05-01 03:39:52',2,15,'52','None',3,''),(153,'2014-05-01 03:39:52',2,15,'53','None',3,''),(154,'2014-05-01 03:39:52',2,15,'54','None',3,''),(155,'2014-05-01 03:39:52',2,15,'55','None',3,''),(156,'2014-05-01 03:39:52',2,15,'56','None',3,''),(157,'2014-05-01 03:39:52',2,15,'57','None',3,''),(158,'2014-05-01 03:39:52',2,15,'58','None',3,''),(159,'2014-05-01 03:39:52',2,15,'59','None',3,''),(160,'2014-05-01 03:39:52',2,15,'60','None',3,''),(161,'2014-05-01 03:39:52',2,15,'61','None',3,''),(162,'2014-05-01 03:39:52',2,15,'62','None',3,''),(163,'2014-05-01 03:39:52',2,15,'63','None',3,''),(164,'2014-05-01 03:39:52',2,15,'64','None',3,''),(165,'2014-05-01 03:39:52',2,15,'65','None',3,''),(166,'2014-05-01 03:39:52',2,15,'66','None',3,''),(167,'2014-05-01 03:39:52',2,15,'67','None',3,''),(168,'2014-05-01 03:39:52',2,15,'68','None',3,''),(169,'2014-05-01 03:39:52',2,15,'69','None',3,''),(170,'2014-05-01 03:39:52',2,15,'70','None',3,''),(171,'2014-05-01 03:39:52',2,15,'71','None',3,''),(172,'2014-05-01 03:39:52',2,15,'72','None',3,''),(173,'2014-05-01 03:39:52',2,15,'73','None',3,''),(174,'2014-05-01 03:39:52',2,15,'74','None',3,''),(175,'2014-05-01 03:39:52',2,15,'75','None',3,''),(176,'2014-05-01 03:39:52',2,15,'76','None',3,''),(177,'2014-05-01 03:39:52',2,15,'77','None',3,''),(178,'2014-05-01 03:39:52',2,15,'78','None',3,''),(179,'2014-05-01 03:39:52',2,15,'79','None',3,''),(180,'2014-05-01 03:39:52',2,15,'80','None',3,''),(181,'2014-05-01 03:39:52',2,15,'81','None',3,''),(182,'2014-05-01 03:39:52',2,15,'82','None',3,''),(183,'2014-05-01 03:39:52',2,15,'83','None',3,''),(184,'2014-05-01 03:39:52',2,15,'84','None',3,''),(185,'2014-05-01 03:39:52',2,15,'85','None',3,''),(186,'2014-05-01 03:39:52',2,15,'86','None',3,''),(187,'2014-05-01 03:39:52',2,15,'87','None',3,''),(188,'2014-05-06 16:11:29',2,11,'3','Cheaper',2,'Changed service_bandwidth, service_latency and service_cost.'),(189,'2014-05-06 16:24:06',2,11,'57','Service 1',1,''),(190,'2014-05-06 16:52:48',2,11,'58','Service 2',1,''),(191,'2014-05-06 18:43:48',2,11,'56','Add Balance',2,'Changed service_id and service_cost.'),(192,'2014-05-06 18:46:42',2,11,'59','Service 3',1,''),(193,'2014-05-06 18:48:30',2,11,'60','Service 4',1,''),(194,'2014-05-06 18:48:48',2,11,'57','Service 1',2,'Changed end_point2_ip.'),(195,'2014-05-06 18:49:12',2,11,'56','Add Balance',2,'No fields changed.'),(196,'2014-05-06 18:49:44',2,11,'56','Add Balance',2,'Changed service_bandwidth and service_latency.'),(197,'2014-05-06 18:50:02',2,11,'6','Compressing Service',2,'Changed service_bandwidth, service_latency and service_cost.'),(198,'2014-05-06 18:51:07',2,11,'7','Decompressing',2,'Changed service_bandwidth, service_latency and service_cost.'),(199,'2014-05-06 18:51:25',2,11,'5','Decryption Service',2,'Changed service_bandwidth, service_latency and service_cost.'),(200,'2014-05-06 18:52:14',2,11,'4','Encryption Service',2,'Changed service_bandwidth, service_latency and service_cost.'),(201,'2014-05-06 18:52:54',2,11,'2','Expensive Service',2,'Changed service_bandwidth, service_latency and service_cost.'),(202,'2014-05-06 18:53:10',2,11,'53','Long name service long long long long long long long long',2,'Changed service_bandwidth, service_latency and service_cost.'),(203,'2014-05-06 18:53:53',2,11,'1','Testing Service',2,'Changed service_bandwidth, service_latency and service_cost.'),(204,'2014-05-06 19:06:01',2,11,'8','Test Service 1',2,'Changed service_bandwidth, service_latency and service_cost.'),(205,'2014-05-06 19:06:21',2,11,'18','Test Service 10',2,'Changed service_bandwidth, service_latency and service_cost.'),(206,'2014-05-06 19:11:17',2,11,'19','Test Service 11',2,'Changed service_bandwidth, service_latency and service_cost.'),(207,'2014-05-06 19:11:35',2,11,'20','Test Service 12',2,'Changed service_bandwidth, service_latency and service_cost.'),(208,'2014-05-06 19:12:04',2,11,'21','Test Service 13',2,'Changed service_bandwidth, service_latency and service_cost.'),(209,'2014-05-06 19:12:18',2,11,'22','Test Service 14',2,'Changed service_bandwidth, service_latency and service_cost.'),(210,'2014-05-06 19:12:37',2,11,'23','Test Service 15',2,'Changed service_bandwidth, service_latency and service_cost.'),(211,'2014-05-06 19:12:48',2,11,'24','Test Service 16',2,'Changed service_bandwidth, service_latency and service_cost.'),(212,'2014-05-06 19:13:00',2,11,'25','Test Service 17',2,'Changed service_bandwidth, service_latency and service_cost.'),(213,'2014-05-06 19:13:12',2,11,'26','Test Service 18',2,'Changed service_bandwidth, service_latency and service_cost.'),(214,'2014-05-06 19:13:25',2,11,'27','Test Service 19',2,'Changed service_bandwidth, service_latency and service_cost.'),(215,'2014-05-06 19:13:54',2,11,'10','Test Service 2',2,'Changed service_bandwidth, service_latency and service_cost.'),(216,'2014-05-06 19:14:11',2,11,'9','Test Service 2',2,'Changed service_bandwidth, service_latency and service_cost.'),(217,'2014-05-06 19:14:37',2,11,'28','Test Service 20',2,'Changed service_bandwidth, service_latency and service_cost.'),(218,'2014-05-06 19:14:47',2,11,'29','Test Service 21',2,'Changed service_bandwidth, service_latency and service_cost.'),(219,'2014-05-06 19:15:01',2,11,'30','Test Service 22',2,'Changed service_bandwidth, service_latency and service_cost.'),(220,'2014-05-06 19:15:12',2,11,'31','Test Service 23',2,'Changed service_bandwidth, service_latency and service_cost.'),(221,'2014-05-06 19:15:27',2,11,'32','Test Service 24',2,'Changed service_bandwidth, service_latency and service_cost.'),(222,'2014-05-06 19:15:42',2,11,'33','Test Service 25',2,'Changed service_bandwidth, service_latency and service_cost.'),(223,'2014-05-06 19:15:56',2,11,'34','Test Service 26',2,'Changed service_bandwidth, service_latency and service_cost.'),(224,'2014-05-06 19:16:09',2,11,'35','Test Service 27',2,'Changed service_bandwidth, service_latency and service_cost.'),(225,'2014-05-06 19:16:23',2,11,'36','Test Service 28',2,'Changed service_bandwidth, service_latency and service_cost.'),(226,'2014-05-06 19:16:36',2,11,'37','Test Service 29',2,'Changed service_bandwidth, service_latency and service_cost.'),(227,'2014-05-06 19:16:49',2,11,'11','Test Service 3',2,'Changed service_bandwidth, service_latency and service_cost.'),(228,'2014-05-06 19:17:02',2,11,'38','Test Service 30',2,'Changed service_bandwidth, service_latency and service_cost.'),(229,'2014-05-06 19:17:17',2,11,'17','Test Service 9',2,'Changed service_bandwidth, service_latency and service_cost.'),(230,'2014-05-06 19:17:35',2,11,'39','Test Service 31',2,'Changed service_bandwidth, service_latency and service_cost.'),(231,'2014-05-06 19:17:50',2,11,'40','Test Service 32',2,'Changed service_bandwidth, service_latency and service_cost.'),(232,'2014-05-06 19:18:03',2,11,'41','Test Service 33',2,'Changed service_bandwidth, service_latency and service_cost.'),(233,'2014-05-06 19:18:17',2,11,'42','Test Service 34',2,'Changed service_bandwidth, service_latency and service_cost.'),(234,'2014-05-06 19:18:32',2,11,'43','Test Service 35',2,'Changed service_bandwidth, service_latency and service_cost.'),(235,'2014-05-06 19:18:48',2,11,'44','Test Service 36',2,'Changed service_bandwidth, service_latency and service_cost.'),(236,'2014-05-06 19:19:01',2,11,'45','Test Service 37',2,'Changed service_bandwidth, service_latency and service_cost.'),(237,'2014-05-06 19:19:14',2,11,'46','Test Service 38',2,'Changed service_bandwidth, service_latency and service_cost.'),(238,'2014-05-06 19:19:28',2,11,'47','Test Service 39',2,'Changed service_bandwidth, service_latency and service_cost.'),(239,'2014-05-06 19:19:46',2,11,'12','Test Service 4',2,'Changed service_bandwidth, service_latency and service_cost.'),(240,'2014-05-06 19:20:01',2,11,'48','Test Service 40',2,'Changed service_bandwidth, service_latency and service_cost.'),(241,'2014-05-06 19:20:20',2,11,'49','Test Service 41',2,'Changed service_bandwidth, service_latency and service_cost.'),(242,'2014-05-06 19:20:33',2,11,'50','Test Service 42',2,'Changed service_bandwidth, service_latency and service_cost.'),(243,'2014-05-06 19:20:45',2,11,'51','Test Service 43',2,'Changed service_bandwidth, service_latency and service_cost.'),(244,'2014-05-06 19:20:59',2,11,'52','Test Service 44',2,'Changed service_bandwidth, service_latency and service_cost.'),(245,'2014-05-06 19:21:14',2,11,'13','Test Service 5',2,'Changed service_bandwidth, service_latency and service_cost.'),(246,'2014-05-06 19:21:37',2,11,'14','Test Service 6',2,'Changed service_bandwidth, service_latency and service_cost.'),(247,'2014-05-06 19:21:49',2,11,'15','Test Service 7',2,'Changed service_bandwidth, service_latency and service_cost.'),(248,'2014-05-06 19:22:01',2,11,'55','Test Service 7000',2,'Changed service_bandwidth, service_latency and service_cost.'),(249,'2014-05-06 19:22:14',2,11,'16','Test Service 8',2,'Changed service_bandwidth, service_latency and service_cost.'),(250,'2014-05-06 19:25:40',2,11,'61','Service 5',1,''),(251,'2014-05-06 19:25:54',2,11,'61','Service 5',2,'Changed owner.'),(252,'2014-05-06 19:29:58',2,11,'62','Service 6',1,''),(253,'2014-05-06 19:30:54',2,11,'62','Service 6',2,'Changed owner.'),(254,'2014-05-06 19:33:22',2,11,'63','Service 7',1,''),(255,'2014-05-06 19:35:01',2,11,'64','Service 8',1,''),(256,'2014-05-06 19:35:11',2,11,'64','Service 8',2,'Changed owner.'),(257,'2014-05-06 20:09:22',2,10,'36','Provider, Provider',2,'Changed is_staff.'),(258,'2014-05-06 20:17:20',2,11,'3','Cheaper',2,'Changed owner.'),(259,'2014-05-06 20:17:35',2,11,'20','Test Service 12',2,'Changed owner.'),(260,'2014-05-06 20:17:44',2,11,'57','Service 1',2,'Changed owner.'),(261,'2014-05-06 20:17:55',2,11,'58','Service 2',2,'Changed owner.'),(262,'2014-05-06 20:18:05',2,11,'59','Service 3',2,'Changed owner.'),(263,'2014-05-06 20:18:16',2,11,'60','Service 4',2,'Changed owner.'),(264,'2014-05-06 20:18:27',2,11,'61','Service 5',2,'Changed owner.'),(265,'2014-05-06 20:18:38',2,11,'62','Service 6',2,'Changed owner.'),(266,'2014-05-06 20:18:47',2,11,'63','Service 7',2,'Changed owner.'),(267,'2014-05-06 20:18:57',2,11,'64','Service 8',2,'Changed owner.'),(268,'2014-05-07 12:47:47',2,16,'1','Qi, Yunsheng',1,''),(269,'2014-05-23 15:57:00',2,13,'83','1400860192366-service-56-24',3,''),(270,'2014-05-23 15:57:00',2,13,'82','1400860042567-service-56-24',3,''),(271,'2014-05-23 15:57:00',2,13,'81','1400860012465-service-56-24',3,''),(272,'2014-05-23 15:57:00',2,13,'80','1400859907765-service-56-24',3,''),(273,'2014-05-23 15:57:00',2,13,'79','1400859382066-service-56-24',3,''),(274,'2014-05-23 15:57:00',2,13,'78','1400859285818-service-56-24',3,''),(275,'2014-05-23 15:57:00',2,13,'77','1400859132019-service-56-24',3,''),(276,'2014-05-23 15:57:00',2,13,'76','1400859073718-service-56-24',3,''),(277,'2014-05-23 15:57:00',2,13,'75','1400857996219-service-56-24',3,''),(278,'2014-05-26 17:22:49',2,18,'1','Provider, Provider',1,''),(279,'2014-05-26 17:23:07',2,18,'2','admin, admin',1,''),(280,'2014-05-26 17:23:20',2,18,'2','admin, admin',2,'Changed service.'),(281,'2014-05-26 17:23:27',2,18,'1','Provider, Provider',2,'Changed service.'),(282,'2014-05-26 17:50:29',2,13,'94','1401052702206-service-64-24',2,'Changed refund_status.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'permission','auth','permission'),(2,'group','auth','group'),(4,'content type','contenttypes','contenttype'),(5,'session','sessions','session'),(6,'site','sites','site'),(7,'PayPal IPN','ipn','paypalipn'),(8,'log entry','admin','logentry'),(9,'migration history','south','migrationhistory'),(10,'user','accounts','user'),(11,'service','service','service'),(12,'service type','service','servicetype'),(13,'invoice','choiceNet','invoice'),(14,'balance','choiceNet','balance'),(15,'session','choiceNet','session'),(16,'comment','choiceNet','comment'),(17,'income','choiceNet','income'),(18,'service owner','service','serviceowner');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('22lxa2idb07epp9dg2vnyxz05s8u9h0y','Zjg1NWUxMzJiMTQxNjcwNDk3MzNjZDkxM2I3YTg5NDQ3ODU2YjliZjqAAn1xAS4=','2013-09-30 20:47:12'),('5c2hptbpopekoame2qo8wbrxrumljh8e','Zjg1NWUxMzJiMTQxNjcwNDk3MzNjZDkxM2I3YTg5NDQ3ODU2YjliZjqAAn1xAS4=','2013-10-01 15:45:51'),('5o5di2s7ocrt1cobczjxcuiz74uh5ito','NDdjMWEzODRmNjUzMjkwMjUwYTRhZjI4ZGU2MzcxZDdmY2NkY2NkYjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==','2013-11-14 21:06:00'),('5tzpxvexp2d1jd3hf3nwh3xixkvjg2k1','OTZmZDk0YzllYzQ5NzFjNDJjOWE4ODhkYzRiZmQ5NmMyYzY3ZTc1Njp7InRlc3Rjb29raWUiOiJ3b3JrZWQifQ==','2014-04-24 15:58:12'),('6769iijx2lmr7ygrvt5easbcexupwomd','NWZlM2QxMzc3ZGY0MTM0YzgxZjY5YTA2NTAxYzJjZWYxNzVlN2FjYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARhVA3VpZHEFigEYdS4=','2013-10-07 20:09:18'),('6rzif91x701ho028ah502jf0uo65djs2','NjRhOWZhOTZjN2IyOTA2OWQ2NGQ3MWMwZTZiYTJjMjg0YjA3NzMzZTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MjQsInVpZCI6MjR9','2013-12-10 03:37:12'),('af60i6tevc56hpecrhhxakod1c1ao9ct','Zjg1NWUxMzJiMTQxNjcwNDk3MzNjZDkxM2I3YTg5NDQ3ODU2YjliZjqAAn1xAS4=','2013-12-05 23:52:26'),('cstwa65z0zyxje4y9z8dcgbkel5z7cwh','ZDgwNTkxODcyMTkxMmJiMzcyODkwNTAxMjc4NTdmY2I5YmVkOTZmMTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-06-09 17:46:20'),('esi1krs0zmu5l5ixaio4rwy06sw0ekby','YzFlYzlhMmQ4MGM5NDM0MzUyNjBjYTFiYTdkOTRmZGFlYjZmMjhjMzqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2013-10-02 21:00:12'),('gf8bt2a9v8zujrgi28xxjpad4l25yoe4','YzFlYzlhMmQ4MGM5NDM0MzUyNjBjYTFiYTdkOTRmZGFlYjZmMjhjMzqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2013-10-05 02:39:08'),('gi0lnu5vcigvkhc41fzlid784kpd7vvq','ZDgwNTkxODcyMTkxMmJiMzcyODkwNTAxMjc4NTdmY2I5YmVkOTZmMTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-03-02 03:43:12'),('glmf2bv7iy9zxi79hkkycw3nzds51plm','NWZlM2QxMzc3ZGY0MTM0YzgxZjY5YTA2NTAxYzJjZWYxNzVlN2FjYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARhVA3VpZHEFigEYdS4=','2013-10-11 14:38:23'),('gygkimrhsfp2qhmga06yqsdpb7lpqfbg','Zjg1NWUxMzJiMTQxNjcwNDk3MzNjZDkxM2I3YTg5NDQ3ODU2YjliZjqAAn1xAS4=','2013-10-07 15:03:37'),('hty7srzzn70taxuidxl7r849s7p1m3u6','NjRhOWZhOTZjN2IyOTA2OWQ2NGQ3MWMwZTZiYTJjMjg0YjA3NzMzZTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MjQsInVpZCI6MjR9','2014-04-03 19:31:18'),('id8u8myoomu1o26nr1a0s3m7z4lwveh5','Zjg1NWUxMzJiMTQxNjcwNDk3MzNjZDkxM2I3YTg5NDQ3ODU2YjliZjqAAn1xAS4=','2013-10-04 15:43:57'),('lfwh2mcqum72e6wi3nw19i5bb3ahdofi','YzFlYzlhMmQ4MGM5NDM0MzUyNjBjYTFiYTdkOTRmZGFlYjZmMjhjMzqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2013-10-05 12:55:24'),('n55as0l39hc6wy8g1g6wleejvj9cd5ee','Zjg1NWUxMzJiMTQxNjcwNDk3MzNjZDkxM2I3YTg5NDQ3ODU2YjliZjqAAn1xAS4=','2013-10-01 15:45:26'),('n5khsfl8fkkhlmaf1u0pff8xyw4jkzet','NGFkMjVhY2ZkNTUzODY5YTYzYzZhZDgyODQ5ZGRhMjQ5ZDEyMTZjZTqAAn1xAVgKAAAAdGVzdGNvb2tpZVgGAAAAd29ya2VkcQJzLg==','2013-09-27 19:40:38'),('naqsqmbhgazn4ev4amiv7s6h71dngw31','YzFlYzlhMmQ4MGM5NDM0MzUyNjBjYTFiYTdkOTRmZGFlYjZmMjhjMzqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2013-10-01 14:23:40'),('njm1bsgxtg6o33mo69owg6jsle1ublke','Zjg1NWUxMzJiMTQxNjcwNDk3MzNjZDkxM2I3YTg5NDQ3ODU2YjliZjqAAn1xAS4=','2013-10-01 15:06:24'),('nm241emf5lwrbngql35hq93gbo5leqfh','NWZlM2QxMzc3ZGY0MTM0YzgxZjY5YTA2NTAxYzJjZWYxNzVlN2FjYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARhVA3VpZHEFigEYdS4=','2013-10-07 20:07:12'),('nyui9roaayywicgjwka6pr660uiaqtdw','YzFlYzlhMmQ4MGM5NDM0MzUyNjBjYTFiYTdkOTRmZGFlYjZmMjhjMzqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2013-10-05 15:41:36'),('plqvzjpfqh0ob8w8s492sz55sdhcha36','NDdjMWEzODRmNjUzMjkwMjUwYTRhZjI4ZGU2MzcxZDdmY2NkY2NkYjqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKAQJ1Lg==','2013-11-12 18:16:33'),('qlzf2315wj8qxhzkbjjd4p4qhhg3iwk6','ZDgwNTkxODcyMTkxMmJiMzcyODkwNTAxMjc4NTdmY2I5YmVkOTZmMTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-01-21 19:28:55'),('r7ia14bllz1uoc905dw9n9zgr0lct3v2','ZDgwNTkxODcyMTkxMmJiMzcyODkwNTAxMjc4NTdmY2I5YmVkOTZmMTp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6Mn0=','2014-04-25 15:12:07'),('svqbic6damcakew1gc768t9rtd6olinu','NWZlM2QxMzc3ZGY0MTM0YzgxZjY5YTA2NTAxYzJjZWYxNzVlN2FjYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARhVA3VpZHEFigEYdS4=','2013-12-02 23:40:28'),('try0umnf4045ulsukuegi7ral1kqiqx2','Zjg1NWUxMzJiMTQxNjcwNDk3MzNjZDkxM2I3YTg5NDQ3ODU2YjliZjqAAn1xAS4=','2013-10-07 20:00:11'),('ttajb7wc3lt8fbw0fkqz0tl5lhylbkgi','YzFlYzlhMmQ4MGM5NDM0MzUyNjBjYTFiYTdkOTRmZGFlYjZmMjhjMzqAAn1xAVgKAAAAdGVzdGNvb2tpZXECWAYAAAB3b3JrZWRxA3Mu','2013-10-01 19:26:05'),('tx17bxo5hyu3s26vapym5bitkbq2h3gk','Zjg1NWUxMzJiMTQxNjcwNDk3MzNjZDkxM2I3YTg5NDQ3ODU2YjliZjqAAn1xAS4=','2013-10-04 22:11:54'),('v2am9maqmwhhbhttwspkcfw50y15zx48','Zjg1NWUxMzJiMTQxNjcwNDk3MzNjZDkxM2I3YTg5NDQ3ODU2YjliZjqAAn1xAS4=','2013-09-30 20:47:09'),('v9yasv25fezq7m1nv7vfk072g3y1bw0y','Zjg1NWUxMzJiMTQxNjcwNDk3MzNjZDkxM2I3YTg5NDQ3ODU2YjliZjqAAn1xAS4=','2013-09-30 20:45:59'),('xzxzyle1b5kt4twgi8c4g5clkx5pch4i','NWZlM2QxMzc3ZGY0MTM0YzgxZjY5YTA2NTAxYzJjZWYxNzVlN2FjYzqAAn1xAShVEl9hdXRoX3VzZXJfYmFja2VuZHECVSlkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZHEDVQ1fYXV0aF91c2VyX2lkcQSKARhVA3VpZHEFigEYdS4=','2013-10-07 15:09:48'),('z9r1ie77rairiwivk4y2ukofzz3p7b06','ODliYzVjZjRhN2YzODk0OWJmNTc1NGU4MWY0YTY1NjQyYjVmNGVhNDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9pZCI6MzYsInVpZCI6MzZ9','2014-06-09 17:39:16');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `paypal_ipn`
--

DROP TABLE IF EXISTS `paypal_ipn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `paypal_ipn` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `business` varchar(127) NOT NULL,
  `charset` varchar(32) NOT NULL,
  `custom` varchar(255) NOT NULL,
  `notify_version` decimal(64,2) DEFAULT NULL,
  `parent_txn_id` varchar(19) NOT NULL,
  `receiver_email` varchar(127) NOT NULL,
  `receiver_id` varchar(127) NOT NULL,
  `residence_country` varchar(2) NOT NULL,
  `test_ipn` tinyint(1) NOT NULL,
  `txn_id` varchar(19) NOT NULL,
  `txn_type` varchar(128) NOT NULL,
  `verify_sign` varchar(255) NOT NULL,
  `address_country` varchar(64) NOT NULL,
  `address_city` varchar(40) NOT NULL,
  `address_country_code` varchar(64) NOT NULL,
  `address_name` varchar(128) NOT NULL,
  `address_state` varchar(40) NOT NULL,
  `address_status` varchar(11) NOT NULL,
  `address_street` varchar(200) NOT NULL,
  `address_zip` varchar(20) NOT NULL,
  `contact_phone` varchar(20) NOT NULL,
  `first_name` varchar(64) NOT NULL,
  `last_name` varchar(64) NOT NULL,
  `payer_business_name` varchar(127) NOT NULL,
  `payer_email` varchar(127) NOT NULL,
  `payer_id` varchar(13) NOT NULL,
  `auth_amount` decimal(64,2) DEFAULT NULL,
  `auth_exp` varchar(28) NOT NULL,
  `auth_id` varchar(19) NOT NULL,
  `auth_status` varchar(9) NOT NULL,
  `exchange_rate` decimal(64,16) DEFAULT NULL,
  `invoice` varchar(127) NOT NULL,
  `item_name` varchar(127) NOT NULL,
  `item_number` varchar(127) NOT NULL,
  `mc_currency` varchar(32) NOT NULL,
  `mc_fee` decimal(64,2) DEFAULT NULL,
  `mc_gross` decimal(64,2) DEFAULT NULL,
  `mc_handling` decimal(64,2) DEFAULT NULL,
  `mc_shipping` decimal(64,2) DEFAULT NULL,
  `memo` varchar(255) NOT NULL,
  `num_cart_items` int(11) DEFAULT NULL,
  `option_name1` varchar(64) NOT NULL,
  `option_name2` varchar(64) NOT NULL,
  `payer_status` varchar(10) NOT NULL,
  `payment_date` datetime DEFAULT NULL,
  `payment_gross` decimal(64,2) DEFAULT NULL,
  `payment_status` varchar(9) NOT NULL,
  `payment_type` varchar(7) NOT NULL,
  `pending_reason` varchar(14) NOT NULL,
  `protection_eligibility` varchar(32) NOT NULL,
  `quantity` int(11) DEFAULT NULL,
  `reason_code` varchar(15) NOT NULL,
  `remaining_settle` decimal(64,2) DEFAULT NULL,
  `settle_amount` decimal(64,2) DEFAULT NULL,
  `settle_currency` varchar(32) NOT NULL,
  `shipping` decimal(64,2) DEFAULT NULL,
  `shipping_method` varchar(255) NOT NULL,
  `tax` decimal(64,2) DEFAULT NULL,
  `transaction_entity` varchar(7) NOT NULL,
  `auction_buyer_id` varchar(64) NOT NULL,
  `auction_closing_date` datetime DEFAULT NULL,
  `auction_multi_item` int(11) DEFAULT NULL,
  `for_auction` decimal(64,2) DEFAULT NULL,
  `amount` decimal(64,2) DEFAULT NULL,
  `amount_per_cycle` decimal(64,2) DEFAULT NULL,
  `initial_payment_amount` decimal(64,2) DEFAULT NULL,
  `next_payment_date` datetime DEFAULT NULL,
  `outstanding_balance` decimal(64,2) DEFAULT NULL,
  `payment_cycle` varchar(32) NOT NULL,
  `period_type` varchar(32) NOT NULL,
  `product_name` varchar(128) NOT NULL,
  `product_type` varchar(128) NOT NULL,
  `profile_status` varchar(32) NOT NULL,
  `recurring_payment_id` varchar(128) NOT NULL,
  `rp_invoice_id` varchar(127) NOT NULL,
  `time_created` datetime DEFAULT NULL,
  `amount1` decimal(64,2) DEFAULT NULL,
  `amount2` decimal(64,2) DEFAULT NULL,
  `amount3` decimal(64,2) DEFAULT NULL,
  `mc_amount1` decimal(64,2) DEFAULT NULL,
  `mc_amount2` decimal(64,2) DEFAULT NULL,
  `mc_amount3` decimal(64,2) DEFAULT NULL,
  `password` varchar(24) NOT NULL,
  `period1` varchar(32) NOT NULL,
  `period2` varchar(32) NOT NULL,
  `period3` varchar(32) NOT NULL,
  `reattempt` varchar(1) NOT NULL,
  `recur_times` int(11) DEFAULT NULL,
  `recurring` varchar(1) NOT NULL,
  `retry_at` datetime DEFAULT NULL,
  `subscr_date` datetime DEFAULT NULL,
  `subscr_effective` datetime DEFAULT NULL,
  `subscr_id` varchar(19) NOT NULL,
  `username` varchar(64) NOT NULL,
  `case_creation_date` datetime DEFAULT NULL,
  `case_id` varchar(14) NOT NULL,
  `case_type` varchar(24) NOT NULL,
  `receipt_id` varchar(64) NOT NULL,
  `currency_code` varchar(32) NOT NULL,
  `handling_amount` decimal(64,2) DEFAULT NULL,
  `transaction_subject` varchar(255) NOT NULL,
  `ipaddress` char(15) NOT NULL,
  `flag` tinyint(1) NOT NULL,
  `flag_code` varchar(16) NOT NULL,
  `flag_info` longtext NOT NULL,
  `query` longtext NOT NULL,
  `response` longtext NOT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `from_view` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `paypal_ipn`
--

LOCK TABLES `paypal_ipn` WRITE;
/*!40000 ALTER TABLE `paypal_ipn` DISABLE KEYS */;
/*!40000 ALTER TABLE `paypal_ipn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service_service`
--

DROP TABLE IF EXISTS `service_service`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `service_service` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `date_created` datetime NOT NULL,
  `date_modified` datetime,
  `date_used` datetime,
  `picture` varchar(100),
  `owner_id` int(11),
  `description` varchar(3000),
  `service_id` varchar(255) NOT NULL,
  `service_type` varchar(255),
  `hosted_node_id` varchar(255),
  `end_point1_id` varchar(255),
  `end_point1_ip` varchar(255),
  `end_point2_id` varchar(255),
  `end_point2_ip` varchar(255),
  `service_bandwidth` decimal(64,12) NOT NULL,
  `service_latency` decimal(64,12) NOT NULL,
  `service_cost` decimal(64,12) NOT NULL,
  `controller_id` varchar(255),
  `controller_ip` varchar(255),
  `service_listings` varchar(1024),
  PRIMARY KEY (`id`),
  KEY `service_service_cb902d83` (`owner_id`),
  CONSTRAINT `owner_id_refs_id_98b58480` FOREIGN KEY (`owner_id`) REFERENCES `accounts_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=69 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service_service`
--

LOCK TABLES `service_service` WRITE;
/*!40000 ALTER TABLE `service_service` DISABLE KEYS */;
INSERT INTO `service_service` VALUES (1,'Testing Service','2013-10-31 23:03:11','2013-10-31 23:03:14','2013-10-31 23:03:17','',NULL,'','0','','','','','','',5442.000000000000,5.000000000000,435.000000000000,'','',''),(2,'Expensive Service','2013-11-01 16:12:39','2013-11-01 16:12:41','2013-11-01 16:12:42','',NULL,'','0','','','','','','',34.000000000000,0.220000000000,999999.743000000000,'','',''),(3,'Cheaper','2013-11-01 16:16:46','2014-05-07 01:00:02','2013-11-01 16:16:49','',36,'','0','','','','','','',6.000000000000,2.000000000000,0.190000000000,'','',''),(4,'Encryption Service','2013-11-20 02:06:15','2013-11-20 02:06:16','2013-11-20 02:06:18','',NULL,'','0','','','','','','',1.000000000000,44.000000000000,0.432000000000,'','',''),(5,'Decryption Service','2013-11-20 02:07:37','2013-11-20 02:07:39','2013-11-20 02:07:41','',NULL,'','0','','','','','','',1.000000000000,1.000000000000,0.567000000000,'','',''),(6,'Compressing Service','2013-11-20 02:08:56','2013-11-20 02:08:59','2013-11-20 02:09:00','pictures/2013/11/23/QQ20131123-72x.png',NULL,'','0','','','','','','',1.000000000000,1.000000000000,32.000000000000,'','',''),(7,'Decompressing','2013-11-20 02:10:22','2013-11-20 02:10:24','2013-11-20 02:10:28','',NULL,'','0','','','','','','',1.000000000000,1.000000000000,798.000000000000,'','',''),(8,'Test Service 1','2013-11-20 16:24:24','2013-11-20 16:24:26','2013-11-20 16:24:29','pictures/2013/11/23/QQ20131123-62x_2.png',NULL,'','0','','','','','','',24.000000000000,78.000000000000,67.000000000000,'','',''),(9,'Test Service 2','2013-11-20 16:25:02','2013-11-20 16:25:04','2013-11-20 16:25:07','',NULL,'','0','','','','','','',5.000000000000,6.000000000000,6.000000000000,'','',''),(10,'Test Service 2','2013-11-20 16:26:41','2013-11-20 16:26:42','2013-11-20 16:26:44','',NULL,'','0','','','','','','',4.000000000000,4.000000000000,4.000000000000,'','',''),(11,'Test Service 3','2013-11-20 16:29:15','2013-11-20 16:29:18','2013-11-20 16:29:20','',NULL,'','0','','','','','','',77.000000000000,77.000000000000,77.000000000000,'','',''),(12,'Test Service 4','2013-11-20 16:29:57','2013-11-20 16:29:59','2013-11-20 16:30:01','',NULL,'','0','','','','','','',45.000000000000,3.000000000000,65.000000000000,'','',''),(13,'Test Service 5','2013-11-20 16:30:35','2013-11-20 16:30:36','2013-11-20 16:30:39','',NULL,'','0','','','','','','',4356.000000000000,45.000000000000,5436.000000000000,'','',''),(14,'Test Service 6','2013-11-20 16:31:15','2013-11-20 16:31:18','2013-11-20 16:31:20','',NULL,'','0','','','','','','',3246.000000000000,43.000000000000,4.000000000000,'','',''),(15,'Test Service 7','2013-11-20 16:33:02','2013-11-20 16:33:05','2013-11-20 16:33:08','',NULL,'','0','','','','','','',435.000000000000,324.000000000000,34.000000000000,'','',''),(16,'Test Service 8','2013-11-20 16:33:40','2013-11-20 16:33:42','2013-11-20 16:33:44','',NULL,'','0','','','','','','',3457.000000000000,4.000000000000,23.000000000000,'','',''),(17,'Test Service 9','2013-11-20 16:34:24','2013-11-20 16:34:27','2013-11-20 16:34:29','',NULL,'','0','','','','','','',99.000000000000,99.000000000000,99.000000000000,'','',''),(18,'Test Service 10','2013-11-20 16:35:11','2013-11-20 16:35:14','2013-11-20 16:35:16','',NULL,'','0','','','','','','',34.000000000000,75.000000000000,89.000000000000,'','',''),(19,'Test Service 11','2013-11-20 16:35:57','2013-11-20 16:36:00','2013-11-20 16:36:02','',NULL,'','0','','','','','','',56.000000000000,668.000000000000,0.344600000000,'','',''),(20,'Test Service 12','2013-11-20 16:36:44','2013-11-20 16:36:46','2013-11-20 16:36:48','',36,'','0','','','','','','',89.000000000000,70.000000000000,345.000000000000,'','',''),(21,'Test Service 13','2013-11-20 16:37:27','2013-11-20 16:37:30','2013-11-20 16:37:31','',NULL,'','0','','','','','','',346.000000000000,678.000000000000,4.000000000000,'','',''),(22,'Test Service 14','2013-11-20 16:38:04','2013-11-20 16:38:09','2013-11-20 16:38:12','',NULL,'','0','','','','','','',765.000000000000,33.000000000000,11111.000000000000,'','',''),(23,'Test Service 15','2013-11-20 16:38:51','2013-11-20 16:38:53','2013-11-20 16:38:54','',NULL,'','0','','','','','','',65.000000000000,1.000000000000,1.000000000000,'','',''),(24,'Test Service 16','2013-11-20 16:39:31','2013-11-20 16:39:32','2013-11-20 16:39:34','',NULL,'','0','','','','','','',1.000000000000,1.000000000000,1.000000000000,'','',''),(25,'Test Service 17','2013-11-20 16:40:05','2013-11-20 16:40:07','2013-11-20 16:40:09','',NULL,'','0','','','','','','',1.000000000000,1.000000000000,1.000000000000,'','',''),(26,'Test Service 18','2013-11-20 16:40:44','2013-11-20 16:40:46','2013-11-20 16:40:47','',NULL,'','0','','','','','','',2.000000000000,2.000000000000,2.000000000000,'','',''),(27,'Test Service 19','2013-11-20 16:41:26','2013-11-20 16:41:28','2013-11-20 16:41:30','',NULL,'','0','','','','','','',3.000000000000,3.000000000000,3.000000000000,'','',''),(28,'Test Service 20','2013-11-20 16:42:03','2013-11-20 16:42:06','2013-11-20 16:42:08','',NULL,'','0','','','','','','',6.000000000000,6.000000000000,6.000000000000,'','',''),(29,'Test Service 21','2013-11-20 22:21:09','2013-11-20 22:21:12','2013-11-20 22:21:14','',NULL,'','0','','','','','','',7.000000000000,7.000000000000,7.000000000000,'','',''),(30,'Test Service 22','2013-11-20 22:21:46','2013-11-20 22:21:49','2013-11-20 22:21:50','',NULL,'','0','','','','','','',8.000000000000,8.000000000000,8.000000000000,'','',''),(31,'Test Service 23','2013-11-20 22:22:24','2013-11-20 22:22:27','2013-11-20 22:22:29','',NULL,'','0','','','','','','',9.000000000000,9.000000000000,9.000000000000,'','',''),(32,'Test Service 24','2013-11-20 22:23:07','2013-11-20 22:23:09','2013-11-20 22:23:11','',NULL,'','0','','','','','','',11.000000000000,11.000000000000,11.000000000000,'','',''),(33,'Test Service 25','2013-11-20 22:23:43','2013-11-20 22:23:45','2013-11-20 22:23:47','',NULL,'','0','','','','','','',22.000000000000,22.000000000000,22.000000000000,'','',''),(34,'Test Service 26','2013-11-20 22:24:19','2013-11-20 22:24:22','2013-11-20 22:24:23','',NULL,'','0','','','','','','',33.000000000000,33.000000000000,33.000000000000,'','',''),(35,'Test Service 27','2013-11-20 22:24:59','2013-11-20 22:25:01','2013-11-20 22:25:03','',NULL,'','0','','','','','','',44.000000000000,44.000000000000,44.000000000000,'','',''),(36,'Test Service 28','2013-11-20 22:30:51','2013-11-20 22:30:54','2013-11-20 22:30:56','',NULL,'','0','','','','','','',55.000000000000,55.000000000000,55.000000000000,'','',''),(37,'Test Service 29','2013-11-20 22:31:28','2013-11-20 22:31:30','2013-11-20 22:31:32','',NULL,'','0','','','','','','',66.000000000000,66.000000000000,66.000000000000,'','',''),(38,'Test Service 30','2013-11-20 22:32:52','2013-11-20 22:32:54','2013-11-20 22:32:56','',NULL,'','0','','','','','','',88.000000000000,88.000000000000,88.000000000000,'','',''),(39,'Test Service 31','2013-11-20 22:33:32','2013-11-20 22:33:34','2013-11-20 22:33:35','',NULL,'','0','','','','','','',1.000000000000,2.000000000000,3.000000000000,'','',''),(40,'Test Service 32','2013-11-20 22:34:17','2013-11-20 22:34:19','2013-11-20 22:34:20','',NULL,'','0','','','','','','',3.000000000000,2.000000000000,1.000000000000,'','',''),(41,'Test Service 33','2013-11-20 22:34:53','2013-11-20 22:34:55','2013-11-20 22:34:57','',NULL,'','0','','','','','','',5.000000000000,3.000000000000,1.000000000000,'','',''),(42,'Test Service 34','2013-11-20 22:35:23','2013-11-20 22:35:25','2013-11-20 22:35:28','',NULL,'','0','','','','','','',4.000000000000,7.000000000000,8.000000000000,'','',''),(43,'Test Service 35','2013-11-20 22:35:56','2013-11-20 22:35:57','2013-11-20 22:35:59','',NULL,'','0','','','','','','',7.000000000000,7.000000000000,4.000000000000,'','',''),(44,'Test Service 36','2013-11-20 22:36:25','2013-11-20 22:36:26','2013-11-20 22:36:28','',NULL,'','0','','','','','','',6.000000000000,4.000000000000,3.000000000000,'','',''),(45,'Test Service 37','2013-11-20 22:36:57','2013-11-20 22:36:58','2013-11-20 22:37:00','',NULL,'','0','','','','','','',6.000000000000,6.000000000000,4.000000000000,'','',''),(46,'Test Service 38','2013-11-20 22:37:24','2013-11-20 22:37:26','2013-11-20 22:37:28','',NULL,'','0','','','','','','',3.000000000000,6.000000000000,4.000000000000,'','',''),(47,'Test Service 39','2013-11-20 22:38:03','2013-11-20 22:38:05','2013-11-20 22:38:06','',NULL,'','0','','','','','','',12.000000000000,12.000000000000,12.000000000000,'','',''),(48,'Test Service 40','2013-11-20 22:38:39','2013-11-20 22:38:41','2013-11-20 22:38:44','',NULL,'','0','','','','','','',2.000000000000,345.000000000000,74.000000000000,'','',''),(49,'Test Service 41','2013-11-20 22:39:14','2013-11-20 22:39:15','2013-11-20 22:39:17','',NULL,'','0','','','','','','',456.000000000000,4546.000000000000,23.000000000000,'','',''),(50,'Test Service 42','2013-11-20 22:39:43','2013-11-20 22:39:44','2013-11-20 22:39:46','',NULL,'','0','','','','','','',452.000000000000,2345.000000000000,6454.000000000000,'','',''),(51,'Test Service 43','2013-11-20 22:40:12','2013-11-20 22:40:14','2013-11-20 22:40:15','',NULL,'','0','','','','','','',2345.000000000000,43.000000000000,4.000000000000,'','',''),(52,'Test Service 44','2013-11-20 22:40:44','2013-11-20 22:40:45','2013-11-20 22:40:47','',NULL,'','0','','','','','','',32.000000000000,62.000000000000,42.000000000000,'','',''),(53,'Long name service long long long long long long long long','2013-11-23 17:17:40','2013-11-23 17:17:42','2013-11-23 17:17:44','',NULL,'Long name service long long long long long long long longLong name service long long long long long long long longLong name service long long long long long long long longLong name service long long long long long long long longLong name service long long long long long long long longLong name service long long long long long long long longLong name service long long long long long long long longLong name service long long long long long long long longLong name service long long long long long long long longLong name service long long long long long long long longLong name service long long long long long long long longLong name service long long long long long long long longLong name service long long long long long long long longLong name service long long long long long long long long','0','','','','','','',456.000000000000,3.000000000000,342.000000000000,'','',''),(54,'This is for testing null field','2013-11-23 17:51:41',NULL,NULL,NULL,NULL,NULL,'0',NULL,NULL,NULL,NULL,NULL,NULL,0.000000000000,0.000000000000,0.000000000000,NULL,NULL,NULL),(55,'Test Service 7000','2013-11-23 16:24:24',NULL,NULL,'',NULL,'','0','','','','','','',432.000000000000,4.000000000000,45.000000000000,'','',''),(56,'Add Balance','2014-04-29 18:57:42',NULL,NULL,'',2,'Add balance service','56-add-balance','','','','','','',1.000000000000,1.000000000000,0.010000000000,'','',''),(57,'Service 1','2014-05-06 16:21:55','2014-05-06 16:21:57','2014-05-06 16:21:58','',36,'','10.5.0.2_0_10.6.0.2','NetworkLink100','','10.5.0.2','10.5.0.2','10.6.0.2','10.6.0.2',2034.000000000000,2.000000000000,29.794921875000,'Controller_192.168.0.15_6634','192.168.0.15',''),(58,'Service 2','2014-05-06 16:50:11','2014-05-06 16:50:13','2014-05-06 16:50:14','',36,'','10.6.0.2_0_10.3.0.1','NetworkLink100','','10.6.0.2','10.6.0.2','10.3.0.2','10.3.0.2',986.000000000000,2.000000000000,14.443359375000,'Controller_192.168.0.15_6634','192.168.0.15',''),(59,'Service 3','2014-05-06 18:44:33','2014-05-06 18:44:35','2014-05-06 18:44:36','',36,'','10.6.0.2_0_10.5.0.1','NetworkLink100','','10.6.0.2','10.6.0.2','10.5.0.1','10.5.0.1',1054.000000000000,2.000000000000,15.439453125000,'Controller_192.168.0.15_6634','192.168.0.15',''),(60,'Service 4','2014-05-06 18:47:00','2014-05-06 18:47:02','2014-05-06 18:47:04','',36,'','10.3.0.2_0_10.6.0.2','NetworkLink100','','10.3.0.2','10.3.0.2','10.6.0.2','10.6.0.2',1119.000000000000,2.000000000000,16.391601562500,'Controller_192.168.0.15_6634','192.168.0.15',''),(61,'Service 5','2014-05-06 19:23:38','2014-05-06 19:23:39','2014-05-06 19:23:41','',36,'','10.4.0.2_0_10.5.0.2','NetworkLink100','','10.4.0.2','10.4.0.2','10.5.0.2','10.5.0.2',789.000000000000,2.000000000000,11.557617187500,'Controller_192.168.0.15_6633','192.168.0.15',''),(62,'Service 6','2014-05-06 19:27:17','2014-05-06 19:27:19','2014-05-06 19:27:20','',36,'','10.3.0.1_0_10.4.0.2','NetworkLink100','','10.3.0.1','10.3.0.1','10.4.0.2','10.4.0.2',1627.000000000000,2.000000000000,23.833007812500,'Controller_192.168.0.15_6633','192.168.0.15',''),(63,'Service 7','2014-05-06 19:31:33','2014-05-06 19:31:34','2014-05-06 19:31:36','',36,'','10.4.0.2_0_10.3.0.2','NetworkLink100','','10.4.0.2','10.4.0.2','10.3.0.2','10.3.0.2',522.000000000000,2.000000000000,7.646484375000,'Controller_192.168.0.15_6633','192.168.0.15',''),(64,'Service 8','2014-05-06 19:33:55','2014-05-06 19:33:57','2014-05-06 19:33:59','',36,'','10.5.0.1_0_10.4.0.2','NetworkLink100','','10.5.0.1','10.5.0.1','10.4.0.2','10.4.0.2',1330.000000000000,2.000000000000,19.482421875000,'Controller_192.168.0.15_6633','192.168.0.15',''),(65,'Provider add service','2014-05-06 23:11:58','2014-05-06 23:11:58','2014-05-06 23:11:58','',36,'Provider add service','Provider add service','','','','','','',4356.000000000000,3345.440000000000,67.450000000000,'','',''),(66,'Provider add service','2014-05-06 23:12:04','2014-05-06 23:12:04','2014-05-06 23:12:04','',36,'Provider add service','Provider add service','','','','','','',4356.000000000000,3345.440000000000,67.450000000000,'','',''),(67,'Provider add service3','2014-05-06 23:14:41','2014-05-06 23:14:41','2014-05-06 23:14:41','',36,'','Provider add service3','','','','','','',5.767000000000,75674.000000000000,5.778990000000,'','',''),(68,'Provider add service4','2014-05-06 23:16:38','2014-05-06 23:16:38','2014-05-06 23:16:38','',2,'','Provider add service4','','','','','','',345.000000000000,5346.000000000000,193.000000000000,'','','');
/*!40000 ALTER TABLE `service_service` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service_service_service_type`
--

DROP TABLE IF EXISTS `service_service_service_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `service_service_service_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `service_id` int(11) NOT NULL,
  `servicetype_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `service_service_service_type_service_id_1e11c8e902154852_uniq` (`service_id`,`servicetype_id`),
  KEY `service_service_service_type_91a0ac17` (`service_id`),
  KEY `service_service_service_type_b5dca47b` (`servicetype_id`),
  CONSTRAINT `servicetype_id_refs_id_2838f234` FOREIGN KEY (`servicetype_id`) REFERENCES `service_servicetype` (`id`),
  CONSTRAINT `service_id_refs_id_351a6d61` FOREIGN KEY (`service_id`) REFERENCES `service_service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service_service_service_type`
--

LOCK TABLES `service_service_service_type` WRITE;
/*!40000 ALTER TABLE `service_service_service_type` DISABLE KEYS */;
INSERT INTO `service_service_service_type` VALUES (1,1,3),(2,1,4),(3,1,5),(4,2,3),(61,3,3),(6,4,2),(7,4,3),(8,5,4),(9,5,5),(60,6,4),(11,7,2),(63,8,5),(13,9,4),(14,10,4),(15,11,4),(16,12,2),(17,13,4),(18,14,4),(19,15,4),(20,16,2),(21,17,4),(22,18,2),(23,19,4),(62,20,3),(25,22,3),(26,23,5),(27,24,4),(28,25,2),(29,26,4),(30,27,4),(31,28,4),(32,29,2),(33,30,2),(34,31,4),(35,32,2),(36,33,2),(37,34,2),(38,35,2),(39,36,2),(40,37,2),(41,38,4),(42,39,5),(43,40,4),(44,41,2),(45,42,4),(46,43,2),(47,44,2),(48,45,3),(49,46,4),(50,47,2),(51,48,2),(52,49,3),(53,50,3),(54,51,4),(55,52,2),(56,54,8);
/*!40000 ALTER TABLE `service_service_service_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service_serviceowner`
--

DROP TABLE IF EXISTS `service_serviceowner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `service_serviceowner` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `owner_id` int(11) DEFAULT NULL,
  `service_id` int(11) DEFAULT NULL,
  `share_cost` decimal(64,12) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `service_serviceowner_cb902d83` (`owner_id`),
  KEY `service_serviceowner_91a0ac17` (`service_id`),
  CONSTRAINT `owner_id_refs_id_902361c1` FOREIGN KEY (`owner_id`) REFERENCES `accounts_user` (`id`),
  CONSTRAINT `service_id_refs_id_b16cae7a` FOREIGN KEY (`service_id`) REFERENCES `service_service` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service_serviceowner`
--

LOCK TABLES `service_serviceowner` WRITE;
/*!40000 ALTER TABLE `service_serviceowner` DISABLE KEYS */;
INSERT INTO `service_serviceowner` VALUES (1,36,58,4.443359375000),(2,2,58,10.000000000000);
/*!40000 ALTER TABLE `service_serviceowner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `service_servicetype`
--

DROP TABLE IF EXISTS `service_servicetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `service_servicetype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) NOT NULL,
  `category` varchar(20) DEFAULT NULL,
  `description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `service_servicetype`
--

LOCK TABLES `service_servicetype` WRITE;
/*!40000 ALTER TABLE `service_servicetype` DISABLE KEYS */;
INSERT INTO `service_servicetype` VALUES (1,'Encryption','Important',''),(2,'Decryption','Important',''),(3,'Compression','Important',''),(4,'Decompression','Important',''),(5,'Coding','Important',''),(6,'DNS','Secondary',''),(7,'WINS','Secondary',''),(8,'Link','Secondary','');
/*!40000 ALTER TABLE `service_servicetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'ipn','0001_first_migration','2013-09-16 19:44:45'),(2,'accounts','0001_initial','2013-09-18 15:30:38'),(3,'services','0001_initial','2013-10-31 21:25:40'),(4,'service','0001_initial','2013-10-31 21:54:08'),(5,'service','0002_auto__chg_field_service_name','2013-11-23 16:16:25'),(6,'service','0003_auto__chg_field_service_delay','2013-11-23 16:30:34'),(7,'service','0004_auto__chg_field_service_date_modified__chg_field_service_max_bandwidth','2013-11-23 16:50:44'),(8,'service','0005_auto__add_field_service_picture','2013-11-23 17:16:53'),(9,'service','0006_auto__add_field_service_owner','2013-11-23 17:56:09'),(10,'service','0007_auto__add_field_service_description','2013-11-23 19:55:13'),(11,'choiceNet','0001_initial','2013-11-24 02:04:14'),(12,'choiceNet','0002_auto__add_field_invoice_paid','2013-11-24 03:06:43'),(13,'choiceNet','0003_auto__del_field_invoice_paid__add_field_invoice_is_paid__add_field_inv','2013-11-24 05:44:43'),(14,'choiceNet','0004_auto__del_field_invoice_s_active__add_field_invoice_is_active','2013-11-24 05:45:02'),(15,'choiceNet','0005_auto__add_balance','2014-04-29 15:19:38'),(16,'choiceNet','0006_auto__add_session','2014-04-30 15:26:21'),(17,'choiceNet','0007_auto__chg_field_session_user','2014-04-30 19:33:28'),(18,'choiceNet','0008_auto__add_field_session_key','2014-04-30 20:39:40'),(19,'choiceNet','0009_auto__chg_field_session_key','2014-04-30 21:00:28'),(20,'service','0008_auto__del_field_service_process_id__del_field_service_cost__del_field_','2014-05-06 15:23:15'),(21,'service','0009_auto__del_field_service_service_listings__del_field_service_controller','2014-05-06 15:33:40'),(22,'service','0010_auto__add_field_service_service_bandwidth__add_field_service_service_l','2014-05-06 15:34:16'),(23,'choiceNet','0010_auto__chg_field_balance_balance','2014-05-06 19:43:01'),(24,'choiceNet','0011_auto__add_comment','2014-05-07 12:44:51'),(25,'choiceNet','0012_auto__add_income','2014-05-12 20:29:44'),(26,'service','0011_auto__add_serviceowner','2014-05-26 17:21:43'),(27,'service','0012_auto__add_field_service_refund_status','2014-05-26 17:30:42'),(28,'service','0013_auto__del_field_service_refund_status','2014-05-26 17:48:58'),(29,'choiceNet','0013_auto__add_field_invoice_refund_status','2014-05-26 17:49:48');
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `test_table`
--

DROP TABLE IF EXISTS `test_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `test_table` (
  `id` int(11) NOT NULL,
  `name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `test_table`
--

LOCK TABLES `test_table` WRITE;
/*!40000 ALTER TABLE `test_table` DISABLE KEYS */;
/*!40000 ALTER TABLE `test_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-05-26 14:33:40
