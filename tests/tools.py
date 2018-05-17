from nose.tools import *
import re

def assert_response(resp, contains=None, matches=None, headers=None, status="200"):
	assert status in resp.status, "Expected %r, got %r" % (status, resp.status)
	if status == '200':
		assert resp.data, "Response data empty"

	if contains:
		assert contains in resp.data, "Response doesnt contain %r" % contains

	if matches:
		reg = re.compile(matches)
		assert reg.matches(resp.data), "Response doesnt match %r" % matches

	if headers:
		assert_equal(resp.headers, headers)