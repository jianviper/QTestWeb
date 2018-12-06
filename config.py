#!/usr/bin/env python
#coding:utf-8
import os
basedir=os.path.dirname(os.path.dirname(__file__))

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or ''