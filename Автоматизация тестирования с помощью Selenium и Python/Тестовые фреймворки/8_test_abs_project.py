"""
��������� ����� ����� ��������� � �����, ����� ��� ���� ������ ��������� � ������� � ������� �������� ������. �������
�������� ���� test_abs_project.py � ������� � �� ��������� ���:

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"


if __name__ == "__main__":
    test_abs1()
    print("All tests passed!")
�� ��������� �������� �������� � ������� ��� ���������� ����-������ � ����������� �� ������������ �������.

�� �������� � �����������, ������ ������, ��� ����������� if __name__ == "__main__" ������ ��� ������������� ����, ���
������ ������ ��� ������� ��������, � �� ������ ������ ������� ����� � �������� ������. ���� ��� ���������� � ����
����� ������� ����� �������� ������ ���� ������������ �������� ���� ��������������. ��������� ����� ������������ �
����� ����� ���������.

� ���� ����������� �� ������� ������� test_abs1(), ������� ��������� �������� ��������.

� ������� print("All tests passed!") �� ������ ���������, ���� ��� ����� ������ �������.

����� ��������� ����, ��������� � ������� �������:
python test_abs_project.py

�� ������ ������� � ������� ��������� "All tests passed!".



���� ��� ����� �������� ��� ���� ����, �� ����� �������� ��� ��� ������� � ���� �� �����. � ����������� ������� �� ���
�� ������ ��������� "Everything passed", ��� ��� ������� ������ ����� �������� ����� �� ���������:

def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"

def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"

if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")
��������� ���� �����. �� ������ ������� ��������� �� ������� ������ �����:


$ python test_abs_project.py

Traceback (most recent call last):

  File "test_abs_project.py", line 9, in <module>

    test_abs2()

  File "test_abs_project.py", line 5, in test_abs2

    assert abs(-42) == -42, "Should be absolute value of a number"

AssertionError: Should be absolute value of a number
"""


def test_abs1():
    assert abs(-42) == 42, "Should be absolute value of a number"


def test_abs2():
    assert abs(-42) == -42, "Should be absolute value of a number"


if __name__ == "__main__":
    test_abs1()
    test_abs2()
    print("Everything passed")
