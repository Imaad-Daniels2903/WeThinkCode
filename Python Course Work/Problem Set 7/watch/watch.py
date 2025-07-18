import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if match := re.search(r"^<iframe (.+ )?src=\"(?P<url>(?P<security>https?)://(?P<www>www.)?youtu(?P<extn>be\.com/embed)/[a-zA-Z0-9]+)\"( .+)?></iframe>$", s):
        url = match.group("url")
        repl = match.group("extn")
        security = match.group("security")
        www = match.group("www")
        output = url.replace(repl, ".be")
        if not www == None:
            output = output.replace(www, "")
        output = output.replace(security, "https")
        return output

    else:
        return None



if __name__ == "__main__":
    main()
