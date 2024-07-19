-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Database: airlinedbms
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `airport`
--

DROP TABLE IF EXISTS `airport`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airport` (
  `airport_id` int NOT NULL AUTO_INCREMENT,
  `airport_name` varchar(100) NOT NULL,
  `city` varchar(50) NOT NULL,
  `latitude` decimal(10,8) DEFAULT NULL,
  `longitude` decimal(11,8) DEFAULT NULL,
  PRIMARY KEY (`airport_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airport`
--

LOCK TABLES `airport` WRITE;
/*!40000 ALTER TABLE `airport` DISABLE KEYS */;
INSERT INTO `airport` VALUES (1,'Los Angeles International Airport','Los Angeles',33.94250000,-118.40810000),(2,'Heathrow Airport','London',51.47000000,-0.45430000),(3,'Tokyo Haneda Airport','Tokyo',35.55330000,139.78110000),(4,'Dubai International Airport','Dubai',25.25320000,55.36570000),(5,'Singapore Changi Airport','Singapore',1.36440000,103.99150000),(6,'Sydney Kingsford Smith Airport','Sydney',-33.94610000,151.17720000),(7,'Denver International Airport','Denver',39.85610000,-104.67370000),(8,'Hong Kong International Airport','Hong Kong',22.30800000,113.91850000),(9,'Frankfurt Airport','Frankfurt',50.03360000,8.57060000),(10,'Incheon International Airport','Incheon',37.46920000,126.45050000);
/*!40000 ALTER TABLE `airport` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `airport_employee_management`
--

DROP TABLE IF EXISTS `airport_employee_management`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airport_employee_management` (
  `airport_id` int NOT NULL,
  `emp_id` int NOT NULL,
  PRIMARY KEY (`airport_id`,`emp_id`),
  KEY `emp_id` (`emp_id`),
  CONSTRAINT `airport_employee_management_ibfk_1` FOREIGN KEY (`airport_id`) REFERENCES `airport` (`airport_id`),
  CONSTRAINT `airport_employee_management_ibfk_2` FOREIGN KEY (`emp_id`) REFERENCES `employee` (`emp_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airport_employee_management`
--

LOCK TABLES `airport_employee_management` WRITE;
/*!40000 ALTER TABLE `airport_employee_management` DISABLE KEYS */;
INSERT INTO `airport_employee_management` VALUES (1,1),(1,2),(2,3),(2,4),(3,5),(3,6),(4,7),(4,8),(5,9),(5,10);
/*!40000 ALTER TABLE `airport_employee_management` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `airport_flight_management`
--

DROP TABLE IF EXISTS `airport_flight_management`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `airport_flight_management` (
  `airport_id` int NOT NULL,
  `flight_id` int NOT NULL,
  PRIMARY KEY (`airport_id`,`flight_id`),
  KEY `flight_id` (`flight_id`),
  CONSTRAINT `airport_flight_management_ibfk_1` FOREIGN KEY (`airport_id`) REFERENCES `airport` (`airport_id`),
  CONSTRAINT `airport_flight_management_ibfk_2` FOREIGN KEY (`flight_id`) REFERENCES `flight` (`flight_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `airport_flight_management`
--

LOCK TABLES `airport_flight_management` WRITE;
/*!40000 ALTER TABLE `airport_flight_management` DISABLE KEYS */;
INSERT INTO `airport_flight_management` VALUES (1,1),(2,2),(3,3),(4,4),(5,5);
/*!40000 ALTER TABLE `airport_flight_management` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `emp_id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(256) NOT NULL,
  `is_admin` tinyint(1) NOT NULL,
  `name` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phno` varchar(20) DEFAULT NULL,
  `role` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`emp_id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'admin1','password1',1,'Admin One','admin1@example.com','1234567890','admin'),(2,'admin2','password2',1,'Admin Two','admin2@example.com','1234567891','admin'),(3,'admin3','password3',1,'Admin Three','admin3@example.com','1234567892','admin'),(4,'admin4','password4',1,'Admin Four','admin4@example.com','1234567893','admin'),(5,'admin5','password5',1,'Admin Five','admin5@example.com','1234567894','admin'),(6,'pilot1','password6',0,'Pilot One','pilot1@example.com','1234567895','pilot'),(7,'pilot2','password7',0,'Pilot Two','pilot2@example.com','1234567896','pilot'),(8,'pilot3','password8',0,'Pilot Three','pilot3@example.com','1234567897','pilot'),(9,'pilot4','password9',0,'Pilot Four','pilot4@example.com','1234567898','pilot'),(10,'pilot5','password10',0,'Pilot Five','pilot5@example.com','1234567899','pilot'),(11,'attendant1','password11',0,'Attendant One','attendant1@example.com','1234567800','attendant'),(12,'attendant2','password12',0,'Attendant Two','attendant2@example.com','1234567801','attendant'),(13,'attendant3','password13',0,'Attendant Three','attendant3@example.com','1234567802','attendant'),(14,'attendant4','password14',0,'Attendant Four','attendant4@example.com','1234567803','attendant'),(15,'attendant5','password15',0,'Attendant Five','attendant5@example.com','1234567804','attendant'),(16,'mechanic1','password16',0,'Mechanic One','mechanic1@example.com','1234567805','mechanic'),(17,'mechanic2','password17',0,'Mechanic Two','mechanic2@example.com','1234567806','mechanic'),(18,'mechanic3','password18',0,'Mechanic Three','mechanic3@example.com','1234567807','mechanic'),(19,'mechanic4','password19',0,'Mechanic Four','mechanic4@example.com','1234567808','mechanic'),(20,'mechanic5','password20',0,'Mechanic Five','mechanic5@example.com','1234567809','mechanic'),(21,'ground1','password21',0,'Ground Staff One','ground1@example.com','1234567810','ground staff'),(22,'ground2','password22',0,'Ground Staff Two','ground2@example.com','1234567811','ground staff'),(23,'ground3','password23',0,'Ground Staff Three','ground3@example.com','1234567812','ground staff'),(24,'ground4','password24',0,'Ground Staff Four','ground4@example.com','1234567813','ground staff'),(25,'ground5','password25',0,'Ground Staff Five','ground5@example.com','1234567814','ground staff');
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_flight_assignment`
--

DROP TABLE IF EXISTS `employee_flight_assignment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_flight_assignment` (
  `emp_id` int NOT NULL,
  `flight_id` int NOT NULL,
  PRIMARY KEY (`emp_id`,`flight_id`),
  KEY `flight_id` (`flight_id`),
  CONSTRAINT `employee_flight_assignment_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employee` (`emp_id`),
  CONSTRAINT `employee_flight_assignment_ibfk_2` FOREIGN KEY (`flight_id`) REFERENCES `flight` (`flight_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_flight_assignment`
--

LOCK TABLES `employee_flight_assignment` WRITE;
/*!40000 ALTER TABLE `employee_flight_assignment` DISABLE KEYS */;
INSERT INTO `employee_flight_assignment` VALUES (5,1),(6,1),(7,2),(8,2),(9,3),(10,3),(1,4),(2,4),(3,5),(4,5);
/*!40000 ALTER TABLE `employee_flight_assignment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `employee_task_assignment`
--

DROP TABLE IF EXISTS `employee_task_assignment`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee_task_assignment` (
  `emp_id` int NOT NULL,
  `task_id` int NOT NULL,
  PRIMARY KEY (`emp_id`,`task_id`),
  KEY `task_id` (`task_id`),
  CONSTRAINT `employee_task_assignment_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employee` (`emp_id`),
  CONSTRAINT `employee_task_assignment_ibfk_2` FOREIGN KEY (`task_id`) REFERENCES `task` (`task_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee_task_assignment`
--

LOCK TABLES `employee_task_assignment` WRITE;
/*!40000 ALTER TABLE `employee_task_assignment` DISABLE KEYS */;
INSERT INTO `employee_task_assignment` VALUES (1,1),(2,1),(3,2),(4,2),(5,3),(6,3),(7,4),(8,4),(9,5),(10,5);
/*!40000 ALTER TABLE `employee_task_assignment` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `flight`
--

DROP TABLE IF EXISTS `flight`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `flight` (
  `flight_id` int NOT NULL AUTO_INCREMENT,
  `flight_no` varchar(20) NOT NULL,
  `departure_city` varchar(50) NOT NULL,
  `arrival_city` varchar(50) NOT NULL,
  `depature_time` datetime NOT NULL,
  `arrival_time` datetime NOT NULL,
  `aircraft_model` varchar(50) NOT NULL,
  PRIMARY KEY (`flight_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `flight`
--

LOCK TABLES `flight` WRITE;
/*!40000 ALTER TABLE `flight` DISABLE KEYS */;
INSERT INTO `flight` VALUES (1,'FL001','Los Angeles','Heathrow','2023-11-15 08:00:00','2023-11-15 16:00:00','Boeing 777'),(2,'FL002','Tokyo','Dubai','2023-11-16 12:00:00','2023-11-16 18:00:00','Airbus A380'),(3,'FL003','Singapore','Sydney','2023-11-17 10:00:00','2023-11-17 18:30:00','Boeing 747'),(4,'FL004','Denver','Hong Kong','2023-11-18 09:30:00','2023-11-18 20:00:00','Airbus A330'),(5,'FL005','Frankfurt','Incheon','2023-11-19 11:30:00','2023-11-19 18:30:00','Boeing 787');
/*!40000 ALTER TABLE `flight` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `task`
--

DROP TABLE IF EXISTS `task`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `task` (
  `task_id` int NOT NULL AUTO_INCREMENT,
  `descrip` text NOT NULL,
  `deadline` datetime NOT NULL,
  `status` varchar(20) NOT NULL DEFAULT 'Not Started',
  `roles_req` varchar(50) NOT NULL,
  PRIMARY KEY (`task_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `task`
--

LOCK TABLES `task` WRITE;
/*!40000 ALTER TABLE `task` DISABLE KEYS */;
INSERT INTO `task` VALUES (1,'Flight Planning','2023-11-15 10:00:00','Not Started','pilot'),(2,'Pre-flight Checks','2023-11-16 14:00:00','Not Started','pilot'),(3,'In-flight Navigation','2023-11-17 12:00:00','Not Started','pilot'),(4,'Post-flight Checks','2023-11-18 16:00:00','Not Started','pilot'),(5,'Cabin Preparation','2023-11-15 09:30:00','Not Started','attendant'),(6,'Passenger Assistance','2023-11-16 15:30:00','Not Started','attendant'),(7,'Emergency Response Training','2023-11-17 11:00:00','Not Started','attendant'),(8,'In-flight Service','2023-11-18 17:30:00','Not Started','attendant'),(9,'Aircraft Inspection','2023-11-15 10:30:00','Not Started','mechanic'),(10,'Engine Maintenance','2023-11-16 14:30:00','Not Started','mechanic'),(11,'Avionics Check','2023-11-17 12:30:00','Not Started','mechanic'),(12,'Landing Gear Inspection','2023-11-18 16:30:00','Not Started','mechanic'),(13,'Baggage Handling','2023-11-15 09:00:00','Not Started','ground staff'),(14,'Check-in Assistance','2023-11-16 15:00:00','Not Started','ground staff'),(15,'Security Check','2023-11-17 11:30:00','Not Started','ground staff'),(16,'Gate Operations','2023-11-18 17:00:00','Not Started','ground staff');
/*!40000 ALTER TABLE `task` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-11-15 22:50:46
