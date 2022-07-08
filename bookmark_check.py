import re

import requests


def is_bookmark(line):
    line = line.strip()
    if line.startswith("<DT><A HREF="):
        return True
    return False


def extract_url(bookmark):
    pattern = '(?:(?:https?|ftp):\/\/)?[\w/\-?=%.]+\.[\w/\-&?=%.]+'
    match = re.search(pattern, bookmark)
    if match:
        if match.group(0) == "window.open":
            return None
        return match.group(0)
    else:
        print("Not matched : ", bookmark)
        return None


def remove_404_and_write_to_new_file():
    count = 1
    with open('bookmark_editted/edited_bookmars_20200402.html', 'w') as w:
        with open('bookmark_original/bookmarks_4_2_21.html', 'r') as f:
            with open('bookmark_editted/not_200_list.html', 'w') as not_200:
                lines = f.readlines()
                for line in lines:
                    print(count, " of ", len(lines))
                    count += 1
                    if is_bookmark(line):
                        url = extract_url(line)
                        if url is None:
                            w.write(line)
                        else:
                            try:
                                response = requests.get(url)
                            except:
                                print(url)
                                print("-" * 80)
                                not_200.write(line)
                                continue
                            if response.status_code != 200:
                                not_200.write(line)
                                print(response.status_code)
                                print(url)
                                print("-" * 80)
                            else:
                                w.write(line)
                    else:
                        w.write(line)
            

if __name__ == "__main__":
    remove_404_and_write_to_new_file()
