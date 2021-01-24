from underline import Underline


def main():
    _ = Underline(url="https://suyambu.net")

    print("""
Title: {}
Story Count: {}
Url: {}
    """.format(_.title(), _.css(".story").size(), _.url))

    links = _.css("a").map(lambda el: el.href()).to_set()
    for link in links:
        _.follow(url=link)
        print("""
Title: {}
Story Count: {}
Url: {}


        """.format(_.title(), _.css(".story").size(), _.url))


if __name__ == '__main__':
    main()
