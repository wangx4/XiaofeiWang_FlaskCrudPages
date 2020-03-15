/*
 Navicat Premium Data Transfer

 Source Server         : xfw
 Source Server Type    : MySQL
 Source Server Version : 80019
 Source Host           : localhost:3306
 Source Schema         : shoppinglist

 Target Server Type    : MySQL
 Target Server Version : 80019
 File Encoding         : 65001

 Date: 16/03/2020 00:14:37
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for product
-- ----------------------------
DROP TABLE IF EXISTS `product`;
CREATE TABLE `product`  (
  `ProductID` int(0) NOT NULL,
  `ProductName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
  `ProductUnitPrice` int(10) UNSIGNED ZEROFILL NULL DEFAULT NULL,
  PRIMARY KEY (`ProductID`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of product
-- ----------------------------
INSERT INTO `product` VALUES (1, 'Apple', 0000000010);
INSERT INTO `product` VALUES (2, 'Pear', 0000000008);
INSERT INTO `product` VALUES (3, 'beef', 0000000050);
INSERT INTO `product` VALUES (4, 'Orange', 0000000006);
INSERT INTO `product` VALUES (5, 'pork', 0000000080);
INSERT INTO `product` VALUES (6, 'hamburger', 0000000015);

SET FOREIGN_KEY_CHECKS = 1;
