import datetime
import times

def test_given_input():
    large = times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
        #output = (times.overlap_time(large, short))
    result = (times.overlap_time(large, short))
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected    


test_given_input() #this runs the function 

def test_class_time():
    large = times.time_range("2019-10-31 10:00:00", "2019-10-31 13:00:00")
    short = times.time_range("2019-10-31 10:05:00", "2019-10-31 12:55:00", 3, 60)
    result = times.overlap_time(large,short)
    assert result == short

'''
 no overlapping times instead of years 1/1 - 1/2, 1/3 -1/4
 gap time larger then range  >> error
 two time ranges are exactly the same aka. overlap of identical times >> time
 overlapping across different dates 1/1 - 1/3, 1/2 1/4
 what when 1st < 2nd >> overlap
 2nd = Gap of 1st
 wrong format input >> error
 end date earlier then start date  t1 < t0
 time is negative, BC
 Different time format, such as American time format >> error
'''

def test_20_min():
    large = times.time_range("2019-01-01 00:00:00", "2019-01-01 23:50:00", 24, 10 * 60)
    short = times.time_range("2019-01-01 00:30:00", "2019-01-01 23:55:00", 24, 35 * 60)
    result = times.overlap_time(large, short)
    #import pdb; pdb.set_trace()
    assert all([(datetime.datetime.strptime(t1, "%Y-%m-%d %H:%M:%S") - 
    datetime.datetime.strptime(t0, "%Y-%m-%d %H:%M:%S")).total_seconds() == 20 * 60
    for t0,t1 in result])
    
