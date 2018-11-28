#coding=utf-8
import json
import os
import signal
from time import sleep

import bjoern

from apiworks.caoe import install
from apiworks.server.wsgi.router import Router

router = Router()

# @router.route("^/(?P<tags>.+)/")

# @router.route("^/(.+)/(.+)/1234/5678", mode='group')
# def test(a,b):
#     print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
#     return a+'hello'+b

@router.route("^/favicon.ico", mode='group')
def test():
    return 'icon'
# @router.route("^/b/", msg=23)
# def test(msg='default'):
#     print(msg)
#     return 'bbb'

front = Router()
front.route("^/blog")(router)
# front.route("^/wiki")(router)
# @front.route("^/blog", mode='group')
# def test(tags):
#     print(tags, 'mmmmmmmmmmmm')
#     return tags, 200



front2 = Router()
front2.route("^/blog")(front)




def should_be_int(data):
    print(data, '.......')
    return int(data)


@router.route("^/(.+)", mode='group', validator=should_be_int)
#@router.route("^/a/", mode='group')
def test(tags):
    print(tags, 'mmmmmmmmmmmm')
    print(type(tags))
    return str(tags), 200


@router.route("^/123/", mode='group')
def test2():
    print('hellohello')
    return 'hello'

@router.route("^/b", mode='group')
def test3():
    return 'aaaaa'

api = front2
print(api.rules)

# router.route("^/blog")(router)


# def ap1(environ, start_response):
#     # ... do your WSGI app
# #     print('here'*400)
#     start_response("200 OK", [])
#     return b'xxxxxxxxxxxx'
# def entries(environ, start_response):
#    ... do your WSGI app
    # start_response("200 OK", [])
    # return [b"Some content"]
# @router.route("^/entries/")
# def blog_entries(environ, start_response):
#    # ... do your WSGI app
#    start_response("200 OK", [])
#    return [b"Some content"]

# @router.route("^/entries/(.*)/")
# def entry_detail(environ, start_response):
#    args = environ['router.args']
#    slug = args[0]
#
#    # .. lookup blog entry
#    start_response("200 OK", [])
#    return [b"Some content"]
#
# @router.route("^/entries/tags/(?P<tags>.+)/")
# def entries_by_tag(environ, start_response):
#    kwargs = environ['router.kwargs']
#    tags = kwargs['tags']
#
#    # ... Do your magic
#    start_response("200 OK", [])
#    return [b"Some content"]

# if __name__ == '__main__':
#     install()
#     print('hello world', os.getpid())
#     a='hello world'
#     bjoern.listen(api, '127.0.0.1', 8083)
#     print(NUM_WORKERS,'>>>>>>.')
#     for i in range(NUM_WORKERS):
#         a += str(i)
#         pid = os.fork()
#         print('loop begin',i, pid)
#         if pid > 0:
#             #pid>0时是父进程，返回的pid是子进程的pid
#
#             worker_pids.append(pid)
#         elif pid == 0:
#             print('..............sub process')
#             #pid为0时是子进程
#             # try:
#             bjoern.run()
#             # except KeyboardInterrupt:
#             #     print('keyboard interrupt')
#             #     pass
#             # except Exception as e:
#             #     print(e)
#             #     print(type(e))
#             #     print('hahahah')
#             #     pass
#             print('loop end.',i)
#             exit()
#             print('after')
#         print('loop end',i, pid)
#
#     # try:
#     for _ in range(NUM_WORKERS):
#         print('here')
#         os.wait()
#     # except KeyboardInterrupt:
#     #     for pid in worker_pids:
#     #         print('kill ', pid)
#     #         os.kill(pid, signal.SIGINT)
#
#
#

