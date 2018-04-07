<?php

namespace SolidFizzBuzz;

class FizzBuzz
{
    public $factory;
    protected $rules;

    public function __construct()
    {
        $this->factory = new FizzBuzzFactory();
    }

    private function allRules()
    {
        return $this->factory->getRules();
    }

    public function generateList(int $start, int $end): array
    {
        $elementList = [];
        $this->rules = $this->allRules();

        for($i = $start; $i<=$end; $i++)
        {
            array_push($elementList, $this->generateElement($i));
        }

        return $elementList;
    }

    private function generateElement(int $element)
    {
         foreach($this->rules as $rule)
         {
            if ($rule->match($element))
            {
                return $rule->replacement();
            }
         }

         return $element;
    }

}


