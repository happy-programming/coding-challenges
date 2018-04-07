<?php

namespace SolidFizzBuzz;


class FizzBuzzRule implements RuleInterface
{
    public function match(int $element):bool
    {
        if ($element%3==0 && $element%5==0)
        {
            return true;
        }

        return false;
    }

    public function replacement():string
    {
        return 'FizzBuzz';
    }
}
