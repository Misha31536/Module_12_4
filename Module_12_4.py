import logging
import unittest
from Module_12_4_Test import Runner, Tournament


logging.basicConfig(level=logging.INFO, filename='runner_tests.log', filemode='w', encoding='utf-8',
                        format='%(asctime)s | %(funcName)s | %(module)s | %(levelname)s: %(message)s')
class RunnerTest(unittest.TestCase):


    def test_walk(self):
        try:
            tw = Runner('Test1', speed=-2)
            for walk in range(10):
                tw.walk()

            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)


    def test_run(self):
        try:
            tr = Runner(2)
            for run in range(10):
                tr.run()
            self.assertEqual(tr.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)


if __name__ == '__main__':
    unittest.main()