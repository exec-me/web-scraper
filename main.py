import scraper


def main():
    d = scraper.get_structure('https://timetable.spbu.ru/AMCP/StudentGroupEvents/Primary/304448')
    print(d['time'])
    print(d['subject'])


if __name__ == '__main__':
    main()
