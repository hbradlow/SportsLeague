from django import template






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
def overall_points(fraternity, sport_type):
    sport = Sport.objects.filter(type=sport_type)[0] #in case there is more than one sport of that type for some reason (HACK)
    return fraternity.overall_points_for_sport( sport )
