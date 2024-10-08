-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: eventmanage
-- ------------------------------------------------------
-- Server version	8.0.39

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `eventcreators`
--

DROP TABLE IF EXISTS `eventcreators`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eventcreators` (
  `Gmail` varchar(255) NOT NULL,
  `EventID` int NOT NULL,
  PRIMARY KEY (`Gmail`,`EventID`),
  KEY `EventID` (`EventID`),
  CONSTRAINT `eventcreators_ibfk_1` FOREIGN KEY (`Gmail`) REFERENCES `userinfo` (`Gmail`),
  CONSTRAINT `eventcreators_ibfk_2` FOREIGN KEY (`EventID`) REFERENCES `eventsdetail` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eventcreators`
--

LOCK TABLES `eventcreators` WRITE;
/*!40000 ALTER TABLE `eventcreators` DISABLE KEYS */;
INSERT INTO `eventcreators` VALUES ('alice@example.com',1),('bob@example.com',1),('catherine@example.com',2),('david@example.com',3),('eva@example.com',4),('frank@example.com',5),('grace@example.com',6),('henry@example.com',7),('ivy@example.com',8),('jack@example.com',9);
/*!40000 ALTER TABLE `eventcreators` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eventregistrations`
--

DROP TABLE IF EXISTS `eventregistrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eventregistrations` (
  `Gmail` varchar(255) DEFAULT NULL,
  `EventID` int DEFAULT NULL,
  `RegisteredAt` datetime DEFAULT CURRENT_TIMESTAMP,
  UNIQUE KEY `UQ_User_Event` (`Gmail`,`EventID`),
  KEY `EventID` (`EventID`),
  CONSTRAINT `eventregistrations_ibfk_1` FOREIGN KEY (`Gmail`) REFERENCES `userinfo` (`Gmail`),
  CONSTRAINT `eventregistrations_ibfk_2` FOREIGN KEY (`EventID`) REFERENCES `eventsdetail` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eventregistrations`
--

LOCK TABLES `eventregistrations` WRITE;
/*!40000 ALTER TABLE `eventregistrations` DISABLE KEYS */;
INSERT INTO `eventregistrations` VALUES ('alice@example.com',1,'2024-10-07 12:22:57'),('bob@example.com',1,'2024-10-07 12:22:57'),('catherine@example.com',2,'2024-10-07 12:22:57'),('david@example.com',3,'2024-10-07 12:22:57'),('eva@example.com',4,'2024-10-07 12:22:57'),('frank@example.com',5,'2024-10-07 12:22:57'),('grace@example.com',6,'2024-10-07 12:22:57'),('henry@example.com',7,'2024-10-07 12:22:57'),('ivy@example.com',8,'2024-10-07 12:22:57'),('jack@example.com',9,'2024-10-07 12:22:57');
/*!40000 ALTER TABLE `eventregistrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `eventsdetail`
--

DROP TABLE IF EXISTS `eventsdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `eventsdetail` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `EventType` varchar(20) DEFAULT NULL,
  `EventName` varchar(255) NOT NULL,
  `StartTime` datetime NOT NULL,
  `EndTime` datetime NOT NULL,
  `Location` varchar(255) NOT NULL,
  `EventImages` text,
  `Description` text,
  `RegisteredCount` int DEFAULT '0',
  `MaxAttendees` int DEFAULT NULL,
  PRIMARY KEY (`ID`),
  CONSTRAINT `CHK_StartTime` CHECK ((`StartTime` < `EndTime`)),
  CONSTRAINT `eventsdetail_chk_1` CHECK ((`RegisteredCount` >= 0)),
  CONSTRAINT `eventsdetail_chk_2` CHECK ((`MaxAttendees` > 0))
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `eventsdetail`
--

LOCK TABLES `eventsdetail` WRITE;
/*!40000 ALTER TABLE `eventsdetail` DISABLE KEYS */;
INSERT INTO `eventsdetail` VALUES (1,'PR','Product Launch','2024-10-15 10:00:00','2024-10-15 12:00:00','Main Hall','img_5.jpg','Launching our new product line.',0,100),(2,'PL','Workshop on Product Design','2024-10-20 14:00:00','2024-10-20 17:00:00','Room 101','img_1.jpg','Learn about product design principles.',0,50),(3,'PR','Networking Event','2024-10-25 18:00:00','2024-10-25 20:00:00','Rooftop Lounge','img_4.jpg','Connect with industry professionals.',0,75),(4,'PL','Tech Conference','2024-11-01 09:00:00','2024-11-01 17:00:00','Convention Center','img_2.jpg','Discuss the latest in tech.',0,200),(5,'PR','Launch Party','2024-11-05 19:00:00','2024-11-05 22:00:00','City Square','img_3.jpg','Celebrate our new product launch.',0,150),(6,'PL','Leadership Summit','2024-11-10 09:00:00','2024-11-10 15:00:00','Grand Ballroom','img_3.jpg','Leadership skills for the modern world.',0,60),(7,'PR','Online Webinar','2024-11-15 15:00:00','2024-11-15 16:30:00','Virtual','img_2.jpg','Join us for an informative webinar.',0,200),(8,'PL','Community Meetup','2024-11-20 18:00:00','2024-11-20 20:00:00','Community Center','img_4.jpg','Meet like-minded individuals in your area.',0,30),(9,'PR','Annual Gala','2024-11-25 19:00:00','2024-11-25 23:00:00','Hotel Ballroom','img_1.jpg','Join us for our annual gala event.',0,100),(10,'PL','Hackathon','2024-12-01 10:00:00','2024-12-01 18:00:00','Tech Park','img_5.jpg','A 10-hour coding challenge.',10,50);
/*!40000 ALTER TABLE `eventsdetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `userinfo`
--

DROP TABLE IF EXISTS `userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `userinfo` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `FullName` varchar(255) NOT NULL,
  `Gmail` varchar(255) NOT NULL,
  `PhoneNumber` varchar(20) DEFAULT NULL,
  `CreatedAt` datetime DEFAULT CURRENT_TIMESTAMP,
  `UpdatedAt` datetime DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `Gmail` (`Gmail`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `userinfo`
--

LOCK TABLES `userinfo` WRITE;
/*!40000 ALTER TABLE `userinfo` DISABLE KEYS */;
INSERT INTO `userinfo` VALUES (1,'Alice Johnson','alice@example.com','1234567890','2024-10-07 12:22:57','2024-10-07 12:22:57'),(2,'Bob Smith','bob@example.com','2345678901','2024-10-07 12:22:57','2024-10-07 12:22:57'),(3,'Catherine Brown','catherine@example.com','3456789012','2024-10-07 12:22:57','2024-10-07 12:22:57'),(4,'David Wilson','david@example.com','4567890123','2024-10-07 12:22:57','2024-10-07 12:22:57'),(5,'Eva Green','eva@example.com','5678901234','2024-10-07 12:22:57','2024-10-07 12:22:57'),(6,'Frank White','frank@example.com','6789012345','2024-10-07 12:22:57','2024-10-07 12:22:57'),(7,'Grace Lee','grace@example.com','7890123456','2024-10-07 12:22:57','2024-10-07 12:22:57'),(8,'Henry Black','henry@example.com','8901234567','2024-10-07 12:22:57','2024-10-07 12:22:57'),(9,'Ivy Adams','ivy@example.com','9012345678','2024-10-07 12:22:57','2024-10-07 12:22:57'),(10,'Jack Davis','jack@example.com','0123456789','2024-10-07 12:22:57','2024-10-07 12:22:57');
/*!40000 ALTER TABLE `userinfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-10-08 21:12:05
