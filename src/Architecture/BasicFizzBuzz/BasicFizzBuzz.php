<?php

declare(strict_types=1);

class FizzBuzz {

    public function generateList(int $start, int $end): array
    {
        $elementList = [];

        for($i = $start; $i<=$end; $i++)
        {
            array_push($elementList, self::generateElement($i));
        }

        return $elementList;
    }

    private static function generateElement(int $element)
    {
        if ($element%3==0 && $element%5==0)
        {
            return 'FizzBuzz';
        }

        if ($element%3==0)
        {
            return 'Fizz';
        }

        if ($element%5==0)
        {
            $integerList[$i] = 'Buzz';
        }

        return $element;
    }
}

class FizzBuzzRunner
{
    public function run()
    {
        $fizzBuzz = new FizzBuzz();
        $result = $fizzBuzz->generateList(1,100);
        foreach($result as $element)
        {
            print $element;
            print "\n";
        }
    }
}

(new FizzBuzzRunner())->run();

