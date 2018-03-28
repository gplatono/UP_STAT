import pandas
from pandas import Series
import dateutil.parser
from matplotlib import pyplot

crime_data = pandas.read_csv("datasets/RPD__Part_I_Crime_2011_to_Present.csv")
weather_data = pandas.read_csv('1261407.csv')
#crime_data = crime_data.values
crime_data['datetime'] = pandas.to_datetime(crime_data.OccurredFrom_Timestamp, format="%Y.%m.%d %H:%M:%S.%f")
crime_data['day'] = crime_data['datetime'].apply(lambda x: x.day)
crime_data['weekday'] = crime_data['datetime'].apply(lambda x: x.weekday())
crime_data['yearday'] = crime_data['datetime'].apply(lambda x: x.timetuple().tm_yday)
crime_data['temp'] = weather  
weather_data['datetime'] = pandas.to_datetime(weather_data.DATE, format="%Y.%m.%d")
weather_data['year'] = weather_data['datetime'].apply(lambda x: x.year)
#crime_data['yearday'] = crime_data['datetime'].apply(lambda x: x.timetuple().tm_yday)
weather_data['avg'] = (weather_data.TMAX + weather_data.TMIN) / 2
#print dateutil.parser.parse(crime_data.OccurredFrom_Timestamp[0]).day



print crime_data.datetime[1], crime_data.OccurredFrom_Timestamp[1], crime_data.datetime[1].year, crime_data['day'][1], crime_data['weekday'][1]

#ser = pandas.Series(crime_data.weekday)
#print ser
#pyplot.figure()
#ser.hist(ser)
data2012 = crime_data.loc[crime_data["OccurredFrom_Date_Year"] == 2011]
weather2012 = weather_data.loc[weather_data["year"] == 2011]
weather_data.groupby(['OccurredFrom_Date_Month', )
weather2012.reset_index(drop=True, inplace=True)
#print weather2012

crime_grouped = data2012.groupby('yearday')['yearday'].size().to_frame()
#print crime_grouped
print crime_grouped['yearday'].corr(weather2012['avg'])

#print weather_data['year']

#pyplot.hist(data2012['yearday'], bins=365, align='mid', histtype='bar')
pyplot.plot(crime_grouped['yearday'], '-r', label="Crimes")
pyplot.plot(weather2012['avg'], '-b', label="Weather")
#line_up = pyplot.plot(crime_grouped['yearday'], label="Crimes")
#line_down = pyplot.plot(weather2012['avg'], label="Weather")
#pyplot.legend(handles=[line_up, line_down])
#crime_data.hist(column='yearday', bins=365)
#crime_data.hist(column='OccurredFrom_Date_Month', bins=12)
#crime_data.plot(kind='hist', use_index=crime_data.columns.get_loc('weekday'), bins=7)
#pyplot.plot()
pyplot.show()
