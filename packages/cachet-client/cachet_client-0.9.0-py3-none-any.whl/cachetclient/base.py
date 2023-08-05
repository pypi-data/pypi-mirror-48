from cachetclient.httpclient import HttpClient
from typing import Union


class Resource:
    """Bag of attributes"""
    def __init__(self, manager, data):
        self._manager = manager
        self._data = data

    @property
    def attrs(self) -> dict:
        """The raw json respons from the server"""
        return self._data

    def get(self, name) -> Union[int, str, float, bool]:
        """Obtain any attribute name for the resource"""
        return self._data.get(name)

    def update(self):
        return self._manager.update(self.get('id'), **self.attrs)

    def delete(self) -> None:
        self._manager.delete(self.get('id'))

    def __repr__(self) -> str:
        return str(self)

    def __str__(self) -> str:
        return str(self._data)


class Manager:
    """
    Base class for handling crud resources
    """
    resource_class = Resource
    path = None  # Type: str

    def __init__(self, http_client: HttpClient):
        self._http = http_client

        if self.resource_class is None:
            raise ValueError('resource_class not defined in class {}'.format(self.__class__))

        if self.path is None:
            raise ValueError('path not defined for class {}'.format(self.__class__))

    def _create(self, path, data):
        response = self._http.post(path, data=data)
        return self.resource_class(self, response.json()['data'])

    def _update(self, path, resource_id, data):
        response = self._http.put("{}/{}".format(path, resource_id), data=data)
        return self.resource_class(self, response.json()['data'])

    def _list_paginated(self, path, page=1, per_page=20):
        while True:
            result = self._http.get(
                path,
                params={
                    'page': page,
                    'per_page': per_page,
                },
            )
            json_data = result.json()

            meta = json_data['meta']
            data = json_data['data']

            for entry in data:
                yield self.resource_class(self, entry)

            if page >= meta['pagination']['total_pages']:
                break

            page += 1

    # def _search(self, path, params=None):
    #     params = params or {}
    #     result = self._http.get(path, params={'per_page': 1, **params})
    #     json_data = result.json()

    def _get(self, path, resource_id):
        result = self._http.get("{}/{}".format(path, resource_id))
        json_data = result.json()
        return self.resource_class(self, json_data['data'])

    def _count(self, path):
        result = self._http.get(path, params={'per_page': 1})
        json_data = result.json()
        return json_data['meta']['pagination']['total']

    def _delete(self, path, resource_id):
        self._http.delete(path, resource_id)

    def _build_data_dict(self, **kwargs):
        """
        Builds a data dictionary for posting to the server.
        Will ommit key/value pars with None values.
        This makes partial updates less error prone.
        """
        return {key: value for key, value in kwargs.items() if value is not None}
