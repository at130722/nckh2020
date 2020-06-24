/*
 Navicat Premium Data Transfer

 Source Server         : nckh
 Source Server Type    : MySQL
 Source Server Version : 80020
 Source Host           : 192.168.254.134:3306
 Source Schema         : nckh

 Target Server Type    : MySQL
 Target Server Version : 80020
 File Encoding         : 65001

 Date: 24/06/2020 11:34:00
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for attendance
-- ----------------------------
DROP TABLE IF EXISTS `attendance`;
CREATE TABLE `attendance`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `student_id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `time` datetime(0) NULL DEFAULT NULL,
  `path` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `status` int(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  INDEX `fk_student_id`(`student_id`) USING BTREE,
  CONSTRAINT `fk_student_id` FOREIGN KEY (`student_id`) REFERENCES `student` (`id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB AUTO_INCREMENT = 38 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of attendance
-- ----------------------------
INSERT INTO `attendance` VALUES (1, 'at130722', '2020-06-01 03:28:36', 'at130722_1592794363', 1);
INSERT INTO `attendance` VALUES (2, 'at130723', '2020-06-01 03:28:36', 'at130723_1592794364', 1);
INSERT INTO `attendance` VALUES (3, 'at130722', '2020-06-04 03:28:39', 'at130722_1592794363', 1);
INSERT INTO `attendance` VALUES (4, 'at130723', '2020-06-04 03:28:39', 'at130723_1592794364', 1);
INSERT INTO `attendance` VALUES (5, 'at130722', '2020-06-18 01:28:40', 'at130722_1592794363', 1);
INSERT INTO `attendance` VALUES (6, 'at130723', '2020-06-18 03:28:40', 'at130723_1592794364', 0);
INSERT INTO `attendance` VALUES (7, 'at130722', '2020-06-25 09:38:26', 'at130722_1592794363', 0);
INSERT INTO `attendance` VALUES (8, 'at130723', '2020-06-25 09:38:45', 'at130723_1592794364', 1);
INSERT INTO `attendance` VALUES (9, 'at130722', '2020-06-26 10:23:20', 'at130722_1592794363', 1);
INSERT INTO `attendance` VALUES (10, 'at130723', '2020-06-26 10:23:36', 'at130723_1592794364', 1);
INSERT INTO `attendance` VALUES (11, 'at130722', '2020-06-30 10:23:54', 'at130722_1592794363', 0);
INSERT INTO `attendance` VALUES (12, 'at130723', '2020-06-30 10:24:08', 'at130723_1592794364', 0);
INSERT INTO `attendance` VALUES (14, 'at130722', '2020-06-23 08:30:56', 'at130722_1592794363', 1);
INSERT INTO `attendance` VALUES (15, 'at130723', '2020-06-23 08:30:56', NULL, 0);
INSERT INTO `attendance` VALUES (31, 'at130723', '2020-06-24 01:57:28', 'at130723_1592794364', 1);
INSERT INTO `attendance` VALUES (37, 'at130722', '2020-06-24 02:06:08', 'at130722_1592794363', 1);

-- ----------------------------
-- Table structure for attendance_count
-- ----------------------------
DROP TABLE IF EXISTS `attendance_count`;
CREATE TABLE `attendance_count`  (
  `id` int(0) NOT NULL AUTO_INCREMENT,
  `time` datetime(0) NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 2 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of attendance_count
-- ----------------------------
INSERT INTO `attendance_count` VALUES (1, '2020-06-22 08:54:34');
INSERT INTO `attendance_count` VALUES (2, '2020-06-23 16:54:40');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('at130722', 'Nguyen Van A');
INSERT INTO `student` VALUES ('at130723', 'Nguyen Van B');

SET FOREIGN_KEY_CHECKS = 1;
