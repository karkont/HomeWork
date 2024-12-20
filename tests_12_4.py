import logging
import unittest


logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log", encoding='utf-8',
                        format="%(asctime)s | %(levelname)s | %(message)s")

class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            runner = Runner("Test Runner Walk", -5)
        except ValueError:
            logging.warning("Неверная скорость для Runner", exc_info=True)
        else:
            runner.distance = 0
            for _ in range(10):
                runner.walk()
            self.assertEqual(runner.distance, 50)
            logging.info('"test_walk" выполнен успешно', exc_info=True)

    def test_run(self):
        try:
            runner = Runner(12345)
        except TypeError:
            logging.warning("Неверный тип данных для объекта Runner", exc_info=True)
        else:
            runner.distance = 0
            for _ in range(10):
                runner.run()
            self.assertEqual(runner.distance, 100)
            logging.info('"test_run" выполнен успешно', exc_info=True)

    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)



first = Runner('Вося', 10)
second = Runner('Илья', 5)
# # third = Runner('Арсен', 10)
#
t = Tournament(101, first, second)
print(t.start())

if __name__ == "__main__":
    unittest.main()