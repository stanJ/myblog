#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import orm
from models import User
import asyncio

async def test(loop):
    await orm.create_pool(loop, user='root', password='password', db='awesome')

    # u = await User.find('00150330858907615e816dda62d422b9983e8bbe0f11499000')
    # u.name = 'test111'
    # await u.update()
    # u = await User.findAll(where=r"name='test111'")
    # a = await User.findNumber('name')
    # print(a)
    # u = User(email='hh@qq.com', passwd='123456', name='张三', image='about:blank')
    # await u.save()
    # u = await User.find('00150330858907615e816dda62d422b9983e8bbe0f11499000')
    # await u.remove()
    await orm.destroy_pool()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()