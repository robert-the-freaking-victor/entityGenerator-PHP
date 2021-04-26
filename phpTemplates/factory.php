<?php

namespace FM\Factory;

use Doctrine\ORM\EntityManager;

class {}Factory {
    protected $connection;

    public function __construct(EntityManager $entityManager) {
        $this->connection = $entityManager->getConnection();
    }
}

?>