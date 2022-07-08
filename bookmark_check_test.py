from bookmark_check import extract_url, is_bookmark


def test_is_bookmark():
    print(is_bookmark("      <DT><A HREF="))
    print(is_bookmark("a<DT><A HREF="))
    print(is_bookmark("<!DOCTYPE NETSCAPE-Bookmark-file-1>"))


def test_extract_url():
    result1 = extract_url("hello")
    result2 = extract_url("http://example.com")
    result3 = extract_url('<DT><A HREF="https://refe.tistory.com/entry/%EC%85%80%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-2%EC%9D%BC%EC%B0%A8" ADD_DATE="1471783940" ICON="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABAAAAAQCAYAAAAf8/9hAAAAvklEQVQ4ja3TMWoCQRTG8Z9RUwUhxGIhR7DyKrmAV5A9QY7hEdJob2WhZ0hhl5zBQi00xb7gMLgrK/7h8d7MfHwwHzM8kGcU0f95jWrSgD4+sY3exRjrqHHspZp+alDgG+foQ0xjfY55mGkK4QoHvOEdX1hijxF+McNPmKSa060MBlG1mk4eRsILPmJeYNegvcoEx6hJneiprWtOr+Fsrkqc6gp3kYfYivwhtaZ0eUhlnagpgxU2yXwX+Wd6PH/ZICX/oSVlEQAAAABJRU5ErkJggg=="> 셀스크립트</A>')
    print(result1)
    print(result2)
    print(result3)


if __name__ == "__main__":
    # is_bookmark_test()
    test_extract_url()
