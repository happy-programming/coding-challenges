<?php

namespace SolidFizzBuzz;

class FizzRule implements RuleInterface
{
    public function match(int $element):bool
    {
        if ($element%3==0)
        {
            return true;
        }

        return false;
    }

    public function replacement():string
    {
        return 'Fizz';
    }
}
