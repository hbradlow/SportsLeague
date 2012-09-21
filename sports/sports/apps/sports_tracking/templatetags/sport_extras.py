from django import template


from sports_tracking.models import Fraternity, Sport



register = template.Library()

@register.filter
def get_range( value ):
  """
    Filter - returns a list containing range made from given value
    Usage (in template):

    <ul>{% for i in 3|get_range %}
      <li>{{ i }}. Do something</li>
    {% endfor %}</ul>

    Results with the HTML:
    <ul>
      <li>0. Do something</li>
      <li>1. Do something</li>
      <li>2. Do something</li>
    </ul>

    Instead of 3 one may use the variable set in the views
  """
  return [v + 1 for v in range(value)]

@register.filter
def list_iter( lists ):
    list_a, list_b = lists
    for x, y in zip(list_a, list_b):
        yield (x, y)
    for x in list_iter((list_a, list_b)):
        print x

@register.filter
def stats(fraternity, sport_type):
    from collections import defaultdict
    try:
        sport = Sport.objects.get(type=sport_type)
    except Sport.DoesNotExist:
        return defaultdict(lambda: "NA")
    return fraternity.stats_for_sport( sport )

@register.filter
def overall_points(fraternity, sport_type):
    try:
        sport = Sport.objects.get(type=sport_type)
    except Sport.DoesNotExist:
        return "N/A"
    return fraternity.overall_points_for_sport( sport )

@register.filter
def season(sports, season):
    filtered_sports = []
    for sport in sports:
        if sport.season == season:
            filtered_sports.append(sport)
    return filtered_sports

@register.filter
def group(sport, group_name):

    return sport.group_set.get(group=group_name).fraternities.all()

@register.inclusion_tag("sports_tracking/team_table.html",takes_context=True)
def team_table(context,sport=None):
    return {"sport":sport,"request":context['request'],"fraternities":context['fraternities'],"sports":context["sports"]}
