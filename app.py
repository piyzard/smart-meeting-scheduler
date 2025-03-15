from datetime import datetime, time, timedelta

class MeetingScheduler:
    def __init__(self):
        self.working_hours = (time(9, 0), time(17, 0))
        self.meetings = []
        self.holidays = []

    def add_holiday(self, holiday):
        self.holidays.append(holiday)

    def is_working_day(self, date):
        return date.weekday() < 5 and date not in self.holidays

    def is_available_slot(self, start_time, end_time):
        for meeting in self.meetings:
            if meeting["start"] < end_time and start_time < meeting["end"]:
                return False
        return True

    def schedule_meeting(self, date, start_time, duration_in_hours):
        start_datetime = datetime.combine(date, start_time)
        end_datetime = start_datetime + timedelta(hours=duration_in_hours)

        if not self.is_working_day(date):
            return "Cannot schedule on weekends or holidays."

        if not (self.working_hours[0] <= start_time <= self.working_hours[1]):
            return "Meeting time is outside working hours."

        if self.is_available_slot(start_datetime, end_datetime):
            self.meetings.append({"start": start_datetime, "end": end_datetime})
            return "Meeting scheduled successfully."
        else:
            return "Time slot unavailable."

    def view_schedule(self):
        return sorted(self.meetings, key=lambda m: m["start"])

scheduler = MeetingScheduler()

scheduler.add_holiday(datetime(2025, 3, 18).date())

print(scheduler.schedule_meeting(datetime(2025, 3, 19).date(), time(10, 0), 1))
print(scheduler.schedule_meeting(datetime(2025, 3, 19).date(), time(11, 0), 1))

for meeting in scheduler.view_schedule():
    print(f"Meeting from {meeting['start']} to {meeting['end']}")
