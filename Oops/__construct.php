<?php
  class computerparts {
     public $name;
      function __construct($name){
        $this->name=$name;
      }
      function get_name(){
        return $this->name;
      }

  }
  $computer1=new computerparts("Mouse<br>");
  echo $computer1->get_name();
  $computer1=new computerparts("CPU");
  echo $computer1->get_name();

?>