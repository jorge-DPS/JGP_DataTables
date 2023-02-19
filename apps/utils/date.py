# -*- encoding:utf-8 -*-
import pytz
import calendar
from django.conf import settings
from django.utils import timezone
from django.utils.timezone import utc
from django.utils.translation import ugettext_lazy as _
from datetime import datetime, timedelta
from calendar import monthrange


def now():
    """ returns the current date and time in UTC format (datetime object) """
    return datetime.utcnow().replace(tzinfo=utc)


def now_after(**kwargs):
    """ returns the current date and time plus the time (seconds, minutes, hours, days, years) specified """
    return now() + timedelta(**kwargs)


def ago(**kwargs):
    """ returns the current date and time minus the time (seconds, minutes, hours, days, years) specified """
    return now() - timedelta(**kwargs)


def after(date, **kwargs):
    """
    returns the result of the calculation of the date param plus the time (seconds, minutes, hours, days, years) specified

    :paramm datetime: datetime object to which add more time
    """
    return date + timedelta(**kwargs)


def localized_datetime(_datetime=None, tz=pytz.timezone(settings.TIME_ZONE)):
    if _datetime is None:
        _datetime = timezone.now()
    return timezone.localtime(_datetime, timezone=tz)


def localized_datetime_simple(_datetime):
    if _datetime:
        dt = localized_datetime(_datetime)

        _time = str(dt.time())
        if len(_time) > 5:
            _time = _time[:5]

        _date = str(_datetime.date())
        if len(_date) > 10:
            _date = _date[:10]
        return "%s %s" % (_date, _time)
    return None


def localized_date(_datetime):
    if _datetime:
        dt = localized_datetime(_datetime)
        _date = str(dt.date())
        if len(_date) > 10:
            _date = _date[:10]
        return "%s" % _date
    return None


def simple_date(_datetime):
    if _datetime:
        _date = str(_datetime.date())
        if len(_date) > 10:
            _date = _date[:10]
        return "%s" % _date
    return None


def get_month_str(month):
    if month == 1:
        return _("ENERO")
    elif month == 2:
        return _("FEBRERO")
    elif month == 3:
        return _("MARZO")
    elif month == 4:
        return _("ABRIL")
    elif month == 5:
        return _("MAYO")
    elif month == 6:
        return _("JUNIO")
    elif month == 7:
        return _("JULIO")
    elif month == 8:
        return _("AGOSTO")
    elif month == 9:
        return _("SEPTIEMBRE")
    elif month == 10:
        return _("OCTUBRE")
    elif month == 11:
        return _("NOVIEMBRE")
    elif month == 12:
        return _("DICIEMBRE")


def find_day(year, month, day):
    day_number = calendar.weekday(year, month, day)
    days = ["L", "M", "M", "J", "V", "S", "D"]
    return days[day_number]


def get_range_of_days(year, mon):
    total_days = monthrange(year, mon)[1]
    days = []
    for day in range(1, total_days + 1):
        days.append({
            "n": day,
            "w": find_day(year, mon, day)
        })
    return days
