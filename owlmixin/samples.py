# coding: utf-8

from __future__ import division, absolute_import, unicode_literals

from owlmixin.owlcollections import TList, TDict
from owlmixin.owlenum import OwlEnum, OwlObjectEnum
from owlmixin import OwlMixin, Option


class Animal(OwlObjectEnum):  # pragma: no cover
    DOG = ("dog", "bow-wow")
    CAT = ("cat", "mewing")

    def crow(self):
        return self.object


class Color(OwlEnum):  # pragma: no cover
    RED = "red"
    GREEN = "green"
    BLUE = "blue"


class Food(OwlMixin):  # pragma: no cover
    name: str
    names_by_lang: Option[TDict[str]]


class Human(OwlMixin):  # pragma: no cover
    id: int
    name: str
    favorites: TList[Food]


class Machine(OwlMixin):  # pragma: no cover
    id: int
    name: str
