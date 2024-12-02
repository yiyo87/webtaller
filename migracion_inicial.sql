--
-- Create model Pedido
--
CREATE TABLE `elcedroapp_pedido` (`id` bigint AUTO_INCREMENT NOT NULL PRIMARY KEY, `nombre` varchar(100) NOT NULL, `direccion` longtext NOT NULL, `numero` varchar(20) NOT NULL, `cantidad_bidones` integer UNSIGNED NOT NULL CHECK (`cantidad_bidones` >= 0));
