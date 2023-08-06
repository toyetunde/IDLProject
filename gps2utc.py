from astropy.time import Time
def gps2utc(gpsweek, gpsseconds):
    """ GPS time to UTC.
    Parameters
    ----------
    gpsweek : inpi
        GPS week number, i.e. 1866.
    gpsseconds : inpi
        Number of seconds since the beginning of week.
    Returns
    -------
    datetime
        datetime instance with UTC time.
    """
    secs_in_week = 604800
    secs = gpsweek * secs_in_week + gpsseconds

    t_gps = Time(secs, format="gps")
    t_utc = Time(t_gps, format="iso", scale="utc")

    return t_utc.datetime
