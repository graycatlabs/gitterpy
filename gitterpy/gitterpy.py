"""
 gitterpy.py
 Copyright (c) 2015 - Gray Cat Labs, Alex Hiam <alex@graycat.io>

 A Gitter client API in Python.
"""

import requests, urlparse, json
from time import sleep

class Gitter(object):
  rest_api_url = "https://api.gitter.im/v1/"
  stream_api_url = "https://stream.gitter.im/v1/"

  def __init__(self, api_token):
    self.api_token = None
    # Same headers are used for all requests:
    self.headers = { 
      "Content-Type" : "application/json; charset=utf-8",
      "Accept" : "application/json",
      "Authorization" : "Bearer {}".format(api_token)
      }

    # Find the user ID, which is used in some API requests (also tests the 
    # given auth token):
    user_info = self.getUser()
    self.user_id = user_info[0].get("id")
    if not self.user_id:
      raise ValueError("could not connect to Gitter with given auth token")

  def getUser(self):
    """ Returns the info for the user.
    """
    return self._get("user")

  def getRooms(self):
    """ Returns a list of rooms the user is a part of.
    """
    return self._get("user/{}/rooms".format(self.user_id))

  def getChannels(self):
    """ Returns a list of channels nested under the user.
    """
    return self._get("user/{}/rooms".format(self.user_id))

  def getRepos(self):
    """ Returns a list of the user's repos and their associated rooms if 
        available.
    """
    return self._get("user/{}/repos".format(self.user_id))

  def joinRoom(self, room_name):
    """ Joins the given room. Returns server response if successful, None 
        otherwise.
    """
    return self._post("rooms", uri=room_name)

  def leaveRoom(self, room_name):
    """ Leaves the given room. Returns server response if successful, None 
        otherwise.
    """
    room_id = self.roomIdFromName(room_name)
    uri = "rooms/{}/users/{}".format(room_id, self.user_id)
    return self._delete(uri)

  def sendMessage(self, room_name, message):
    """ Sends the given message in the given room. Returns server response
      if successful, None otherwise.
    """
    room_id = self.roomIdFromName(room_name)
    return self._post("rooms/{}/chatMessages".format(room_id), text=message)

  def roomStream(self, room_name):
    """ Returns a requests.request object with stream=True, which can be
        iterated over to get live messages in the given room.
        See: http://docs.python-requests.org/en/master/user/advanced/#streaming-requests
    """
    room_id = self.roomIdFromName(room_name)
    return self._stream("rooms/{}/chatMessages".format(room_id))

  def roomIdFromName(self, room_name):
    info = self._get("rooms")
    for room in info:
      if room.get("name") == room_name:
        return room.get("id")
    return None

  def listMessagesCursor(self, room_name, sleep_time=1.0):
    """
    Makes a cursor to iterate through message objects present to past.

    See: https://developer.gitter.im/docs/messages-resource

    API self-throttling: Between every iteration, the generator sleeps the
    process for some float value ``sleep_time`` in seconds.
    """
    room_id = self.roomIdFromName(room_name)

    # yield first batch of <= 100 message objects
    url_f = "rooms/{0}/chatMessages?limit=100"
    data = self._get(url_f.format(room_id))
    if not data:
      raise StopIteration()
    before_id = data[0].get("id")
    for message in reversed(data):
      yield message

    # yield consecutive batches
    url_f = "rooms/{0}/chatMessages?limit=100&beforeId={1}"
    while True:
      sleep(sleep_time)

      data = self._get(url_f.format(room_id, before_id))
      if not data:
        raise StopIteration()
      before_id = data[0].get("id")
      for message in reversed(data):
        yield message

    StopIteration()

  def _stream(self, path):
    """ Makes a GET request to the given path, returning the response
        if successful and None otherwise.
    """
    if path[0] == "/":
      path = path[1:]
    url = urlparse.urljoin(self.stream_api_url, path)
    return requests.get(url, headers=self.headers, stream=True)
    

  def _get(self, path):
    """ Makes a GET request to the given path, returning the response
        if successful and None otherwise.
    """
    if path[0] == "/":
      path = path[1:]
    url = urlparse.urljoin(self.rest_api_url, path)
    r = requests.get(url, headers=self.headers)
    try:
      response = json.loads(r.content)
    except ValueError:
      return None
    return response

  def _post(self, path, **json_data):
    """ Makes a POST request to the given path with the given data, 
        returning the response if successful and None otherwise.
    """
    if path[0] == "/":
      path = path[1:]
    url = urlparse.urljoin(self.rest_api_url, path)
    r = requests.post(url, headers=self.headers, json=json_data)
    try:
      response = json.loads(r.content)
    except ValueError:
      return None
    return response

  def _delete(self, path):
    """ Makes a DELETE request to the given path, returning the 
        response if successful and None otherwise.
    """
    if path[0] == "/":
      path = path[1:]
    url = urlparse.urljoin(self.rest_api_url, path)
    r = requests.delete(url, headers=self.headers)
    try:
      response = json.loads(r.content)
    except ValueError:
      return None
    return response
