from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year=year
		self.month=month
		super(Calendar, self).__init__()
	
	def formatday(self, day, events):
		events=events.filter(start_time__day=day)
		d=""
		for event in events:
			d+=f'<li> <a href= "/eventdetail/{event.id}">{event.event_title}</a></li>'
		if day!=0:
			return f"<td><span class='date'>{day}</span><ul>{d}</ul></td>"
		return "<td></td>"

	def formatweek(self, week, events):
		a_week=""
		for d, weekday in week:
			a_week+=self.formatday(d,events)
		return f'<tr>{a_week}</tr>'
	def formatmonth(self,withyear=True):
		events=Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
		cal=f'<table class="calendar">\n'
		cal+=f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		cal+=f'</table>'
		return cal
