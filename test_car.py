import pytest
from car import Car
from testdata import cars

class TestCar():
    def test_accelerate(self):
        car = Car()
        assert car.accelerate() == "faster"
        assert car.speed == 0


    def test_brake(self):
        car = Car()
        assert car.brake() == "brake"

    def test_new_car(self, setup_teardown, newcar, logger):
        logger.warning("creating car")
        car = newcar
        assert car.speed == 0

    def test_environments(self, env, logger):
        #pytest -k test_environment
        #pytest -k test_environment --env=dev
        #pytest -k test_environment --env=dev --url=haha
        #export TEST_USERNAME=bas --> pytest -k test_environment
        url = env["url"]
        username = env["username"]
        password = env["password"]
        logger.info(url)
        logger.info(username)
        logger.info(password)

    @pytest.mark.parametrize("speed, expected_speed, color, expected_color", cars)
    def test_parameters(self, logger, newcar, speed, expected_speed, color, expected_color):
        newcar.set_speed(speed)
        newcar.set_color(color)
        assert newcar.speed == speed
        assert newcar.color == expected_color








