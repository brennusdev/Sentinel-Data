from streaming.retry import (
    next_retry_count,
    should_retry,
)


def test_retry_allowed():

    assert should_retry(
        0
    ) is True

    assert should_retry(
        1
    ) is True

    assert should_retry(
        2
    ) is True


def test_retry_limit():

    assert should_retry(
        3
    ) is False


def test_retry_increment():

    assert next_retry_count(
        0
    ) == 1

    assert next_retry_count(
        2
    ) == 3