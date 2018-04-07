<?php

namespace SolidFizzBuzz;

class BuzzRule implements RuleInterface
{
    public function match(int $element):bool
    {
        if ($element%5==0)
        {
            return true;
        }

        return false;
    }

    public function replacement():string
    {
        return 'Buzz';
    }
}
