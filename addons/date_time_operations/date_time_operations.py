from .actions import CurrentDate, CurrentTimestamp, GetDaysBetweenTwoDates, GetHoursBetweenTwoDates, GetMinutesBetweenTwoDates, GetSecondsBetweenTwoDates, GetDateInFormat, GetCurrentDate, GetDayOfMonth, GetDayOfWeek, GetDayOfYear, GetHour, GetHourInStringFormat, GetMillis, GetMillisOfDay, GetMillisOfSecond, GetMinutesOfDay, GetMinutesOfHour, GetMonthName, GetMonthOfYear, GetSecondsOfDay, GetSecondsOfMinute, GetWeekOfYear, GetFullYear, SetDays, SetHours, SetMillis, SetMinutes, SetMonths, SetSeconds, SetWeeks, SetYears


class DateTimeOperations:
    @staticmethod
    def currentdate(format: str) -> CurrentDate:
        """Get current date.

        Returns the current DateTime.
        """
        return CurrentDate(format)

    @staticmethod
    def currenttimestamp() -> CurrentTimestamp:
        """Get the current timestamp.

        Returns a moment in the datetime continuum specified as a number of milliseconds from January 1st 1970.
        """
        return CurrentTimestamp()

    @staticmethod
    def getdaysbetweentwodates(firstDateTime: str, firstDateTimeFormat: str, secondDateTime: str, secondDateTimeFormat: str) -> GetDaysBetweenTwoDates:
        """How many days are between {{firstDateTime}} to {{secondDateTime}}?.

        Returns the amount of days between two given DateTime objects.
        """
        return GetDaysBetweenTwoDates(firstDateTime, firstDateTimeFormat, secondDateTime, secondDateTimeFormat)

    @staticmethod
    def gethoursbetweentwodates(firstDateTime: str, firstDateTimeFormat: str, secondDateTime: str, secondDateTimeFormat: str) -> GetHoursBetweenTwoDates:
        """How many hours are between {{firstDateTime}} to {{secondDateTime}}?.

        Returns the amount of hours between two given DateTime objects.
        """
        return GetHoursBetweenTwoDates(firstDateTime, firstDateTimeFormat, secondDateTime, secondDateTimeFormat)

    @staticmethod
    def getminutesbetweentwodates(firstDateTime: str, firstDateTimeFormat: str, secondDateTime: str, secondDateTimeFormat: str) -> GetMinutesBetweenTwoDates:
        """How many minutes are between {{firstDateTime}} to {{secondDateTime}}?.

        Returns the amount of minutes between two given DateTime objects.
        """
        return GetMinutesBetweenTwoDates(firstDateTime, firstDateTimeFormat, secondDateTime, secondDateTimeFormat)

    @staticmethod
    def getsecondsbetweentwodates(firstDateTime: str, firstDateTimeFormat: str, secondDateTime: str, secondDateTimeFormat: str) -> GetSecondsBetweenTwoDates:
        """How many seconds are between {{firstDateTime}} to {{secondDateTime}}?.

        Returns the amount of seconds between two given DateTime objects.
        """
        return GetSecondsBetweenTwoDates(firstDateTime, firstDateTimeFormat, secondDateTime, secondDateTimeFormat)

    @staticmethod
    def getdateinformat(currentDateTimeValue: str, currentDateTimeFormat: str, expectedDateTimeFormatFormat: str, locale: str) -> GetDateInFormat:
        """Format currentDateTime {{currentDateTimeValue}} as {{expectedDateTimeFormatFormat}}.

        Returns a DateTime object in the specified format.
        """
        return GetDateInFormat(currentDateTimeValue, currentDateTimeFormat, expectedDateTimeFormatFormat, locale)

    @staticmethod
    def getcurrentdate(timeZone: str) -> GetCurrentDate:
        """Get current DateTime in ISO 8601 format.

        Returns the current DateTime in ISO 8601 format (yyyy-MM-ddThh:mm:ss.SSS).
        """
        return GetCurrentDate(timeZone)

    @staticmethod
    def getdayofmonth(dateTimeValue: str, dateTimeFormat: str) -> GetDayOfMonth:
        """Get the day of a month from {{dateTimeValue}}.

        Returns the day of a month from the given DateTime object.
        """
        return GetDayOfMonth(dateTimeValue, dateTimeFormat)

    @staticmethod
    def getdayofweek(dateTimeValue: str, dateTimeFormat: str) -> GetDayOfWeek:
        """Get day of the week from {{dateTimeValue}}.

        Returns the day of a week from the given DateTime object.
        """
        return GetDayOfWeek(dateTimeValue, dateTimeFormat)

    @staticmethod
    def getdayofyear(dateTimeValue: str, dateTimeFormat: str) -> GetDayOfYear:
        """Get the day of a year from {{dateTimeValue}}.

        Returns the day of a year from the given DateTime object.
        """
        return GetDayOfYear(dateTimeValue, dateTimeFormat)

    @staticmethod
    def gethour(dateTimeValue: str, dateTimeFormat: str) -> GetHour:
        """Get the hour from {{dateTimeValue}}.

        Returns the hour from the given DateTime object.
        """
        return GetHour(dateTimeValue, dateTimeFormat)

    @staticmethod
    def gethourinstringformat(dateTimeValue: str, dateTimeFormat: str, suffix: bool) -> GetHourInStringFormat:
        """Get hour to string from {{dateTimeValue}}.

        Returns the hour in string format from a given DateTime object (e.g. 09:45 AM).
        """
        return GetHourInStringFormat(dateTimeValue, dateTimeFormat, suffix)

    @staticmethod
    def getmillis(dateTimeValue: str, dateTimeFormat: str) -> GetMillis:
        """Get the milliseconds from {{dateTimeValue}}.

        Returns the milliseconds from the provided DateTime object.
        """
        return GetMillis(dateTimeValue, dateTimeFormat)

    @staticmethod
    def getmillisofday(dateTimeValue: str, dateTimeFormat: str) -> GetMillisOfDay:
        """Get the milliseconds of a day from {{dateTimeValue}}.

        Returns the milliseconds of a day from the provided DateTime object.
        """
        return GetMillisOfDay(dateTimeValue, dateTimeFormat)

    @staticmethod
    def getmillisofsecond(dateTimeValue: str, dateTimeFormat: str) -> GetMillisOfSecond:
        """Get milliseconds of a second from {{dateTimeValue}}.

        Returns the milliseconds of a second from the provided DateTime object.
        """
        return GetMillisOfSecond(dateTimeValue, dateTimeFormat)

    @staticmethod
    def getminutesofday(dateTimeValue: str, dateTimeFormat: str) -> GetMinutesOfDay:
        """Get the minutes of the day from {{dateTimeValue}}.

        Returns the minutes of the day from the provided DateTime object.
        """
        return GetMinutesOfDay(dateTimeValue, dateTimeFormat)

    @staticmethod
    def getminutesofhour(dateTimeValue: str, dateTimeFormat: str) -> GetMinutesOfHour:
        """Get the minutes of hour from {{dateTimeValue}}.

        Returns the minutes of hour from the provided DateTime object.
        """
        return GetMinutesOfHour(dateTimeValue, dateTimeFormat)

    @staticmethod
    def getmonthname(dateTimeValue: str, dateTimeFormat: str) -> GetMonthName:
        """Get the month name from {{dateTimeValue}}.

        Returns the month's name from the provided DateTime object.
        """
        return GetMonthName(dateTimeValue, dateTimeFormat)

    @staticmethod
    def getmonthofyear(dateTimeValue: str, dateTimeFormat: str) -> GetMonthOfYear:
        """Get the month from {{dateTimeValue}}.

        Returns the month from the provided DateTime object.
        """
        return GetMonthOfYear(dateTimeValue, dateTimeFormat)

    @staticmethod
    def getsecondsofday(dateTimeValue: str, dateTimeFormat: str) -> GetSecondsOfDay:
        """Get the seconds of a day from {{dateTimeValue}}.

        Returns the seconds of a day from the provided DateTime object.
        """
        return GetSecondsOfDay(dateTimeValue, dateTimeFormat)

    @staticmethod
    def getsecondsofminute(dateTimeValue: str, dateTimeFormat: str) -> GetSecondsOfMinute:
        """Get the seconds of a minute from {{dateTimeValue}}.

        Returns the seconds of a minute from the provided DateTime object.
        """
        return GetSecondsOfMinute(dateTimeValue, dateTimeFormat)

    @staticmethod
    def getweekofyear(dateTimeValue: str, dateTimeFormat: str) -> GetWeekOfYear:
        """Get the week of a year from {{dateTimeValue}}.

        Returns the week of a year from the provided DateTime object.
        """
        return GetWeekOfYear(dateTimeValue, dateTimeFormat)

    @staticmethod
    def getfullyear(dateTimeValue: str, dateTimeFormat: str) -> GetFullYear:
        """Get the year from {{dateTimeValue}}.

        Returns the year from the provided DateTime object.
        """
        return GetFullYear(dateTimeValue, dateTimeFormat)

    @staticmethod
    def setdays(days: str, originalDateTimeValue: str, originalDateTimeFormat: str, resultFormat: str) -> SetDays:
        """Set {{days}} days to {{originalDateTimeValue}}.

        Sets the days of a given DateTime object and returns the new DateTime object. Can be positive/negative..
        """
        return SetDays(days, originalDateTimeValue, originalDateTimeFormat, resultFormat)

    @staticmethod
    def sethours(hours: str, originalDateTimeValue: str, originalDateTimeFormat: str, resultFormat: str) -> SetHours:
        """Set {{hours}} hours to {{originalDateTimeValue}}.

        Set the hours of a given DateTime object and returns the new DateTime object. Can be positive/negative..
        """
        return SetHours(hours, originalDateTimeValue, originalDateTimeFormat, resultFormat)

    @staticmethod
    def setmillis(milliseconds: str, originalDateTimeValue: str, originalDateTimeFormat: str, resultFormat: str) -> SetMillis:
        """Set {{milliseconds}} milliseconds to {{originalDateTimeValue}}.

        Sets the milliseconds of a given DateTime object and returns the new DateTime object. Can be positive/negative..
        """
        return SetMillis(milliseconds, originalDateTimeValue, originalDateTimeFormat, resultFormat)

    @staticmethod
    def setminutes(minutes: str, originalDateTimeValue: str, originalDateTimeFormat: str, resultFormat: str) -> SetMinutes:
        """Set {{minutes}} minutes to {{originalDateTimeValue}}.

        Sets the minutes of a given DateTime object and returns the new DateTime object. Can be positive/negative..
        """
        return SetMinutes(minutes, originalDateTimeValue, originalDateTimeFormat, resultFormat)

    @staticmethod
    def setmonths(months: str, originalDateTimeValue: str, originalDateTimeFormat: str, resultFormat: str) -> SetMonths:
        """Set {{months}} months to {{originalDateTimeValue}}.

        Sets the months of a given DateTime object and returns the new DateTime object. Can be positive/negative..
        """
        return SetMonths(months, originalDateTimeValue, originalDateTimeFormat, resultFormat)

    @staticmethod
    def setseconds(seconds: str, originalDateTimeValue: str, originalDateTimeFormat: str, resultFormat: str) -> SetSeconds:
        """Set {{seconds}} seconds to {{originalDateTimeValue}}.

        Sets the seconds of a given DateTime object and returns the new DateTime object. Can be positive/negative..
        """
        return SetSeconds(seconds, originalDateTimeValue, originalDateTimeFormat, resultFormat)

    @staticmethod
    def setweeks(weeks: str, originalDateTimeValue: str, originalDateTimeFormat: str, resultFormat: str) -> SetWeeks:
        """Set {{weeks}} weeks to {{originalDateTimeValue}}.

        Sets the weeks of a given DateTime object and returns the new DateTime object. Can be positive/negative..
        """
        return SetWeeks(weeks, originalDateTimeValue, originalDateTimeFormat, resultFormat)

    @staticmethod
    def setyears(years: str, originalDateTimeValue: str, originalDateTimeFormat: str, resultFormat: str) -> SetYears:
        """Set {{years}} years to {{originalDateTimeValue}}.

        Sets the years of a given DateTime object and returns the new DateTime object. Can be positive/negative..
        """
        return SetYears(years, originalDateTimeValue, originalDateTimeFormat, resultFormat)
