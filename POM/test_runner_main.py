import pytest

import time


def runner():
    how_time = time.strftime('%Y-%m-%d %H-%M-%S')
    pytest.main(['-s', '-v', './test_pytest/test_case.py',
                 '--html=./report/{}.html'.format(how_time),
                 '--capture=sys',
                 "--maxfail", "5",
                 '--reruns', '1'])


if __name__ == '__main__':
    runner()
