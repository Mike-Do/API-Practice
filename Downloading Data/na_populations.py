import pygal
import lxml

from pygal.maps.world import World
from lxml.html import open_in_browser

wm = pygal.maps.world.World()
wm.title = 'Populations of Countries in North America'
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('/Users/Mike/Desktop/python_work/Downloading Data/na.svg')