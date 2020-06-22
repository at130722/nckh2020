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

 Date: 22/06/2020 20:02:16
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
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of attendance
-- ----------------------------
INSERT INTO `attendance` VALUES (1, 'at130722', '2020-06-22 03:28:36', 'at130722_1592794363');
INSERT INTO `attendance` VALUES (2, 'at130723', '2020-06-22 03:28:36', 'at130723_1592794364');
INSERT INTO `attendance` VALUES (3, 'at130722', '2020-06-22 03:28:39', 'at130722_1592794363');
INSERT INTO `attendance` VALUES (4, 'at130723', '2020-06-22 03:28:39', 'at130723_1592794364');
INSERT INTO `attendance` VALUES (5, 'at130722', '2020-06-23 01:28:40', 'at130722_1592794363');
INSERT INTO `attendance` VALUES (6, 'at130723', '2020-06-23 03:28:40', 'at130723_1592794364');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `id` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

SET FOREIGN_KEY_CHECKS = 1;
