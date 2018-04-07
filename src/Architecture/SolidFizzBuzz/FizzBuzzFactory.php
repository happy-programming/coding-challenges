<?php

namespace SolidFizzBuzz;

// todo add from config
class FizzBuzzFactory
{
   protected $rules = [];

   public function addRules(RuleInterface $rule)
   {
        array_push($this->rules, $rule);
   }

   public function getRules()
   {
        return $this->rules;
   }

}
