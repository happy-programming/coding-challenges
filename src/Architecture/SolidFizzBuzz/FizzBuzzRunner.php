<?php

namespace SolidFizzBuzz;

require_once('FizzBuzz.php');
require_once('RuleInterface.php');
require_once('FizzBuzzFactory.php');

require_once('Rules/BuzzRule.php');
require_once('Rules/FizzRule.php');
require_once('Rules/FizzBuzzRule.php');


class FizzBuzzRunner
{
    public function run()
    {
        $fizzBuzz = new FizzBuzz();
        $fizzBuzz->factory->addRules(new FizzBuzzRule());
        $fizzBuzz->factory->addRules(new FizzRule());
        $fizzBuzz->factory->addRules(new BuzzRule());

        $result = $fizzBuzz->generateList(1,100);

        foreach($result as $element)
        {
            print $element;
            print "\n";
        }

    }
}

(new FizzBuzzRunner())->run();
