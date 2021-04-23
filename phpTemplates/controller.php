<?php

namespace FM\Controller;

use FM\Controller\FMCrud;
use Zeedhi\Framework\DTO;
use Zeedhi\Framework\DTO\Request;
use Zeedhi\Framework\DTO\Response;
use Zeedhi\Framework\DataSource\DataSet;
use FM\Service\{}Service;

class {}Controller extends FMCrud{
    protected $dataSourceName = 'fcm_checklistagend';
    protected ${}Service;
   
    public function __construct($crudService, $environment, {}Service ${}Service) {
        parent::__construct($crudService, $environment);
        $this->{}Service = ${}Service;
    }
}

?>