from hypothesis import given, strategies as st
from processor import sanitize_string, parse_int_list, reverse_words


@given(st.text() | st.none())
def test_sanitize_string_no_crash(s):
    try:
        result = sanitize_string(s)
    except Exception as e:
        assert False, f"sanitize_string crashed with input={s!r}, error={e}"

    assert isinstance(result, str)


@given(st.text() | st.none())
def test_parse_int_list_safe(s):
    try:
        result = parse_int_list(s)
    except Exception as e:
        assert False, f"parse_int_list crashed with input={s!r}, error={e}"

    assert isinstance(result, list)
    for elem in result:
        assert isinstance(elem, int)


@given(st.text() | st.none())
def test_reverse_words_safe(s):
    try:
        result = reverse_words(s)
    except Exception as e:
        assert False, f"reverse_words crashed with input={s!r}, error={e}"

    assert isinstance(result, str)
