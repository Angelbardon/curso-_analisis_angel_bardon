-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema DB_employers
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `DB_employers` ;

-- -----------------------------------------------------
-- Schema DB_employers
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `DB_employers` DEFAULT CHARACTER SET utf8 ;
USE `DB_employers` ;

-- -----------------------------------------------------
-- Table `DB_employers`.`company`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DB_employers`.`company` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `cif` VARCHAR(10) NULL,
  `fundacion_year` YEAR NULL,
  `address` VARCHAR(45) NULL,
  `phone` VARCHAR(9) NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DB_employers`.`employes_copy1`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DB_employers`.`employes_copy1` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `nif` VARCHAR(9) NULL,
  `first_name` VARCHAR(45) NULL,
  `available` BIT(1) NULL,
  `job_rolerl` VARCHAR(45) NULL,
  `job_level` VARCHAR(45) NULL,
  `company_id` INT NULL,
  PRIMARY KEY (`id`),
  CONSTRAINT `fk_employes_company`
    FOREIGN KEY ()
    REFERENCES `DB_employers`.`company` ()
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE UNIQUE INDEX `nif_UNIQUE` ON `DB_employers`.`employes_copy1` (`nif` ASC) VISIBLE;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `DB_employers`.`company`
-- -----------------------------------------------------
START TRANSACTION;
USE `DB_employers`;
INSERT INTO `DB_employers`.`company` (`id`, `cif`, `fundacion_year`, `address`, `phone`) VALUES (, '32323232z', 1992, 'lago leman', '666777888');
INSERT INTO `DB_employers`.`company` (`id`, `cif`, `fundacion_year`, `address`, `phone`) VALUES (DEFAULT, '24442443lj', 1988, 'tierra', '655555555');
INSERT INTO `DB_employers`.`company` (`id`, `cif`, `fundacion_year`, `address`, `phone`) VALUES (DEFAULT, '45544556h', 1890, 'marte', '998988898');

COMMIT;

