from . import common
from datetime import timedelta, datetime, date, timezone
from urllib import request

import urllib.request, json, asyncio
import voluptuous as vol
import homeassistant.helpers.config_validation as cv

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.entity import Entity
from homeassistant.util import Throttle

MIN_TIME_BETWEEN_UPDATES = timedelta(minutes=60)
SCAN_INTERVAL = timedelta(minutes=30)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(common.CONF_APIKEY): cv.string
    }
)

async def async_setup_entry(hass, config_entry, async_add_entities):
    session = async_get_clientsession(hass)
    apikey = hass.data[common.DOMAIN][config_entry.entry_id]
    
    restaurantAPIList = await get_restaurants(session, apikey)
    restaurantEntitesList = []
    for restaurant in restaurantAPIList['restaurants']:
        menu = LunchaIMjardeviMenu(restaurant['id'], restaurant['name'], apikey)
        restaurantEntitesList.append(menu)

    async_add_entities(restaurantEntitesList, update_before_add=True)


async def get_menu(session, id, apikey):
    url = "https://lunchaimjardevi.com/api/v4/getMenu?id=" + id + "&key=" + apikey
    async with session.get(url) as resp:
        data = await resp.json()
        return data

async def get_restaurant_info(session, id, apikey):
    url = "https://lunchaimjardevi.com/api/v4/getRestaurantInfo?id=" + id + "&key=" + apikey
    async with session.get(url) as resp:
        data = await resp.json()
        return data

async def get_restaurants(session, apikey):
    url = "https://lunchaimjardevi.com/api/v4/getRestaurants?showOutsideMjardevi=true&key=" + apikey
    async with session.get(url) as resp:
        data = await resp.json()
        return data


class LunchaIMjardeviMenu(Entity):

    def __init__(self, id, name, apikey):
        """Initialize the sensor."""

        self._attr_unique_id = "lunchaimjardevi_" + id
        self._apikey = apikey
        self._id = id
        self._name = name
        self._state = None
        self._icon = "mdi:food-fork-drink"
        
    @property
    def name(self):
        """Return the name of the sensor."""
        return self._name

    @property
    def state(self):
        """Return the state of the sensor."""
        return self._state
    
    @property
    def icon(self):
        """Icon to use in the frontend."""
        return self._icon

    @Throttle(MIN_TIME_BETWEEN_UPDATES)
    async def async_update(self) -> None:
        """Get the latest data and updates the states."""
        session = async_get_clientsession(self.hass)

        menu = await get_menu(session, self._id, self._apikey)
        restaurantInfo = await get_restaurant_info(session, self._id, self._apikey)

        today = date.today()
        week = today.isocalendar().week
        weekDays = ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lördag', 'Söndag']

        skolmatCard = {}
        if not week in skolmatCard:
            skolmatCard[week] = []

        dayEntry = {
            "weekday": weekDays[today.weekday()],
            "date": today.isoformat(),
            "week": (week),
            "courses": []
        }

        state = ""
        if menu is not None and 'menuItems' in menu:
            i = 0
            for item in menu['menuItems']:
                if(i != 0):
                    state += ", "
                i += 1
                state += item['title'].replace(",", "")
                dayEntry['courses'].append(item['title'])

        skolmatCard[week].append(dayEntry)

        self._state = state
        self._attr_extra_state_attributes = {
            "latitude": restaurantInfo['info']['coordLat'],
            "longitude": restaurantInfo['info']['coordLong'],
            "website": restaurantInfo['info']['website'],
            "note": restaurantInfo['info']['note'],
            "calendar": skolmatCard
        }
        return None