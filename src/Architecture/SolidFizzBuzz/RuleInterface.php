<?php

namespace SolidFizzBuzz;

interface RuleInterface
{
    public function match(int $element):bool;

    public function replacement();
}
