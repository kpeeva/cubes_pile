"""Calculate the volume of all cubes based on their sides and verify if
a pile can be built through checking if the cube's side added to the pile
is smaller and equal to the last one added.
Unit tests included.
Python 3.9"""

from unittest.mock import patch


# Calculating the volume and checking if a pile can be built or not with several constraints.
def pile_of_cubes():
    test_cases = int(input())
    if 1 <= test_cases <= 5:
        for i in range(test_cases):
            sideLengths = []
            number_cubes = int(input())
            if 1 <= number_cubes <= 10 ** 5:
                pile_volume = 0
                for j in range(number_cubes):
                    length = int(input())
                    if 1 <= length < 2 ** 31:
                        sideLengths.append(length)
                        cube_volume = length ** 3  # volume of a cube is the cube of its side length
                        pile_volume += cube_volume
                    else:
                        print("Invalid input")
                        break
                else:
                    max_cube = max(sideLengths)
                    result = [max_cube]
                    for n in range(number_cubes - 1):
                        if sideLengths[-1] <= sideLengths[0] <= result[-1]:
                            max_cube = sideLengths.pop(0)
                        elif sideLengths[0] < sideLengths[-1] <= result[-1]:
                            max_cube = sideLengths.pop()
                        else:
                            print("No", pile_volume)
                            break
                        result.append(max_cube)
                    else:
                        print("Yes", pile_volume)
            else:
                print("Invalid input")
    else:
        print("Invalid input")


# Unit test for checking right input
def test_pile_of_cubes_valid_input():
    expected_output = ["Yes 36", "No 100"]
    with patch('builtins.input', side_effect=['2', '3', '1', '2', '3', '4', '1', '3', '4', '2']):
        assert [pile_of_cubes() for i in range(2)] == expected_output


# Unit test for checking invalid input
def test_pile_of_cubes_invalid_input():
    expected_output = "Invalid input"
    with patch('builtins.input', side_effect=['1', '100001']):
        assert pile_of_cubes() == expected_output
