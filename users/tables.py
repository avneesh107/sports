import django_tables2 as tables
from .models import Team,College,UserProfile,Match


class TeamTable(tables.Table):
    name = tables.Column(verbose_name="Team Name", accessor='event.name', default="—")
    event = tables.Column(verbose_name="Event")
    gender = tables.Column(verbose_name="Gender", accessor='event.gender', default="—")
    college = tables.Column(verbose_name="College")
    members = tables.TemplateColumn(
        '<a href="{% url \'team_members\' record.pk %}" class="btn btn-outline-primary btn-sm">View</a>',
        verbose_name="Members",
        orderable=False
    )

    class Meta:
        model = Team
        template_name = "django_tables2/bootstrap4.html"
        fields = ("name", "event", "gender", "college")


class ParticipantTable(tables.Table):
    user = tables.Column(verbose_name="Name")
    gender = tables.Column(verbose_name="Gender")
    mobile_number = tables.Column(verbose_name="Phone")
    
    college = tables.TemplateColumn(
        template_code='<a href="{% url \'college_participants\' record.college.id %}">{{ record.college.name }}</a>',
        verbose_name="College"
    )

    class Meta:
        model = UserProfile
        template_name = "django_tables2/bootstrap4.html"
        fields = ("user", "gender", "mobile_number", "college")

class MatchTable(tables.Table):
    event = tables.Column(verbose_name="event")
    start = tables.Column(verbose_name="start-time")
    end = tables.Column(verbose_name="end-time")
    date = tables.Column(verbose_name="date")
    contestants = tables.TemplateColumn(
        template_code= '<a href="{% url \'contest_team\' record.pk %}" class="btn btn-outline-primary btn-sm">View</a>',
        verbose_name="Contestants",
    )



    class Meta:
        model = Match
        template_name = "django_tables2/bootstrap4.html"
        fields = ("event", "start", "end","date","contestants" )




