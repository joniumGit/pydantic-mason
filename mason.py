"""
Provides Pydantic models for representing the JSON elements in the Mason standard

https://github.com/JornWildt/Mason/blob/master/Documentation/Mason-draft-2.md

From: https://github.com/joniumGit/pydantic-mason
"""
from datetime import datetime
from enum import Enum
from typing import Optional, Dict, List

from pydantic import BaseModel, Field, AnyUrl

MASON: str = 'application/vnd.mason+json'


class EncodingEnum(str, Enum):
    """
    Contains the allowed values for Mason Control encoding field
    """
    none = 'none'
    json = 'json'
    json_files = 'json+files'
    raw = 'raw'


class FileDescriptor(BaseModel):
    """
    Model for Mason Control file descriptors
    """
    name: str
    title: Optional[str]
    description: Optional[str]
    accept: Optional[List[str]]


class AltControl(BaseModel):
    """
    Base model for a Mason control
    """
    href: AnyUrl
    isHrefTemplate: Optional[bool]
    title: Optional[str]
    description: Optional[str]
    method: Optional[str] = Field(default="GET")
    encoding: Optional[EncodingEnum] = EncodingEnum.none
    schema_: Optional[Dict] = Field(alias='schema')
    schemaUrl: Optional[AnyUrl]
    template: Optional[Dict]
    accept: Optional[List[str]]
    output: Optional[List[str]]
    files: Optional[List[FileDescriptor]]


class Control(AltControl):
    """
    Mason control

    Adds the capability to have alternative controls
    """
    alt: Optional[List[AltControl]]


class Meta(BaseModel):
    """
    Mason Meta
    """
    title: Optional[str] = Field(None, alias='@title')
    description: Optional[str] = Field(None, alias='@description')
    controls: Optional[Dict[str, Control]] = Field(None, alias='@controls')


class Namespace(BaseModel):
    """
    Wrapper for a namespace object

    Might have more properties in the future so this is represented as a class.
    Another possibility would be to simple serialize this as a Dict[str,str]
    """
    name: str


class Error(BaseModel):
    """
    Mason error element
    """
    message: str = Field(alias='@message')
    id: Optional[str] = Field(None, alias='@id')
    code: Optional[str] = Field(None, alias='@code')
    messages: Optional[List[str]] = Field(None, alias='@messages')
    details: Optional[str] = Field(None, alias='@details')
    httpStatusCode: Optional[int] = Field(None, alias='@httpStatusCode')
    controls: Optional[Dict[str, Control]] = Field(None, alias='@controls')
    time: Optional[datetime] = Field(None, alias='@time')


class MasonBase(BaseModel):
    """
    Base class for Mason

    Can be used as a mix-in class to add Mason capability
    """
    meta: Optional[Meta] = Field(None, alias='@meta')
    namespaces: Optional[Dict[str, Namespace]] = Field(None, alias='@namespaces')
    controls: Optional[Dict[str, Control]] = Field(None, alias='@controls')
    error: Optional[Error] = Field(None, alias='@error')

    class Config:
        allow_population_by_field_name = True


__all__ = [
    'MASON',
    'Control',
    'Namespace',
    'Meta',
    'Error',
    'MasonBase',
    'AltControl',
    'FileDescriptor',
    'EncodingEnum',
    'datetime',
]
