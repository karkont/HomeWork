import unittest

class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0


    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(False, "")
    def test_walk(self):
        runner = Runner("Test Runner Walk")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @unittest.skipIf(False, "")
    def test_run(self):
        runner = Runner("Test Runner Run")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @unittest.skipIf(False, "")
    def test_challenge(self):
        runner1 = Runner("Runner 1")
        runner2 = Runner("Runner 2")

        for _ in range(10):
            runner1.run()
            runner2.walk()

        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == '__main__':
    unittest.main()
