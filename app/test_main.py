import pytest

from app.main import check_password


class TestCheckPasswordClass:
    @pytest.mark.parametrize(
        "password, result",
        [
            pytest.param("", False,
                         id="test password digits less than 0"),
            pytest.param("qwerty7!2qQfewf123312QqqQQ", False,
                         id="test password digits more than 16"),
            pytest.param("qwerty7!2qQQqqQQ", True,
                         id="test password digits at least 8 characters"),
            pytest.param("fwenbuFJI123", False,
                         id="test password is not latin alphabet "),
            pytest.param("апцутшщ123!Ааьтуцшщ", False,
                         id="test password did not have special character "),
            pytest.param("gcBhuiFа321!@@#", False,
                         id="test password has not latin alphabet")
        ]
    )
    def test_only_latin_digits_0_to_9_special_character(self,
                                                        password: str,
                                                        result: bool
                                                        ) -> None:
        assert check_password(password) == result
