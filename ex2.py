import datetime
from dateutil.relativedelta import relativedelta


class Calendar:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, d):
        if not isinstance(d, int) or d < 0:
            raise Exception('Your day is invalid')
        self.__day = d

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, m):
        if not isinstance(m, int) or m < 0:
            raise Exception('Your month is invalid')
        self.__month = m

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, y):
        if not isinstance(y, int) or y < 0:
            raise Exception('Your year is invalid')
        self.__year = y


class Date:
    def __init__(self, day, month, year):
        if not isinstance(year, int) or year < 0:
            raise Exception('Your year is invalid')
        if not isinstance(day, int) or not 0 < day <= 31:
            raise Exception('Your day is invalid')
        if not isinstance(month, int) or not 0 < month <= 12:
            raise Exception('Your month is invalid')
        self.date = datetime.date(year, month, day)

    def __lt__(self, d):
        if not isinstance(d, Date):
            raise Exception('Your date is invalid')
        return f'{self.date} < {d.date}: ' \
               f'{self.date < d.date}'

    def __le__(self, d):
        if not isinstance(d, Date):
            raise Exception('Your date is invalid')
        return f'{self.date} <= {d.date}: ' \
               f'{self.date <= d.date}'

    def __gt__(self, d):
        if not isinstance(d, Date):
            raise Exception('Your date is invalid')
        return f'{self.date} > {d.date}: ' \
               f'{self.date > d.date}'

    def __ge__(self, d):
        if not isinstance(d, Date):
            raise Exception('Your date is invalid')
        return f'{self.date} >= {d.date}: ' \
               f'{self.date >= d.date}'

    def __eq__(self, d):
        if not isinstance(d, Date):
            raise Exception('Your date is invalid')
        return f'{self.date} == {d.date}: ' \
               f'{self.date == d.date}'

    def __ne__(self, d):
        if not isinstance(d, Date):
            raise Exception('Your date is invalid')
        return f'{self.date} != {d.date}: ' \
               f'{self.date != d.date}'

    def __iadd__(self, d):
        if not isinstance(d, Calendar):
            raise Exception('Your date is invalid')
        self.date += relativedelta(years=d.year, months=d.month, days=d.day)
        return self.date

    def __isub__(self, d):
        if not isinstance(d, Calendar):
            raise Exception('Your date is invalid')
        self.date -= relativedelta(years=d.year, months=d.month, days=d.day)
        return self.date

    def __str__(self):
        return f'{self.date}'


today = Date(2, 10, 1995,)
tomorrow = Date(24, 8, 1991)
aftertomorrow = Date(27, 11, 2022)
aftertomorrow += Calendar(month=23)
print(f'{today}\n{tomorrow}\n{today < tomorrow}\n{aftertomorrow}')
