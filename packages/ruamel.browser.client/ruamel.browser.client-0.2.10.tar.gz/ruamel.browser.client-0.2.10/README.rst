
zmq based client to talk with ruamel.browser.server

Example from commandline::

  rbc init abc selenium
  rbc br abc get http://stackoverflow.com
  rbc br abc find store sbox css "#search > input"
  rbc br abc elem sbox keys 'ruamel.yaml
  '
  sleep 1
  rbc br abc find css ".js-search-results > div:first-child h3"
  rbc br abc inner

Yes that is a newline within the quotes. The `store sbox` and `elem sbox` are not
really necessary here.

You have to have ``ruamel.browser.server.selenium`` installed, and started the server
with ``rbs``
