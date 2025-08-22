-- Base de datos y tablas (MySQL)
CREATE DATABASE IF NOT EXISTS `hidrostal` CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE `hidrostal`;

-- Tabla usuarios
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `username` VARCHAR(80) NOT NULL UNIQUE,
  `email` VARCHAR(120) UNIQUE,
  `password_hash` VARCHAR(255) NOT NULL,
  `role` ENUM('admin','worker') NOT NULL DEFAULT 'worker',
  `is_active` TINYINT(1) NOT NULL DEFAULT 1,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Tabla documentos
DROP TABLE IF EXISTS `documents`;
CREATE TABLE `documents` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `year` INT NOT NULL,
  `month` VARCHAR(20) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `plan_number` VARCHAR(64) NOT NULL,
  `size` VARCHAR(4) NOT NULL,
  `version` VARCHAR(16) NOT NULL,
  `drafter` VARCHAR(120) NOT NULL,
  `drawn_in` VARCHAR(50) NOT NULL,
  `pdf_filename` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created_by_id` INT,
  INDEX (`plan_number`),
  CONSTRAINT `fk_documents_user` FOREIGN KEY (`created_by_id`) REFERENCES `users`(`id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- Usuario administrador por defecto
-- Hash generado con Werkzeug (pbkdf2:sha256) para 'Admin123!'
INSERT INTO `users` (`username`, `password_hash`, `role`, `is_active`) VALUES (
  'admin',
  'pbkdf2:sha256:600000$LGAwJ9wbwBLW4UqC$5d9bb21d7cb3fd1a9b6de6a2d72e4318319905b0d3d81d692dc58ed4a5b6a68c',
  'admin', 1
) ON DUPLICATE KEY UPDATE `username`=`username`;