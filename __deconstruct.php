<?php
class color{
    public $name;

    function __construct($name)
    {
        $this->name=$name;
    }
    function __destruct()
    {
        echo" color name is {$this->name}.";
    }
}
$color1=new color("Red");

?>